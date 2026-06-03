import sqlite3

def get_connection():
    conn = sqlite3.connect("students.db")
    return conn

def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER,
        course TEXT
    )
    """)

    conn.commit()
    conn.close()