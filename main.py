# Create stock market watchlist that tracks the price of stock(s)
# Goals:
# 1. Implement a reliable API that updates stock price continuously
# 2. Create a GUI using PYQt5 where users can add/remove a stock
#    from their watchlist
#       - Users add stock by searching for a ticker
#       - Users remove stock by typing the ticker in their watchlist
#         then press remove button
# 3. Add a stock details button that adds details about a stock on a
#    user's watchlist. This includes graphs, historical data, public sentiment
#    and analyst ratings/average stock forecasts. Need more APIs here...
# 4. Add a notifications system either through email or SMS

import interface # Import interface file
import database  # Import the database module

def main():
    # Create database table before running the application
    database.create_table()

    # Initialize the interface
    interface.main()

if __name__ == "__main__":
    main()


