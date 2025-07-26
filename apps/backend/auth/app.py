from flask import Flask, request, jsonify
import pymysql
import os
import jwt
import datetime
import os



app = Flask(__name__)

app.config['SECRET_KEY'] = os.getenv("SECRET_KEY", "fallback-secret")



# RDS connection details from environment variables
DB_HOST = os.environ.get('DB_HOST')
DB_USER = os.environ.get('DB_USER')
DB_PASS = os.environ.get('DB_PASSWORD')
DB_NAME = "auth_db"

def get_db_connection():
    return pymysql.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASS,
        database=DB_NAME,
        cursorclass=pymysql.cursors.DictCursor
    )

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    username = data.get("username")
    password = data.get("password")
    
    conn = None  # Initialize here to avoid UnboundLocalError
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
        conn.commit()
        return jsonify({"message": f"User {username} created"}), 201
    except pymysql.err.IntegrityError:
        return jsonify({"message": "User already exists"}), 400
    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()



@app.route('/login', methods=['POST'])
def login():
    data = request.json
    username = data.get("username")
    password = data.get("password")

    conn = None
    try:
        conn = get_db_connection()
        with conn.cursor() as cursor:
            cursor.execute(
                "SELECT username, email, role FROM users WHERE username = %s AND password = %s",
                (username, password)
            )
            user = cursor.fetchone()

        if user:
            payload = {
                'username': user['username'],
                'email': user['email'],
                'role': user['role'],
                'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=1)
            }
            token = jwt.encode(payload, app.config['SECRET_KEY'], algorithm='HS256')
            return jsonify({"token": token}), 200
        else:
            return jsonify({"message": "Invalid credentials"}), 401

    except Exception as e:
        return jsonify({"error": str(e)}), 500
    finally:
        if conn:
            conn.close()


@app.route('/verify', methods=['GET'])
def verify():
    token = request.headers.get('Authorization')
    try:
        decoded = jwt.decode(token, app.config['SECRET_KEY'], algorithms=['HS256'])
        return jsonify({"user": decoded["username"]}), 200
    except jwt.ExpiredSignatureError:
        return jsonify({"error": "Token expired"}), 401
    except jwt.InvalidTokenError:
        return jsonify({"error": "Invalid token"}), 403



@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "ok"}), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5001)
