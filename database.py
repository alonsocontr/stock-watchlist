import sqlite3

# Function to create the stock table if it doesn't exist
def create_table():
    conn = sqlite3.connect('stock_watchlist.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stocks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            ticker TEXT NOT NULL
        )
    ''')

    conn.commit()
    conn.close()
