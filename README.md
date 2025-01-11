# Stock Market Watchlist Application
## Overview
The **Stock Market Watchlist Application** is a Python-based desktop application that allows users to track stock prices in real-time, manage a personalized watchlist, and view detailed stock information. Built with **PyQt5** for the GUI and integrated with the **Financial Modeling Prep API**, this app provides an intuitive interface for monitoring stock market data.

---

## Features
- **Add and remove stocks** from your personalized watchlist.
- **Real-time updates** for stock prices, market data, and other metrics.
- **Detailed stock information**, including price, volume, P/E ratio, market cap, and one-day price change.
- **Secure API key management** via environment variables.

---

## Requirements
- Python 3.7 or higher
- Pip (Python package installer)

---

## Installation

### Step 1: Download the Repository
1. Visit the [GitHub Repository](https://github.com/alonsocontr/stock_watchlist).
2. Click the green **Code** button and select **Download ZIP**.
3. Extract the downloaded ZIP file to a folder on your computer.

### Step 2: Install Dependencies
1. Open a terminal or command prompt.
2. Navigate to the extracted folder.
3. Install the required Python libraries:
   \`\`\`
   python -m pip install -r requirements.txt
   \`\`\`

### Step 3: Set Up Environment Variables
1. In the extracted folder, open the .env file.
2. Replace YOUR_API_KEY_HERE with your actual API key from the Financial Modeling Prep API.

---

## Usage

To run the application:
1. Open a terminal or command prompt.
2. Navigate to the project folder.
3. Launch the app:
   \`\`\`bash
   python main.py
   \`\`\`

The application will open, and you can:
- **Add stocks** to your watchlist by entering their ticker symbols.
- **Remove stocks** by typing their ticker symbols and clicking "Remove".
- **View detailed stock data**, such as price, volume, P/E ratio, and market cap.

---

## File Structure

- \`main.py\`: Entry point for the application.
- \`watchlist.py\`: Manages the stock watchlist (add/remove stocks).
- \`interface.py\`: Contains the PyQt5 GUI implementation.
- \`stock_details.py\`: Handles API calls to fetch stock information.
- \`.env.example\`: Template for environment variables.
- \`requirements.txt\`: Lists all dependencies for the project.

---

## .env File

The \`.env\` file stores sensitive information, such as your API key. Example:
\`\`\`
API_KEY=your_actual_api_key_here
\`\`\`

Make sure to:
- Keep this file private.
- Never share it publicly.

---

## Troubleshooting

- **Missing API Key**: Ensure your \`.env\` file contains the correct API key.
- **Dependency Issues**: Verify all dependencies are installed using:
  \`\`\`bash
  pip install -r requirements.txt
  \`\`\`
- **Python Version**: Ensure you’re using Python 3.7 or higher.

---

## Contributions

Contributions are welcome! If you’d like to contribute:
- Open an issue for bugs or feature requests.
- Submit a pull request with your changes.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

## Author

Created by Alonso Contreras (https://github.com/alonsocontr).
