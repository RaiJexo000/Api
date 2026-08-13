from flask import Flask, request, jsonify
import os
import psycopg2

app = Flask(__name__)

# Database connection from environment variable
DATABASE_URL = os.environ.get("DATABASE_URL")

# Valid API keys
VALID_KEYS = ["rjstudio", "test_key_123"]

# ------------------- ROOT ROUTE (Home) -------------------
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

# ------------------- LOOKUP ROUTE -------------------
@app.route('/lookup')
def lookup():
    username = request.args.get('username')
    api_key = request.args.get('api_key')
    
    if not username:
        return jsonify({"error": "Username do (username=...)"}), 400
    
    if not api_key or api_key not in VALID_KEYS:
        return jsonify({"error": "Invalid or missing API key (api_key=...)"}), 401
    
    if not DATABASE_URL:
        return jsonify({"error": "DATABASE_URL not configured"}), 500
    
    try:
        conn = psycopg2.connect(DATABASE_URL)
        cur = conn.cursor()
        cur.execute("SELECT number FROM users WHERE username = %s", (username,))
        row = cur.fetchone()
        cur.close()
        conn.close()
        
        if row:
            return jsonify({
                "status": "success",
                "username": username,
                "number": row[0],
                "source": "@ApiMarket1_bot",
                "powered_by": "RJ Studio"
            })
        else:
            return jsonify({"error": "Username nahi mila"}), 404
    except Exception as e:
        return jsonify({"error": f"Database error: {str(e)}"}), 500

# This is required for Vercel
app = app

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
