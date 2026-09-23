import os
import sqlite3
from werkzeug.security import generate_password_hash

# Database path can be overridden via environment variable (e.g., for tests)
DATABASE_PATH = os.environ.get('DATABASE_PATH') or os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cyberhelp.db')
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schema.sql')
SEED_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seed.sql')

# Admin credentials from environment
ADMIN_USERNAME = os.environ.get('ADMIN_USERNAME', 'admin')
ADMIN_PASSWORD = os.environ.get('ADMIN_PASSWORD')

def get_db():
    """
    Returns a database connection configured with Row factory
    and enabled foreign keys.
    """
    conn = sqlite3.connect(DATABASE_PATH)
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn

def init_db():
    """
    Initializes the database tables from schema.sql.
    """
    conn = get_db()
    with open(SCHEMA_PATH, 'r', encoding='utf-8') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()
    print("Database tables created successfully from schema.sql.")

def seed_db():
    """
    Seeds the database with default admin user and initial sample data
    for awareness articles, scams, quiz questions, FAQs, and reporting guidance.
    """
    init_db()
    conn = get_db()
    cursor = conn.cursor()

    # Check if admin exists; if not, create admin with password from environment
    cursor.execute("SELECT admin_id FROM admin WHERE username = ?", (ADMIN_USERNAME,))
    admin_row = cursor.fetchone()
    if not admin_row:
        if not ADMIN_PASSWORD:
            raise RuntimeError("ADMIN_PASSWORD is not configured. Set ADMIN_PASSWORD in .env")
        admin_hash = generate_password_hash(ADMIN_PASSWORD)
        cursor.execute(
            "INSERT INTO admin (username, password_hash) VALUES (?, ?)",
            (ADMIN_USERNAME, admin_hash)
        )
        conn.commit()
        print(f"Default admin account created (Username: {ADMIN_USERNAME}).")
    else:
        # Ensure admin password hash is valid for current werkzeug version
        if ADMIN_PASSWORD:
            cursor.execute("UPDATE admin SET password_hash = ? WHERE username = ?", (generate_password_hash(ADMIN_PASSWORD), ADMIN_USERNAME))
            conn.commit()

    # Read and run seed.sql to populate initial sample records if tables are empty
    # Only run seed.sql for default admin (production); tests use their own admin and data
    if ADMIN_USERNAME == 'admin':
        cursor.execute("SELECT COUNT(*) as count FROM awareness_content")
        if cursor.fetchone()['count'] == 0:
            with open(SEED_PATH, 'r', encoding='utf-8') as f:
                conn.executescript(f.read())

            # Update admin password hash in seed data to match current env
            if ADMIN_PASSWORD:
                cursor.execute("UPDATE admin SET password_hash = ? WHERE username = ?", (generate_password_hash(ADMIN_PASSWORD), ADMIN_USERNAME))
                conn.commit()
            print("Sample seed data loaded successfully from seed.sql.")
    else:
        print("Test mode: skipping seed.sql (using test admin).")

    conn.close()

if __name__ == '__main__':
    print("Initializing and seeding CyberHelp SQLite Database...")
    seed_db()
    print("Ready to run CyberHelp application!")
