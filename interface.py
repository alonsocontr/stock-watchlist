import sys
import watchlist
from stock_details import get_stock_info
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QListWidget, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Watchlist")
        self.setGeometry(700, 250, 500, 500)

        #Initialize stock watchlist class
        stock_watchlist_instance = watchlist.StockWatchlist()
        stock_list_values = stock_watchlist_instance.store_watchlist()
        stock_watchlist_instance.add_stock("NVDA")
        stock_watchlist_instance.add_stock("AAPL")

        # Initialize get stock
        # Currently gets stock values of nvidia or 1st stock in list
        # Add loop for each stock in stock list
        stock_list_values = get_stock_info(stock_watchlist_instance.stock_list[0])

        # Gets stock symbol
        stock_symbol = stock_list_values[0]
        stock_symbol_label = QLabel(f"-{stock_symbol}", self)
        stock_symbol_label.setGeometry(0, 0, 300, 300)
        stock_symbol_label.setFont(QFont("Arial", 20))

        # Gets stock price
        stock_price = stock_list_values[1]
        price_label = QLabel(f"Price: ${stock_price:,.2f}", self)
        price_label.setGeometry(0,0,300,500)
        price_label.setFont(QFont("Arial", 10))

        # Gets stock volume
        stock_volume = stock_list_values[2]
        volume_label = QLabel(f"Daily Volume: {stock_volume:,}", self)
        volume_label.setGeometry(0,0,300,600)
        volume_label.setFont(QFont("Arial", 10))

        # Gets stock pe ratio
        stock_pe_ratio = stock_list_values[3]
        stock_pe_label = QLabel(f"P/E Ratio: {stock_pe_ratio:.2f}", self)
        stock_pe_label.setGeometry(0,0,300,700)
        stock_pe_label.setFont(QFont("Arial", 10))

        # Gets stock market cap
        stock_market_cap = stock_list_values[4]
        stock_market_cap_label = QLabel(f"Market Cap: ${stock_market_cap:,}", self)
        stock_market_cap_label.setGeometry(0,0,300,800)
        stock_market_cap_label.setFont(QFont("Arial", 10))

        # Create Stock Watchlist Title
        title_label = QLabel("Stock Watchlist", self)
        title_label.setGeometry(0,0,500,100)
        title_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        title_label.setFont(QFont("Arial", 30))

        # Create a label for the stock name
        stock_symbol_label = QLabel("Stocks: ", self)
        stock_symbol_label.setGeometry(0,0,300,175)
        stock_symbol_label.setFont(QFont("Arial", 20))

        # Button to add a stock
        add_stock_button = QPushButton("Add stock", self)
        add_stock_button.move(350, 70)

        # Button to remove a stock
        remove_stock_button = QPushButton("Remove stock", self)
        remove_stock_button.move(350, 120)



def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()