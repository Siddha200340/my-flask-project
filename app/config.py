import os
import sqlite3

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "app.db")

# Flask secret (falls back to a dev key if not set in the environment)
SECRET_KEY = os.environ.get("FLASK_SECRET", "dev-secret-key")

def get_db():
    """
    Return a sqlite3 connection with row access by name.
    Caller is responsible for closing the connection.
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """
    Create the users table if it doesn't exist.
    Safe to call multiple times.
    """
    conn = get_db()
    try:
        c = conn.cursor()
        c.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT UNIQUE NOT NULL,
                password_hash TEXT NOT NULL
            );
        """)
        conn.commit()
    finally:
        conn.close()
