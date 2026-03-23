import pandas as p
import yfinance as yf
tickers = p.read_csv("updated_stocks.csv")["Symbol"].tolist()
names = p.read_csv("updated_stocks.csv")["Company Name"].tolist()
company_ticker_mapping = dict(zip(tickers, names))
corporate_actions = p.DataFrame()
for ticker in tickers:
    print(f"Fetching corporate actions for {ticker}...")
    actions = yf.Ticker(ticker+".NS").actions.reset_index()
    actions['name'] = company_ticker_mapping[ticker]
    corporate_actions = p.concat([corporate_actions, actions])

print(corporate_actions)
corporate_actions.to_csv("D:/Stock Analyzer/corporate_actions.csv", index=False)