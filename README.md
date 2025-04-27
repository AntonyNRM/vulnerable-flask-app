# Vulnerable Flask App - Security Vulnerability Assessment Demo

---

## Overview

This project demonstrates a deliberately vulnerable Flask-based web application, developed for educational and security assessment purposes. It simulates real-world coding mistakes that commonly lead to exploitation in production systems, including critical vulnerabilities identified in the OWASP Top 10 2021 list.

**Disclaimer**:  
This application is intentionally insecure.  
**Do not deploy it on any production environment or expose it to the Internet.**  
Use strictly within controlled, local testing environments.

---

## Purpose of This Application

- Showcase how typical security vulnerabilities arise during application development.
- Provide practical examples for security training and penetration testing practice.
- Help in understanding the impact of insecure coding patterns across web, API, and cloud integrations.

---

## Vulnerabilities Demonstrated

| Endpoint | Vulnerability | Description |
|:---------|:--------------|:------------|
| `/login` (POST) | **Broken Access Control** and **Cryptographic Failures** | Login function does not enforce role-based access and handles passwords insecurely without hashing. |
| `/query` (GET) | **SQL Injection** | Direct usage of user input in SQL queries without sanitization enables injection attacks. |
| `/ping` (GET) | **Command Injection** | User input is directly passed to OS commands without validation, allowing arbitrary command execution. |
| `/upload` (POST) | **Security Misconfiguration + Hardcoded Secrets** | AWS credentials are hardcoded, and files are "uploaded" to a simulated public bucket without secure configuration. |

---

## Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/AntonyNRM/vulnerable-flask-app.git
cd vulnerable-flask-app
