import time
import requests
from pymongo import MongoClient

import sys, os
sys.path.append(os.getcwd() + "/include")
from c2j import get_json_from_csv

client = MongoClient()
db = client.Stock_Data

base_url = "http://download.finance.yahoo.com/d/quotes.csv"
symbol = "GOOG"

fields = "ask,bid\n"
pricing_url = base_url + "?s=" + symbol + "&f=ab"

while 1:
    csv_data = fields + requests.get(pricing_url).text
    json_data = get_json_from_csv(csv_data)

    collection = db.get_collection(symbol)
    collection.insert(json_data)
    time.sleep(1)

