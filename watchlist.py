import stock_details


# Stock watchlist that can add/remove stocks from list
class StockWatchlist():
    def __init__(self):
        self.stock_list = []

    # Add stock to list
    def add_stock(self, stock_symbol):
        if stock_symbol not in self.stock_list:
            stock_info = stock_details.get_stock_info(stock_symbol)
            self.stock_list.append(stock_symbol)
            print(f"{stock_symbol} added to watchlist.")
        else:
           print("This stock is already in your watchlist.")

    # Remove stock from list

    def remove_stock(self, stock_symbol):
        if stock_symbol in self.stock_list:
           self.stock_list.remove(stock_symbol)
           print(f"{stock_symbol} removed from watchlist.")
        else:
            print("This stock is not in your watchlist.")

    # Display watchlist
    def store_watchlist(self):
        if self.stock_list:
            stock_info_list = []
            for stock in stock_info_list:
                stock_info = stock_details.get_stock_info(stock)
                stock_name = f"- {stock_info[0]}"
                stock_price = f"Price: ${stock_info[1]:.2f}"
                stock_daily_volume = f"Daily volume: {stock_info[2]:,}"
                stock_pe_ratio = f"P/E Ratio: {stock_info[3]:.2f}"
                stock_market_cap = f"Market Cap: ${stock_info[4]:,}"
                stock_info_list.append((stock_name, stock_price, stock_daily_volume, stock_pe_ratio, stock_market_cap))
                return stock_info_list
        else:
            print("Your stock watchlist is currently empty.")
            return []

