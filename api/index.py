from flask import Flask, request, jsonify

app = Flask(__name__)
VALID_KEYS = ["rjstudio", "test_key_123"]

@app.route('/')
def home():
    return jsonify({"status": "active", "message": "API is running!"})

@app.route('/lookup')
def lookup():
    username = request.args.get('username')
    api_key = request.args.get('api_key')
    
    if not username:
        return jsonify({"error": "Username do"}), 400
    if not api_key or api_key not in VALID_KEYS:
        return jsonify({"error": "Invalid API key"}), 401
    
    # Dummy response (database ki jagah)
    return jsonify({
        "status": "success",
        "username": username,
        "number": "21211111XX",
        "source": "@ApiMarket1_bot",
        "powered_by": "RJ Studio"
    })

app = app
