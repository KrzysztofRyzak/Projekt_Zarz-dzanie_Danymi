import sqlite3

def setup_database():
    conn = sqlite3.connect('car_dealership.db')
    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS cars (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            brand TEXT NOT NULL,
            year INTEGER NOT NULL,
            type TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

if __name__ == '__main__':
    setup_database()
