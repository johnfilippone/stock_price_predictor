import requests
import csv
import json
from pymongo import MongoClient

import sys, os
sys.path.append(os.getcwd() + "/include")
from c2j import get_json_from_csv



client = MongoClient()
db = client.Stock_Symbols
collections = {
                "nasdaq_symbols" : open(os.getcwd() + "/../csv_files/nasdaq_stocks.csv", "r"),
                "nyse_symbols"   : open(os.getcwd() + "/../csv_files/nyse_stocks.csv", "r"),
                "amex_symbols"   : open(os.getcwd() + "/../csv_files/amex_stocks.csv", "r")
              }

for key in collections:
    csv_data  = collections[key].read()
    json_data = get_json_from_csv(csv_data)
    collection = db.get_collection(key)
    collection.insert_many(json_data)

