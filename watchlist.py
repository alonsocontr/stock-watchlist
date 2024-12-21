import stock_details


# Stock watchlist that can add/remove stocks from list
class StockWatchlist():
    def __init__(self):
        self.stock_list = []
        self.stock_data = {}

    # Add stock to list
    def add_stock(self, stock_symbol):
        stock_symbol = stock_symbol.upper()
        if stock_symbol not in self.stock_list:
            stock_info = stock_details.get_stock_info(stock_symbol)
            if stock_info:
                self.stock_list.append(stock_symbol)
                self.stock_data[stock_symbol] = stock_info
                print(f"{stock_symbol} added to watchlist.")
            else:
                print(f"Failed to retrieve data for {stock_symbol}")
        else:
           print("This stock is already in your watchlist.")

    # Remove stock from list

    def remove_stock(self, stock_symbol):
        stock_symbol = stock_symbol.upper()
        if stock_symbol in self.stock_list:
           self.stock_list.remove(stock_symbol)
           del self.stock_data[stock_symbol]
           print(f"{stock_symbol} removed from watchlist.")
        else:
            print("This stock is not in your watchlist.")


