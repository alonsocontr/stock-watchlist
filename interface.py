import sys

import watchlist
from watchlist import StockWatchlist
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QInputDialog
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Watchlist")
        self.setGeometry(700, 250, 500, 500)

        # Create Stock Watchlist Title
        title_label = QLabel("Stock Watchlist", self)
        title_label.setGeometry(0,0,500,100)
        title_label.setAlignment(Qt.AlignHCenter | Qt.AlignTop)
        title_label.setFont(QFont("Arial", 30))

        # Create a label for the stock name
        stock_symbol_label = QLabel("Stocks: ", self)
        stock_symbol_label.setGeometry(0,0,300,150)
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