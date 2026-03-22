import pandas as p
import yfinance as yf
df = p.read_csv(
    "D:/Stock Analyzer/updated_stocks.csv"
)
all_data = {}
tickers = df["Symbol"].tolist()
names = df["Company Name"].tolist()
for ticker in tickers:
    df = yf.download(ticker+".NS", start="2024-01-01")
    all_data[ticker] = df
company_ticker_mapping = dict(zip(tickers, names))
all_stocks_data = p.DataFrame()
for ticker in tickers:
    stock_data = all_data[ticker].reset_index().droplevel(1, axis=1)
    stock_data['Name'] = company_ticker_mapping[ticker]
    all_stocks_data = p.concat([all_stocks_data, stock_data], ignore_index=True)
all_stocks_data.to_csv("D:/Stock Analyzer/all_stocks_data.csv")
