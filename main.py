# Create stock market watchlist that tracks the price of stock(s)
# 1. Implement a reliable API that will update stock price continuously
# 2. Create a dashboard or GUI using PYQt5 where users can add/remove a stock
#    from their watchlist
#       - Users add stock by searching for a ticker
#       - Users remove stock by selecting the stock in their watchlist
#         then press remove button
# 3. Add a stock details button that adds details about a stock on a
#    user's watchlist. This includes graphs, historical data, public sentiment
#    and analyst ratings/average stock forecasts. Need more APIs here...
# 4. Add user authentication.
# 5. Add a notifications system either through email or SMS
import stock_details
from watchlist import StockWatchlist
import interface


def main():
    # Initialize watchlist
    watchlist = StockWatchlist()
    watchlist.add_stock("NVDA")
    interface.main()

main()
