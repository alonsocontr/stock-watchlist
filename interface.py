import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
import watchlist
import stock_details

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Watchlist")
        self.setGeometry(700, 250, 600, 500)

        # Initialize stock watchlist class
        self.stock_watchlist_instance = watchlist.StockWatchlist()
        self.stock_watchlist_instance.add_stock("NVDA")
        self.stock_watchlist_instance.add_stock("AAPL")

        # Add a widget to display the stocks
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)
        self.layout = QVBoxLayout(main_widget)

        # Create Stock Watchlist Title
        title_label = QLabel("Stock Watchlist", self)
        title_label.setFont(QFont("Arial", 30))
        title_label.setAlignment(Qt.AlignTop)
        self.layout.addWidget(title_label)

        # Add some spacing after the title to separate it from the stock list
        self.layout.addSpacing(20)

        # Dictionary to hold stock labels and button states
        self.stock_labels = {}
        self.detail_buttons = {}

        # Add loop for each stock in stock list
        for stock in self.stock_watchlist_instance.stock_list:
            stock_list_h_layout = QHBoxLayout()

            # Create stock symbol label
            stock_symbol_label = QLabel(f"- {stock}", self)
            stock_symbol_label.setFont(QFont("Arial", 20))
            stock_list_h_layout.addWidget(stock_symbol_label)

            # Create label for displaying stock details
            stock_details_label = QLabel("Loading...", self)
            stock_details_label.setFont(QFont("Arial", 12))
            stock_details_label.setVisible(False)  # Initially hidden
            stock_list_h_layout.addWidget(stock_details_label)

            # Show/Hide details button
            details_button = QPushButton("Show details", self)
            details_button.setFont(QFont("Arial", 10))

            # Capture current stock, button, and label in lambda using default arguments
            details_button.clicked.connect(lambda checked, btn=details_button, lbl=stock_details_label: self.toggle_details(btn, lbl))
            stock_list_h_layout.addWidget(details_button)

            # Store labels and buttons in dictionaries for later access
            self.stock_labels[stock] = stock_details_label
            self.detail_buttons[stock] = details_button

            # Add the layout to the main layout
            self.layout.addLayout(stock_list_h_layout)
            self.layout.addSpacing(10)

        # Set up QTimer to refresh stock data every 30 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_data)  # Call `refresh_data` every timeout
        self.timer.start(30000)  # 30 seconds (30,000 ms)

        # Trigger the first refresh immediately
        self.refresh_data()

        # Button to add a stock (placeholder for now)
        add_stock_button = QPushButton("Add stock", self)
        self.layout.addWidget(add_stock_button)

        # Button to remove a stock (placeholder for now)
        remove_stock_button = QPushButton("Remove stock", self)
        self.layout.addWidget(remove_stock_button)

    def refresh_data(self):
        """Fetch stock data and update the labels."""
        for stock in self.stock_watchlist_instance.stock_list:
            stock_info = stock_details.get_stock_info(stock)
            if stock_info:
                symbol, price, volume, pe_ratio, market_cap = stock_info
                formatted_text = (f"Price: ${price:,.2f} | "
                                  f"Volume: {volume:,} | "
                                  f"P/E Ratio: {pe_ratio:.2f} | "
                                  f"Market Cap: ${market_cap:,}")
                # Update the label with the new stock data
                self.stock_labels[stock].setText(formatted_text)
            else:
                # If the data retrieval fails, update the label with an error message
                self.stock_labels[stock].setText("Failed to load data")

    def toggle_details(self, button, label):
        """Toggle stock details visibility and change button text."""
        if label.isVisible():
            label.setVisible(False)
            button.setText("Show details")
        else:
            label.setVisible(True)
            button.setText("Hide details")


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    main()
