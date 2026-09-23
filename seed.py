"""
Seed script for CyberHelp database.
Executes schema creation and seeds realistic data for all modules.
"""
from db import seed_db

if __name__ == '__main__':
    print("Executing CyberHelp database initialization and seeding...")
    seed_db()
    print("Database seeding completed.")
