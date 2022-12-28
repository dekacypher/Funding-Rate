import requests
import pandas as pd
import datetime



from binance.client import Client
import datetime
from datetime import timezone
import asyncio
from binance import BinanceSocketManager

api_secret="SYtnp6UOHbeWZQS1ZzQ7KnaRDujB7ezTxkv1OXltVaFo45uLhPHbBuJ1O5P3byUU"
api_key="E1kR6Ct3yfvSjRDwv8dYzweOzAyZqloO4mbY54QYHBWqOkysLtXmiL0OKpMGkQ24"

client1 = Client(api_key, api_secret)
bsm = BinanceSocketManager(client1)

sym = "RENUSDT"
socket = bsm.symbol_mark_price_socket(sym)
balance = 90

# Make a file with the tickers with the most negative funding rates:
def get_funding_rates():
    URL = f"https://fapi.binance.com/fapi/v1/fundingRate?symbol="
    r = requests.get(url = URL)
    r_json = r.json()
    funding_rates_df = pd.json_normalize(r_json)
    
    return funding_rates_df

# Sort the tickers by funding rate:
def sort_funding_rates():
    funding_rates_df = get_funding_rates().sort_values(by=['fundingRate'], ascending=True)
    return funding_rates_df

import requests
from bs4 import BeautifulSoup

# Set the URL and the date you want to fetch data for
url = "https://www.binance.com/en/futures/funding-history/0"
date = "2022-01-01"

# Make a GET request to the URL
response = requests.get(url)

# Parse the HTML response
soup = BeautifulSoup(response.text, "html.parser")

# Find the table containing the funding rate data
table = soup.find("table", {"class": "fh-history-table"})

print(table)

