import os
import pandas as p
import streamlit as st
from phi.agent import Agent
from phi.model.groq import Groq
from dotenv import load_dotenv
load_dotenv()
api_key = os.getenv("API_KEY")
st.title("Stock Outlook")
st.write("This page provides an outlook on Nifty50 stocks")
updated_stocks = p.read_csv("updated_stocks.csv")
stock_list = updated_stocks["Company Name"].tolist()
selected_stock = st.selectbox("Select a stock to view its outlook:", stock_list)
stock_news = p.read_csv("stock_news.csv")
corpotate_actions = p.read_csv("corporate_actions.csv")
stock_analysis = p.read_csv("stock_analytics.csv")
signal_json = {"Signals":stock_analysis[stock_analysis["Name"] == selected_stock].to_dict()}
news_json = {"News":stock_news[stock_news["name"] == selected_stock].to_dict()}
actions_json = {"Actions":corpotate_actions[corpotate_actions["name"] == selected_stock].iloc[0].to_dict()}
signal_agent = Agent(
model = Groq(id="openai/gpt-oss-120b",api_key=api_key),
instructions = "Summarize the stock signals for the selected stock."
)
news_agent = Agent(
model = Groq(id="openai/gpt-oss-120b",api_key=api_key),
instructions = "Summarize the stock news for the selected stock" 
    )
actions_agent = Agent(
model = Groq(id="openai/gpt-oss-120b",api_key=api_key),
instructions = "Summarize the stock corporate action history for the selected stock."
    )
combined_response = f"""
"Signals": {signal_agent.run(f"Analyze this data: {signal_json}").content}
"News": {news_agent.run(f"Analyze this data: {news_json}").content}
"Actions": {actions_agent.run(f"Analyze this data: {actions_json}").content}
"""
print(combined_response)
combined_agent = Agent(
model = Groq(id="openai/gpt-oss-120b",api_key=api_key),
instructions = "Based on the stock signals, news and corporate actions, provide an overall outlook for a retail investor only for the selected stock.No investment advice,risk adjusted view and monitoring checklist for the stock."
)
st.write(combined_agent.run(f"Give consolidated outlook from this data: {combined_response}").content)