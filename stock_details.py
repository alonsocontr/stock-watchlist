import requests
from dotenv import load_dotenv
import os

# Load environmental variables
load_dotenv()

# Financial modeling API key
API_KEY = os.getenv("API_KEY")

def get_stock_info(symbol):
    short_quote_url = f"https://financialmodelingprep.com/api/v3/quote-short/{symbol}?apikey={API_KEY}"
    full_quote_url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={API_KEY}"
    price_change_url = f"https://financialmodelingprep.com/api/v3/stock-price-change/{symbol}?apikey={API_KEY}"

    # Initialize short quote
    response = requests.get(short_quote_url)
    data = response.json()

    # Converting data from a list to a dictionary
    short_quote_dict = data[0]

    # Initialize full quote
    response2 = requests.get(full_quote_url)
    data2 = response2.json()

    # Converting data from a list to a dictionary
    full_quote_dict = data2[0]

    # Initialize stock market price change %
    response3 = requests.get(price_change_url)
    data3 = response3.json()

    # Converting data from a list to a dictionary
    price_change_dict = data3[0]

    # Retrieve symbol and price value from dictionary
    symbol = short_quote_dict["symbol"]
    price = short_quote_dict["price"]
    volume = short_quote_dict["volume"]
    pe_ratio = full_quote_dict["pe"]
    market_cap = full_quote_dict["marketCap"]
    price_change_one_day = price_change_dict["1D"]

    return symbol, price, volume, pe_ratio, market_cap, price_change_one_day
