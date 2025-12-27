import sqlite3

conn = sqlite3.connect("database.db")

conn.execute("""
CREATE TABLE opportunities (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    lead TEXT NOT NULL,
    description TEXT NOT NULL,
    roles TEXT NOT NULL,
    hours INTEGER NOT NULL
);
""")

conn.commit()
conn.close()

print("Database created")
