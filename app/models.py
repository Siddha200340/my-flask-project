from werkzeug.security import generate_password_hash, check_password_hash
from .config import get_db

def create_user(username: str, password: str) -> bool:
    """
    Create a new user. Returns True on success, False if username exists.
    """
    pw_hash = generate_password_hash(password)
    conn = get_db()
    try:
        c = conn.cursor()
        c.execute("INSERT INTO users (username, password_hash) VALUES (?, ?)",
                  (username, pw_hash))
        conn.commit()
        return True
    except Exception:
        # On IntegrityError (duplicate username) or other error, return False
        return False
    finally:
        conn.close()

def get_user_by_username(username: str):
    """
    Return a row-like dict (sqlite3.Row) for the user, or None.
    Row fields: id, username, password_hash
    """
    conn = get_db()
    try:
        c = conn.cursor()
        c.execute("SELECT id, username, password_hash FROM users WHERE username = ?", (username,))
        row = c.fetchone()
        return row
    finally:
        conn.close()

def verify_user(username: str, password: str) -> bool:
    """
    Return True if username exists and password matches.
    """
    row = get_user_by_username(username)
    if not row:
        return False
    return check_password_hash(row["password_hash"], password)
