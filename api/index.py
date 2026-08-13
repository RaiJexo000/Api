from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "active",
        "message": "SnapChat API is running!",
        "endpoints": {
            "/lookup": "?username=xyz&api_key=your_key"
        }
    })

@app.route('/lookup')
def lookup():
    username = request.args.get('username')
    api_key = request.args.get('api_key')
    
    if not username:
        return jsonify({"error": "Username do"}), 400
    
    # Dummy response (database ki jagah)
    return jsonify({
        "status": "success",
        "username": username,
        "number": "21211111XX",
        "source": "@ApiMarket1_bot",
        "powered_by": "RJ Studio"
    })

app = app
