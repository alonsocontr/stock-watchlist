import stock_details
import sqlite3

# Function to connect to the SQLite database
def get_db_connection():
    conn = sqlite3.connect('stock_watchlist.db')
    conn.row_factory = sqlite3.Row  # Allows accessing columns by name
    return conn

# Stock watchlist that can add/remove stocks from the database
class StockWatchlist():
    def __init__(self):
        self.stock_list = []

        # Initialize stock watchlist from database
        self.load_watchlist_from_db()

    # Load the watchlist from the database
    def load_watchlist_from_db(self):
        conn = get_db_connection()
        cursor = conn.cursor()

        cursor.execute('SELECT ticker FROM stocks')  # Fetch only the ticker column
        rows = cursor.fetchall()

        for row in rows:
            self.stock_list.append(row['ticker'])

        conn.close()

    # Add stock to the watchlist and save to database
    def add_stock(self, stock_symbol):
        stock_symbol = stock_symbol.upper()
        if stock_symbol not in self.stock_list:
            stock_info = stock_details.get_stock_info(stock_symbol)
            print("Stock Info Retrieved:", stock_info)  # Debug: Display retrieved stock info
            if stock_info:
                self.stock_list.append(stock_symbol)

                # Save to database
                conn = get_db_connection()
                cursor = conn.cursor()
                try:
                    print(f"Inserting {stock_symbol} into database...")  # Debug
                    cursor.execute('''
                        INSERT INTO stocks (ticker) VALUES (?)
                    ''', (stock_symbol,))
                    conn.commit()
                    print(f"{stock_symbol} added to database.")  # Debug
                except sqlite3.Error as e:
                    print(f"SQLite Error during insertion: {e}")
                finally:
                    conn.close()
            else:
                print(f"Failed to retrieve data for {stock_symbol}")
        else:
            print("This stock is already in your watchlist.")

    # Remove stock from the watchlist and delete from database
    def remove_stock(self, stock_symbol):
        stock_symbol = stock_symbol.upper()
        if stock_symbol in self.stock_list:
            self.stock_list.remove(stock_symbol)

            # Delete from database
            conn = get_db_connection()
            cursor = conn.cursor()
            try:
                print(f"Removing {stock_symbol} from database...")  # Debug
                cursor.execute('''
                    DELETE FROM stocks WHERE ticker = ?
                ''', (stock_symbol,))
                conn.commit()
                print(f"{stock_symbol} removed from database.")  # Debug
            except sqlite3.Error as e:
                print(f"SQLite Error during deletion: {e}")
            finally:
                conn.close()
        else:
            print("This stock is not in your watchlist.")
