Vulnerable Flask App - Security Vulnerability Assessment Demo
## Overview
This project demonstrates a deliberately vulnerable Flask-based web application.
It simulates real-world coding mistakes that commonly lead to exploitation, covering critical OWASP Top 10 vulnerabilities and cloud misconfigurations.

## Disclaimer:
This application is intentionally insecure.
Do not deploy it in any production environment or public network.

## Purpose
Demonstrate how common coding mistakes create vulnerabilities.

Provide practical examples for penetration testing practice.

Teach developers and security engineers how to identify and fix insecure code.

## Vulnerabilities Demonstrated

Endpoint	Vulnerability	Description
/login (POST)	Broken Access Control and Cryptographic Failures	No role enforcement and plaintext password handling.
/query (GET)	SQL Injection	Direct user input inside SQL queries.
/ping (GET)	Command Injection	Executes OS commands based on unsanitized user input.
/upload (POST)	Cloud Misconfiguration + Hardcoded API Keys	AWS credentials hardcoded; public "upload" simulation.

🔥 Setup and Running Guide
1. Clone the Repository
Clone the vulnerable Flask app repository to your local machine:

bash
Copy
Edit
git clone https://github.com/yourusername/vulnerable-flask-app.git
cd vulnerable-flask-app
2. Install the Required Dependencies
Install Python packages needed to run the app:

bash
Copy
Edit
pip install -r requirements.txt
✅ Requirements:

Python 3.x

Flask

boto3

3. Run the Application
Start the Flask application:

bash
Copy
Edit
python app.py
The app will start running at:

http
Copy
Edit
http://127.0.0.1:5000/
✅ Debug mode is ON intentionally to expose vulnerabilities.

🛠️ Step-by-Step Testing Instructions
1. Login Endpoint (/login)
How to Test:

Open Postman or use a simple HTML form.

Send a POST request to:

http
Copy
Edit
http://127.0.0.1:5000/login
With form data:


Field	Value
username	admin
password	adminpass
Expected Observation:

You should see a list of all users and their roles — without any access control.

This shows Broken Access Control and Cryptographic Failures (plain text password matching).

2. Query Endpoint (/query)
How to Test:

Open in browser:

http
Copy
Edit
http://127.0.0.1:5000/query?username=admin
To test SQL Injection, open:

http
Copy
Edit
http://127.0.0.1:5000/query?username=admin' OR '1'='1
Expected Observation:

Bypasses authentication and returns all user data.

Classic SQL Injection vulnerability.

3. Ping Endpoint (/ping)
How to Test:

Open browser:

http
Copy
Edit
http://127.0.0.1:5000/ping?target=google.com
To test Command Injection:

http
Copy
Edit
http://127.0.0.1:5000/ping?target=127.0.0.1;ls
Expected Observation:

Server executes arbitrary OS commands.

Severe Command Injection vulnerability.

4. Upload Endpoint (/upload)
How to Test:

Send a POST request via Postman to:

http
Copy
Edit
http://127.0.0.1:5000/upload
With form-data field:


Field	Value
filename	sample.txt
