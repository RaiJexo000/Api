from flask import Flask, request, jsonify

app = Flask(__name__)

# Valid API keys (optional)
VALID_KEYS = ["rjstudio", "test_key_123"]

@app.route('/')
def home():
    return jsonify({
        "status": "active",
        "message": "SnapChat API is running!",
        "endpoints": {
            "/lookup": "?username=xyz&api_key=your_key"
        },
        "source": "@ApiMarket1_bot",
        "powered_by": "RJ Studio"
    })

@app.route('/lookup')
def lookup():
    # Get parameters
    username = request.args.get('username')
    api_key = request.args.get('api_key')
    
    # Check username
    if not username:
        return jsonify({"error": "Username do (username=...)"}), 400
    
    # Optional: API key check
    # if not api_key or api_key not in VALID_KEYS:
    #     return jsonify({"error": "Invalid or missing API key (api_key=...)"}), 401
    
    # For now, return dummy data
    return jsonify({
        "status": "success",
        "username": username,
        "number": "21211111XX",
        "source": "@ApiMarket1_bot",
        "powered_by": "RJ Studio"
    })

# Required for Vercel
app = app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
