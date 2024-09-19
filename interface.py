import sys
import watchlist
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QListWidget, QVBoxLayout
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Watchlist")
        self.setGeometry(700, 250, 500, 500)

        # Initialize stock watchlist class
        self.stock_watchlist_instance = watchlist.StockWatchlist()
        self.stock_watchlist_instance.add_stock("NVDA")
        self.stock_watchlist_instance.add_stock("AAPL")

        # Add loop for each stock in stock list

        for stock in self.stock_watchlist_instance.stock_list:
            stock_info = self.stock_watchlist_instance.stock_data[stock]
            # Gets stock symbol
            stock_symbol_label = QLabel(f"-{stock_info[0]}", self)
            stock_symbol_label.setGeometry(0, 0, 300, 300)
            stock_symbol_label.setFont(QFont("Arial", 20))

            # Gets stock price
            stock_price_label = QLabel(f"Price: ${stock_info[1]:,.2f}", self)
            stock_price_label.setGeometry(250,0,300,500)
            stock_price_label.setFont(QFont("Arial", 10))

            # Gets stock volume
            stock_volume_label = QLabel(f"Daily Volume: {stock_info[2]:,}", self)
            stock_volume_label.setGeometry(250,0,300,550)
            stock_volume_label.setFont(QFont("Arial", 10))

            # Gets stock pe ratio
            stock_pe_label = QLabel(f"P/E Ratio: {stock_info[3]:.2f}", self)
            stock_pe_label.setGeometry(250,0,300,600)
            stock_pe_label.setFont(QFont("Arial", 10))

            # Gets stock market cap
            stock_market_cap_label = QLabel(f"Market Cap: ${stock_info[4]:,}", self)
            stock_market_cap_label.setGeometry(250,0,300,650)
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
