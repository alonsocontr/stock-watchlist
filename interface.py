from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton, QHBoxLayout, QVBoxLayout, QWidget, QSpacerItem, QSizePolicy, QLineEdit
from PyQt5.QtGui import QFont
from PyQt5.QtCore import Qt, QTimer
import sys

import watchlist
import stock_details
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Stock Watchlist")
        self.setGeometry(650, 100, 600, 800)

        # Initialize stock watchlist class (with database integration)
        self.stock_watchlist_instance = watchlist.StockWatchlist()

        # Add a widget to display the stocks
        main_widget = QWidget(self)
        self.setCentralWidget(main_widget)

        # Main vertical layout for the entire window
        self.layout = QVBoxLayout(main_widget)

        # Create Stock Watchlist Title
        title_label = QLabel("Stock Watchlist:", self)
        title_label.setFont(QFont("Arial", 30))
        title_label.setAlignment(Qt.AlignTop)
        self.layout.addWidget(title_label)

        # Add some spacing after the title to separate it from the stock list
        self.layout.addSpacing(20)

        # Create a container for the stock list (so it can expand)
        self.stock_list_container = QVBoxLayout()
        self.layout.addLayout(self.stock_list_container)

        # Dictionary to hold stock labels and button states and layouts
        self.stock_labels = {}
        self.detail_buttons = {}
        self.stock_layouts = {}

        # Add loop for each stock in stock list (from the database)
        for stock in self.stock_watchlist_instance.stock_list:
            self.add_stock_to_gui(stock)

        # Spacer to push the buttons to the bottom
        spacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.layout.addItem(spacer)

        # Input box for stock symbol
        self.stock_symbol_input = QLineEdit(self)
        self.stock_symbol_input.setFont(QFont("Arial", 20))
        self.stock_symbol_input.setPlaceholderText("Enter stock symbol")
        self.stock_symbol_input.setFixedSize(650, 50)
        self.layout.addWidget(self.stock_symbol_input)

        # Button to add a stock
        self.add_stock_button = QPushButton("Add stock", self)
        self.add_stock_button.clicked.connect(lambda: self.modify_stock(action="add"))
        self.add_stock_button.setFixedSize(650, 75)
        self.layout.addWidget(self.add_stock_button)

        # Button to remove a stock
        self.remove_stock_button = QPushButton("Remove stock", self)
        self.remove_stock_button.clicked.connect(lambda: self.modify_stock(action="remove"))
        self.remove_stock_button.setFixedSize(650, 75)
        self.layout.addWidget(self.remove_stock_button)

        # Set up QTimer to refresh stock data every 30 seconds
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.refresh_data)  # Call `refresh_data` every timeout
        self.timer.start(30000)  # 30 seconds (30,000 ms)

        # Trigger the first refresh immediately
        self.refresh_data()

    def modify_stock(self, action):
        stock_symbol = self.stock_symbol_input.text().strip().upper()

        if not stock_symbol:
            print("Please enter a valid stock symbol.")
            return

        if action == "add":
            self.stock_watchlist_instance.add_stock(stock_symbol)
            self.add_stock_to_gui(stock_symbol)
        elif action == "remove":
            self.stock_watchlist_instance.remove_stock(stock_symbol)
            self.remove_stock_from_gui(stock_symbol)

        # Clear the input field
        self.stock_symbol_input.clear()

    def add_stock_to_gui(self, stock_symbol):
        # Create horizontal layout for stock
        stock_list_h_layout = QHBoxLayout()

        # Create stock symbol label
        stock_symbol_label = QLabel(f"- {stock_symbol}", self)
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
        details_button.clicked.connect(
            lambda checked, btn=details_button, lbl=stock_details_label: self.toggle_details(btn, lbl))
        stock_list_h_layout.addWidget(details_button)

        # Store layout in the dictionary
        self.stock_layouts[stock_symbol] = stock_list_h_layout

        # Add the layout to the stock list container
        self.stock_list_container.addLayout(stock_list_h_layout)

    def remove_stock_from_gui(self, stock_symbol):
        if stock_symbol in self.stock_layouts:
            # Get the layout to be removed
            layout = self.stock_layouts[stock_symbol]

            # Remove all widgets from the layout
            while layout.count():
                item = layout.takeAt(0)
                widget = item.widget()
                if widget:
                    widget.deleteLater()

            # Remove the layout from the container
            self.stock_list_container.removeItem(layout)

            # Delete the layout from the dictionary
            del self.stock_layouts[stock_symbol]

    def refresh_data(self):
        for stock in self.stock_watchlist_instance.stock_list:
            stock_info = stock_details.get_stock_info(stock)
            if stock_info:
                symbol, price, volume, pe_ratio, market_cap, price_change_one_day = stock_info
                formatted_text = (f"Price: ${price:,.2f}\n"
                                  f"Volume: {volume:,}\n"
                                  f"P/E Ratio: {pe_ratio:.2f}\n"
                                  f"Market Cap: ${market_cap:,}\n"
                                  f"Price Change 1D: {price_change_one_day:.2f}%")
                self.stock_layouts[stock].itemAt(1).widget().setText(formatted_text)
            else:
                self.stock_layouts[stock].itemAt(1).widget().setText("Failed to load data")

    def toggle_details(self, button, label):
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
