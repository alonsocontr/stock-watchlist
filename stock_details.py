import requests

# Financial modeling api key
API_KEY = "Tle4uAteMqjtOCv4fozB2fiHlGC1VsOK"

def get_stock_info(symbol):
    short_quote_url = f"https://financialmodelingprep.com/api/v3/quote-short/{symbol}?apikey={API_KEY}"
    full_quote_url = f"https://financialmodelingprep.com/api/v3/quote/{symbol}?apikey={API_KEY}"

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


    # Check response status code for short quote API
    if response.status_code != 200:
        print("Failed to retrieve data")

    # Check response status code for full quote API
    if response2.status_code != 200:
        print("Failed to retrieve data")

    # Retrieve symbol and price value from dictionary
    symbol = (short_quote_dict["symbol"])
    price = (short_quote_dict["price"])
    volume = (short_quote_dict["volume"])
    pe_ratio = (full_quote_dict["pe"])
    market_cap = (full_quote_dict["marketCap"])

    return symbol, price, volume, pe_ratio, market_cap

