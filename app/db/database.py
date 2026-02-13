import sqlite3
from pathlib import Path

base_dir = Path(__file__).resolve().parent
db_path = base_dir / "database.sqlite3"

def get_connection():
    conn = sqlite3.connect(db_path)
    conn.row_factory = sqlite3.Row
    return conn

def criar_tabela():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
                   CREATE TABLE IF NOT EXISTS pessoas (
                       id INTEGER PRIMARY KEY AUTOINCREMENT,
                       nome TEXT NOT NULL,
                       idade INTEGER NOT NULL,
                       email TEXT NOT NULL UNIQUE)
              """)
    conn.commit()
    conn.close()
    