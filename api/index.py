from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "active", "message": "API is running!"})

@app.route('/lookup')
def lookup():
    username = request.args.get('username')
    if not username:
        return jsonify({"error": "Username do"}), 400
    return jsonify({"status": "success", "username": username, "number": "21211111XX"})

app = app
