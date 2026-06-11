import boto3
import os
from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import mysql.connector

app = Flask(__name__)
app.secret_key = "classroom-secret-key"

s3 = boto3.client('s3')

BUCKET_NAME = "virtual-classroom-materials-siddhesh"

@app.route('/')
def home():
    return render_template('home.html')

def get_db_connection():
    conn = mysql.connector.connect(
        host='virtual-classroom-db.cp8g0ice8db5.ap-south-1.rds.amazonaws.com',
        user='admin',
        password='Classroom123',
        database='classroom'
    )
    return conn


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        hashed_password = generate_password_hash(password)

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, hashed_password)

        cursor.execute(query, values)

        conn.commit()

        cursor.close()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':

        username = request.form['username']
        password = request.form['password']

        conn = get_db_connection()
        cursor = conn.cursor()

        query = "SELECT * FROM users WHERE username=%s"
        cursor.execute(query, (username,))

        user = cursor.fetchone()

        cursor.close()
        conn.close()

        if user and check_password_hash(user[2], password):

            if user[3] == "instructor":
                return redirect('/upload')

            return redirect('/dashboard')

        return "Invalid Credentials"

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():
    
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
SELECT *
FROM materials
ORDER BY upload_date DESC
""")
    materials = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('dashboard.html', materials=materials)

    # course_urls = [
    #     "https://virtual-classroom-materials-siddhesh.s3.ap-south-1.amazonaws.com/pexels-optically-challenged-12088462.jpg",
    #     "https://virtual-classroom-materials-siddhesh.s3.ap-south-1.amazonaws.com/Siddhesh1st.pdf"
    # ]
    

    #return render_template('dashboard.html', course_urls=course_urls)
    
    
# @app.route('/upload')
# def upload():
#     return render_template('upload.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload():

    if request.method == 'POST':

        title = request.form['title']
        file = request.files['file']

        if file:

            filename = file.filename

            s3.upload_fileobj(
                file,
                BUCKET_NAME,
                filename
            )

            file_url = f"https://{BUCKET_NAME}.s3.ap-south-1.amazonaws.com/{filename}"

            conn = get_db_connection()
            cursor = conn.cursor()

            query = """
            INSERT INTO materials
            (title, file_url, uploaded_by)
            VALUES (%s, %s, %s)
            """

            cursor.execute(
                query,
                (title, file_url, "Instructor")
            )

            conn.commit()

            cursor.close()
            conn.close()

            flash("Material uploaded successfully!")

    return render_template('upload.html')

if __name__ == '__main__':
    app.run(debug=True)
