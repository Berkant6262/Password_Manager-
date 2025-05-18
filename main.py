import sqlite3
import hashlib
import cryptography

#Erstellung der Datenbank
def create_db():
    _db = sqlite3.connect("Passwörter.db")
    _cursor = _db.cursor()
    _cursor.execute("""
        CREATE TABLE IF NOT EXISTS Passwoerter (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            Site TEXT NOT NULL,
            Login TEXT,
            Passwort TEXT
        )
    """)
    _db.commit()
    return _db

if __name__ == "__main__":
    _db = create_db()
