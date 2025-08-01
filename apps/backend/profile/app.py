from flask import Flask, request, jsonify, Blueprint
import psycopg2
import os
import jwt
from flask_cors import CORS

app = Flask(__name__)
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

profile_bp = Blueprint("profile", __name__)

@profile_bp.get("/")  # handles GET /profile
def profile_root():
    return jsonify({"ok": True, "service": "profile"}), 200

@profile_bp.get("/health")
def health():
    return jsonify({"status": "ok"}), 200

@profile_bp.get("")  # optional: also handle /profile (no trailing slash cases)
def profile_empty():
    return jsonify({"ok": True, "service": "profile"}), 200

@profile_bp.get("/profile")  # handles GET /profile/profile
def profile():
    token = request.headers.get("Authorization")
    if not token:
        return jsonify({"error": "Token required"}), 401
    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=["HS256"])
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

# Mount all profile routes at /profile
app.register_blueprint(profile_bp, url_prefix="/profile")

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5002)
