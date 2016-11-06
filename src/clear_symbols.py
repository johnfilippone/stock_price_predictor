from pymongo import MongoClient

client = MongoClient()
db = client.Stock_Symbols

db.nasdaq_symbols.remove({})
db.nyse_symbols.remove({})
db.amex_symbols.remove({})
