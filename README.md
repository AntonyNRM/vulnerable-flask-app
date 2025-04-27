# Vulnerable Flask App - Security Vulnerability Assessment Demo

---

## Overview

This project demonstrates a deliberately vulnerable Flask-based web application.  
It simulates real-world coding mistakes that commonly lead to exploitation, covering critical OWASP Top 10 vulnerabilities and cloud misconfigurations.

**Disclaimer:**  
This application is intentionally insecure.  
**Do not deploy it in any production environment or expose it to the internet.**

---

## Purpose

- Demonstrate how common coding mistakes create vulnerabilities.
- Provide practical examples for penetration testing and security training.
- Help developers and security engineers understand secure coding practices.

---

## Vulnerabilities Demonstrated

| Endpoint | Vulnerability | Description |
|:---------|:--------------|:------------|
| `/login` (POST) | Broken Access Control & Cryptographic Failures | No role enforcement and plaintext password handling. |
| `/query` (GET) | SQL Injection | Direct user input inside SQL queries without sanitisation. |
| `/ping` (GET) | Command Injection | Executes OS commands based on unsanitized user input. |
| `/upload` (POST) | Cloud Misconfiguration & Hardcoded API Keys | AWS credentials hardcoded; public "upload" simulation. |

---

## 1. Clone the Repository

Clone the vulnerable Flask app repository to your local machine:

```bash

git clone https://github.com/yourusername/vulnerable-flask-app.git
cd vulnerable-flask-app
```

## 2. Install the Required Dependencies

```bash

pip install -r requirements.txt 
```
✅ Requirements:
Python 3.x
Flask
boto3

## 3. Run the Application

```bash

python app.py
```
✅ The server will start at:
```bash

http://127.0.0.1:5000/
```
✅ Note: Debug mode is ON intentionally to make vulnerabilities easier to observe.

# Step-by-Step Testing Instructions

## 1. /login (POST) — Broken Access Control
How to Test:
Send a POST request to:

```html

http://127.0.0.1:5000/login
```
With form-data fields:

Field	Value
username	admin
password	adminpass

Observation:
✅ Exposes all users' data including usernames and roles — without proper authorization.

## 2. /query (GET) — SQL Injection
How to Test:
Visit:

```html

http://127.0.0.1:5000/query?username=admin

```
Injection Example:

```html

http://127.0.0.1:5000/query?username=admin' OR '1'='1
```
Observation:n.
✅ Retrieves all user records, bypassing authentication — demonstrating SQL Injection.

## 3. /ping (GET) — Command Injection
How to Test:
Simple ping:

```html

http://127.0.0.1:5000/ping?target=google.com
```

Injection Example:

```html

http://127.0.0.1:5000/ping?target=127.0.0.1;ls
```

Observation:
✅ Executes arbitrary OS commands — leading to potential RCE.

## 4. /upload (POST) — Cloud Misconfiguration
How to Test:
Send a POST request to:

```html

http://127.0.0.1:5000/upload
```

With form field:
Field | Value
filename | sample.txt

Expected Observation:
- Simulated upload with hardcoded AWS credentials.
- Shows a cloud misconfiguration and hardcoded secret vulnerability.
