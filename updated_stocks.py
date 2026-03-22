import pandas as p
df = p.read_csv(
    "https://archives.nseindia.com/content/indices/ind_nifty50list.csv"
)
print("Stocks updated")
df.to_csv("D:/Stock Analyzer/updated_stocks.csv", index=False)