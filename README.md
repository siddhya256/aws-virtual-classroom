1. Project Title
AWS Hosted Virtual Classroom using Flask, AWS EC2, AWS RDS and AWS S3



<img width="1900" height="910" alt="image" src="https://github.com/user-attachments/assets/1d7587ab-33bc-4b30-ba65-00f75134f6b6" />

<img width="1904" height="903" alt="image" src="https://github.com/user-attachments/assets/9fe4ca8e-fb2f-49e3-b827-c58b1b47db77" />

<img width="1901" height="926" alt="image" src="https://github.com/user-attachments/assets/5276ec6d-73e8-4b4e-949b-adf6780f9344" />


2. Project Overview - 
The AWS Hosted Virtual Classroom is a cloud-based learning platform developed to provide online course material access for students and content management capabilities for instructors.
The system is hosted completely on Amazon Web Services (AWS) and follows a client-server architecture.
Students can:
•	Register 
•	Login 
•	View available course materials 
•	Download learning resources 
•	Instructors can:
•	Login 
•	Upload course materials 
•	Manage classroom resources 
All uploaded resources are stored securely in AWS S3 and their metadata is maintained in AWS RDS MySQL database.

3. Problem Statement -
Traditional classroom material distribution methods are inefficient and difficult to manage remotely.
The objective of this project is to:
•	Provide centralized access to course materials 
•	Enable instructors to upload resources from anywhere 
•	Allow students to access materials online 
•	Demonstrate cloud computing concepts using AWS services

4. Objectives -
Primary Objectives
•	Build a cloud-hosted classroom platform 
•	Implement secure user authentication 
•	Store course materials in AWS S3 
•	Maintain user and material data in AWS RDS 
•	Provide instructor and student access control 
Secondary Objectives
•	Learn AWS Cloud Services 
•	Implement Flask Web Framework 
•	Deploy applications on AWS EC2 
•	Integrate cloud storage and databases


5. Technologies Used -
Component		-	Technology
Frontend		-	HTML, CSS, JavaScript
Backend		-	Python Flask
Database		-	MySQL
Cloud Server		-	AWS EC2
Database Service	-	AWS RDS
Storage Service	-	AWS S3
Web Server		-	Nginx
Application Server	-	Gunicorn
Version Control	-	Git & GitHub

6. AWS Services Used -
6.1 Amazon EC2
Used for:
•	Hosting Flask Application 
•	Running Gunicorn 
•	Running Nginx Web Server 


Instance Details
•	Ubuntu Server 
•	t2.micro 
•	Public IP Access 

6.2 Amazon RDS
Used for:
•	Storing user records 
•	Storing uploaded material information 
Database Engine
MySQL
Database Name
classroom

6.3 Amazon S3
Used for:
•	Uploading PDFs 
•	Uploading Images 
•	Storing Course Materials



7. System Architecture -
Student / Instructor
          |
          |
      Nginx
          |
          |
      Gunicorn
          |
          |
      Flask App
       /     \
      /       \
 AWS RDS      AWS S3
(MySQL)      (Files)






8. Database Design -
Users Table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(100),
    password VARCHAR(255),
    role VARCHAR(50)
);
Purpose
Stores:
•	Student Accounts 
•	Instructor Accounts 

Materials Table
CREATE TABLE materials (
    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    file_url TEXT,
    uploaded_by VARCHAR(100),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Purpose
Stores:
 Material Title 
 S3 URL 
 Instructor Name 
 Upload Timestamp

 9. Project Modules -

Module 1: Welcome Page
Features
•	Attractive Landing Page 
•	Project Introduction 
•	Navigation Menu 
•	Login Button 
•	Registration Button 
Purpose
Provides entry point to the system.

Module 2: Student Registration
Features
•	Username Creation 
•	Password Creation 
•	Password Hashing 
Security
Passwords are stored as hashed values using Werkzeug Security.

Module 3: Login System
Features
•	Username Authentication 
•	Password Verification 
•	Role Based Access 
Roles :-
Student - 
Redirected to:
/dashboard
Instructor
Redirected to:
/upload

Module 4: Student Dashboard
Features
•	View Uploaded Materials 
•	Material Information 
•	Download Resources 
Data Source
AWS RDS

Module 5: Instructor Upload Portal
Features
•	Upload Course Material 
•	Upload Images 
•	Upload PDFs 
•	Material Title Entry 
Workflow
Select File
      ↓
Upload to S3
      ↓
Generate URL
      ↓
Save Metadata in RDS
      ↓
Display to Students

    id INT AUTO_INCREMENT PRIMARY KEY,
    title VARCHAR(255),
    file_url TEXT,
    uploaded_by VARCHAR(100),
    upload_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
Purpose
Stores:
•	Material Title 
•	S3 URL 
•	Instructor Name 
•	Upload Timestamp

10. Security Features -
•	Password Hashing 
•	IAM Role Based Access 
•	Secure S3 Storage 
•	RDS Security Groups 
•	Nginx Reverse Proxy 
•	User Role Management


11. Advantages -
•	Cloud Hosted 
•	Scalable 
•	Low Cost 
•	Centralized Learning Resources 
•	Easy Content Management 
•	High Availability 


12. Future Enhancements -
•	Video Lectures 
•	Live Classroom Integration 
•	Student Progress Tracking 
•	Assignment Submission 
•	Attendance Monitoring 
•	Email Notifications 
•	Mobile Application

12. Project Outcome -
The AWS Hosted Virtual Classroom successfully demonstrates the integration of AWS cloud services with modern web technologies.
The system enables instructors to upload educational content while allowing students to securely access and download learning resources through a cloud-based platform.



13. Conclusion -
The project successfully implements a complete Virtual Classroom solution using AWS Cloud services. AWS EC2 hosts the application, AWS RDS manages user and material data, and AWS S3 stores educational resources. The platform provides a secure, scalable, and efficient environment for online learning and demonstrates practical implementation of cloud computing concepts in education.









