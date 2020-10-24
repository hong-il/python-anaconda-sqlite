import sqlite3

conn = sqlite3.connect("test.db")
cur = conn.cursor()
query = """
    CREATE TABLE IF NOT EXISTS board (
        'idx' INTEGER PRIMARY KEY AUTOINCREMENT,
        'writer' VARCHAR(100),
        'title' VARCHAR(250),
        'content' TEXT
    )
"""
cur.execute(query)

query = "INSERT INTO board ('writer', 'title', 'content') VALUES ('hong-il', 'Invisible elephant', 'The Invisible elephant has defeated the Black dragon.')"
cur.execute(query)
query = "SELECT * FROM board"
cur.execute(query)

rows = cur.fetchall()
for row in rows:
    print(row)

conn.close()