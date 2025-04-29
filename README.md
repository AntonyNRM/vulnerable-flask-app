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

| # | Vulnerability | Endpoint |
|---|---------------|----------|
| 1 | Broken Access Control + Cryptographic Failure | `/login` |
| 2 | SQL Injection | `/query` |
| 3 | OS Command Injection | `/ping` |
| 4 | Cloud Misconfiguration | `/upload` |
| 5 | Insecure Deserialization (from last improvement) | `/deserialize` |
| 6 | Simulated **Use-After-Free** (CVE-2025-29824) | `/allocate`, `/free`, `/use` |

---
## Setup Instructions

### 1. Clone the Repository

Clone the vulnerable Flask app repository to your local machine:

```bash

git clone https://github.com/AntonyNRM/vulnerable-flask-app.git
```
```bash

cd vulnerable-flask-app
```

### 2. Install the Required Dependencies

```bash

pip install -r requirements.txt 
```
Requirements:

Python 3.x

Flask

boto3

### 3. Run the Application

```bash

python app.py
```
The server will start at:
```bash

http://127.0.0.1:5000/
```

## Step-by-Step Testing Instructions

### 1. /login (POST) — Broken Access Control
Send a POST request to:

```http

http://127.0.0.1:5000/login
```
Form Data:

Field	Value
| Field    | Value      |
|----------|------------|
| username | admin      |
| password | admin123   |

Observation:
- Exposes all users' data including usernames and roles — without proper authorization.

## 2. /query (GET) — SQL Injection
Send request:

```http

http://127.0.0.1:5000/query?username=admin

```
Injection Example:

```http

http://127.0.0.1:5000/query?username=admin' OR '1'='1
```
Observation:
- Retrieves all user records, bypassing authentication — demonstrating SQL Injection.

### 3. /ping (GET) — Command Injection
Send request:

```http

http://127.0.0.1:5000/ping?target=google.com
```

Injection Example:

```http

http://127.0.0.1:5000/ping?target=127.0.0.1;ls
```

Observation:
- Executes arbitrary OS commands — leading to potential Remote Code Execution (RCE).

### 4. /upload (POST) — Cloud Misconfiguration
Send POST request to:

```http

http://127.0.0.1:5000/upload
```
Form Data:

| Field    | Value        |
|----------|--------------|
| filename | sample.txt   |

Observation:
- Simulated upload using hardcoded AWS credentials — showing cloud misconfiguration.

### 5. /deserialize - Insecure Deserialization
Python script to test:

```python

# Save this script as test_deserialize.py
import requests
import pickle

payload = pickle.dumps({"exploit": "deserialized!"})
response = requests.post("http://127.0.0.1:5000/deserialize", data=payload)
print(response.text)
```
Observation:
- Untrusted data is deserialized without validation — leading to potential code execution.

### 6. /allocate, /free, /use - Use-After-Free Simulation (CVE-2025-29824)
Step 1: Allocate Object

```bash

curl -X POST -d "id=123" http://127.0.0.1:5000/allocate
```
Step 2: Free the Object

```bash

curl -X POST -d "id=123" http://127.0.0.1:5000/free
```
Step 3: Use the Freed Object (Triggers Error)

```bash

curl "http://127.0.0.1:5000/use?id=123"
```
Observation:
- Attempts to access a freed object — simulating a Use-After-Free vulnerability.
