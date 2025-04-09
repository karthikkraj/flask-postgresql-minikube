from flask import Flask, jsonify
import psycopg2
import os

app = Flask(__name__)

# Load DB config from environment variables
DB_HOST = os.environ.get("DB_HOST", "localhost")
DB_NAME = os.environ.get("DB_NAME", "mydatabase")
DB_USER = os.environ.get("DB_USER", "postgres")
DB_PASSWORD = os.environ.get("DB_PASSWORD", "postgres")
DB_PORT = os.environ.get("DB_PORT", "5432")

# Home route
@app.route("/")
def home():
    return "👋 Hello, KarthikRaj(BCD41)! Flask app is running."

# Example route to fetch students
@app.route("/students", methods=["GET"])
def get_students():
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT
        )
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM students;")
        rows = cursor.fetchall()
        students = [{"id": row[0], "name": row[1]} for row in rows]
        cursor.close()
        conn.close()
        return jsonify(students)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True, use_reloader=False)
