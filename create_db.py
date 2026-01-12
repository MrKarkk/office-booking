import sqlite3
import logging

logging.basicConfig(level=logging.INFO)

db = sqlite3.connect('office.db')
cursor = db.cursor()

logging.info("Creating database 'office.db'")

cursor.execute('''
CREATE TABLE IF NOT EXISTS rooms (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    number INTEGER UNIQUE NOT NULL CHECK (number BETWEEN 1 AND 5)
)
''')

cursor.execute('''
CREATE TABLE IF NOT EXISTS bookings (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    full_name TEXT NOT NULL,
    phone TEXT NOT NULL,
    start_time TEXT NOT NULL,
    end_time TEXT NOT NULL,
    room_number INTEGER NOT NULL,
    FOREIGN KEY (room_number) REFERENCES rooms (number)
)
''')

for num in range(1, 6):
    cursor.execute('INSERT OR IGNORE INTO rooms (number) VALUES (?)', (num,))

db.commit()
db.close()

logging.info("Database created successfully")