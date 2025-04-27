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
⚙️ Setup Instructions
1. Clone the Repository
'''bash
Copy
Edit
git clone https://github.com/AntonyNRM/vulnerable-flask-app.git
cd vulnerable-flask-app
2. Install Dependencies
Install the required Python packages:

'''bash
Copy
Edit
pip install -r requirements.txt
## Requirements:

Python 3.x

Flask

boto3

## Running the Application
Start the Flask application with:

'''bash
Copy
Edit
python app.py
The server will be available at:

'''bash
Copy
Edit
http://127.0.0.1:5000/
## Note: Debug mode is intentionally enabled to make vulnerabilities easier to observe.

## Interacting with the Vulnerabilities
1. /login (POST)
How to Test:
Create a simple HTML login form OR

Use Postman.

Send a POST request to:

'''bash
Copy
Edit
http://127.0.0.1:5000/login
With form fields:


Field	Value
username	admin
password	adminpass
Observation:
## If login is successful, the app exposes all user data including usernames and roles —
without checking user authorization properly.

2. /query (GET)
How to Test:
Open this URL in the browser:

'''bash
Copy
Edit
http://127.0.0.1:5000/query?username=admin
Injection Example:
Inject SQL manipulation by visiting:

'''bash
Copy
Edit
http://127.0.0.1:5000/query?username=admin' OR '1'='1
Observation:
## SQL Injection succeeds:
You retrieve all user records bypassing normal authentication checks.

3. /ping (GET)
How to Test:
Send a simple ping request:

'''bash
Copy
Edit
http://127.0.0.1:5000/ping?target=google.com
Injection Example:
Inject an OS command using:

'''bash
Copy
Edit
http://127.0.0.1:5000/ping?target=127.0.0.1;ls
Observation:
## You can inject commands like ls, cat, rm,
leading to potential Remote Code Execution (RCE) on the server.

4. /upload (POST)
How to Test:
Send a POST request (via Postman or HTML form) to:

'''bash
Copy
Edit
http://127.0.0.1:5000/upload
Form fields:


Field	Value
filename	sample.txt
Observation:
## Simulated upload occurs using hardcoded AWS credentials.
In real-world, this could expose cloud data and compromise the cloud environment.

## Learning Outcomes
By exploring this application, you will learn:

How critical vulnerabilities appear in typical development scenarios.

Why role-based access control, input sanitization, and cryptographic practices are necessary.

How cloud misconfigurations (e.g., hardcoded API keys) pose serious threats.
