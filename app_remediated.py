from flask import Flask, request, jsonify, abort
import os
import sqlite3
import bcrypt
import json

app = Flask(__name__)

# -------------------- Secure Config --------------------

# Environment-based secrets (e.g., for AWS)
AWS_ACCESS_KEY = os.environ.get("AWS_ACCESS_KEY", "REDACTED")
AWS_SECRET_KEY = os.environ.get("AWS_SECRET_KEY", "REDACTED")
BUCKET_NAME = os.environ.get("BUCKET_NAME", "REDACTED")

# Secure SQLite database setup
def init_db():
    conn = sqlite3.connect(':memory:', check_same_thread=False)
    cursor = conn.cursor()
    cursor.execute("CREATE TABLE users (username TEXT, password TEXT, role TEXT)")
    
    # Securely hashed passwords using bcrypt
    admin_pass = bcrypt.hashpw(b"admin123", bcrypt.gensalt()).decode('utf-8')
    user_pass = bcrypt.hashpw(b"user123", bcrypt.gensalt()).decode('utf-8')

    cursor.execute("INSERT INTO users VALUES ('admin', ?, 'admin')", (admin_pass,))
    cursor.execute("INSERT INTO users VALUES ('user1', ?, 'user')", (user_pass,))
    conn.commit()
    return conn

db_conn = init_db()

# -------------------- Secure Endpoints --------------------

@app.route('/login', methods=['POST'])
def login():
    username = request.form.get('username')
    password = request.form.get('password')

    cursor = db_conn.cursor()
    cursor.execute("SELECT password, role FROM users WHERE username = ?", (username,))
    user = cursor.fetchone()

    if user and bcrypt.checkpw(password.encode('utf-8'), user[0].encode('utf-8')):
        # RBAC: only show user role, not full user list
        return jsonify({"message": f"Welcome {username}. Role: {user[1]}"})
    else:
        return jsonify({"message": "Invalid credentials"}), 401

@app.route('/query', methods=['GET'])
def query():
    username = request.args.get('username')
    cursor = db_conn.cursor()
    cursor.execute("SELECT username, role FROM users WHERE username = ?", (username,))
    result = cursor.fetchall()
    return jsonify({"result": result})

@app.route('/ping', methods=['GET'])
def ping():
    target = request.args.get('target')
    if not target or not target.replace(".", "").isalnum():
        return jsonify({"error": "Invalid target"}), 400
    # Emulate a safe ping response (no real os.system call)
    return jsonify({"message": f"Simulated ping to {target}"}), 200

@app.route('/upload', methods=['POST'])
def upload():
    filename = request.form.get('filename')
    if not filename or not filename.endswith(".txt"):
        return jsonify({"error": "Invalid filename"}), 400
    # Secure simulation - No real upload
    return jsonify({"message": f"Secure upload simulated for {filename}"}), 200

@app.route('/deserialize', methods=['POST'])
def deserialize():
    try:
        # Accept only JSON, reject binary/pickle for security
        data = json.loads(request.form.get("payload"))
        return jsonify({"message": f"Parsed object: {data}"})
    except Exception as e:
        return jsonify({"error": str(e)}), 400

@app.route('/allocate', methods=['POST'])
def allocate():
    obj_id = request.form.get('id')
    if not obj_id:
        return abort(400)
    objects[obj_id] = {"data": "Valid Object"}
    return jsonify({"message": f"Object {obj_id} allocated."})

@app.route('/free', methods=['POST'])
def free():
    obj_id = request.form.get('id')
    if obj_id in objects:
        objects.pop(obj_id)
        return jsonify({"message": f"Object {obj_id} freed."})
    return jsonify({"message": "Object not found."}), 404

@app.route('/use', methods=['GET'])
def use():
    obj_id = request.args.get('id')
    obj = objects.get(obj_id)
    if obj:
        return jsonify({"data": obj['data']})
    return jsonify({"error": "Object not available"}), 400

objects = {}

if __name__ == '__main__':
    app.run(debug=False)
