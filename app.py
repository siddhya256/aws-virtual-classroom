from flask import Flask
from flask import Flask, render_template, request, redirect, url_for
from werkzeug.security import generate_password_hash
from werkzeug.security import check_password_hash
import mysql.connector

app = Flask(__name__)

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

conn = get_db_connection()
print("Database Connected")
conn.close()

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
            return redirect('/dashboard')

        return "Invalid Credentials"

    return render_template('login.html')

@app.route('/dashboard')
def dashboard():

    course_urls = [
        "https://virtual-classroom-materials-siddhesh.s3.ap-south-1.amazonaws.com/pexels-optically-challenged-12088462.jpg",
        "https://virtual-classroom-materials-siddhesh.s3.ap-south-1.amazonaws.com/Siddhesh1st.pdf"
    ]

    return render_template('dashboard.html', course_urls=course_urls)

if __name__ == '__main__':
    app.run(debug=True)