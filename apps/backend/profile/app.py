from flask import Flask, request, jsonify
import psycopg2
import os
import jwt
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
# open to any origin—adjust as needed for production
CORS(app, resources={r"/*": {"origins": "*"}})

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret")

# PostgreSQL DB connection from environment variables
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASSWORD')
DB_NAME = "profile_db"

def get_db_connection():
    return psycopg2.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        dbname=DB_NAME
    )

@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

@app.route('/profile', methods=['GET'])
def profile():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token required"}), 401

    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
        # Build a richer profile object:
        return jsonify({
            "username": decoded.get("username"),
            "email":    decoded.get("email"),
            "role":     decoded.get("role"),
            "bio":      f"Hello, {decoded.get('username')}! This is your profile."
        }), 200

    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 403


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
