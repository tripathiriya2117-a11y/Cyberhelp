import os
import sqlite3
from werkzeug.security import generate_password_hash

DATABASE_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'cyberhelp.db')
SCHEMA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'schema.sql')
SEED_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'seed.sql')

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

    # Check if admin exists; if not, create default admin with standard password hash
    cursor.execute("SELECT admin_id FROM admin WHERE username = ?", ('admin',))
    admin_row = cursor.fetchone()
    if not admin_row:
        admin_hash = generate_password_hash('admin123')
        cursor.execute(
            "INSERT INTO admin (username, password_hash) VALUES (?, ?)",
            ('admin', admin_hash)
        )
        conn.commit()
        print("Default admin account created (Username: admin, Password: admin123).")

    # Read and run seed.sql to populate initial sample records if tables are empty
    cursor.execute("SELECT COUNT(*) as count FROM awareness_content")
    if cursor.fetchone()['count'] == 0:
        with open(SEED_PATH, 'r', encoding='utf-8') as f:
            conn.executescript(f.read())
        
        # Ensure admin password hash in database is valid for current werkzeug version
        cursor.execute("UPDATE admin SET password_hash = ? WHERE username = ?", (generate_password_hash('admin123'), 'admin'))
        conn.commit()
        print("Sample seed data loaded successfully from seed.sql.")
    else:
        print("Seed data already present; skipping seed script.")

    conn.close()

if __name__ == '__main__':
    print("Initializing and seeding CyberHelp SQLite Database...")
    seed_db()
    print("Ready to run CyberHelp application!")
