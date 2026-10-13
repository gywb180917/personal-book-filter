import json
import sqlite3
from pathlib import Path

DB_PATH = Path("data/books.db")
JSON_PATH = Path("data/books.json")

def INIT_DB():
    DB_PATH.parent.mkdir(parents=True,exist_ok=True)
    books = json.loads(JSON_PATH.read_text(encoding="utf-8"))
    conn = sqlite3.connect(DB_PATH)
    try:
        conn.execute("PRAGMA foreign_keys = ON")
        conn.executescript("""
        CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY,
        title TEXT NOT NULL,
        genre TEXT NOT NULL
        );
        CREATE TABLE IF NOT EXISTS favorites (
        id INTEGER PRIMARY KEY,
        user_name TEXT NOT NULL,
        book_id INTEGER NOT NULL,
        FOREIGN KEY (book_id) REFERENCES books(id)
        );
         """)
        conn.executemany(
        "INSERT OR IGNORE INTO books (id, title, genre) VALUES (?, ?, ?)",
        [(b["id"], b["title"], b["genre"]) for b in books],
        )
        conn.commit()
    finally:
        conn.close()
if __name__ == "__main__":
    INIT_DB()
    print(f"Database created: {DB_PATH}")
