import pandas as pd


portfolio = pd.read_csv("data/portfolio.csv")
# print(portfolio)
# print(portfolio.shape)
# print(portfolio.head())
# print(portfolio.info())
# print(portfolio.isna().sum().sum())
# print(portfolio.describe())
# portfolio["Invested Amount"] = (portfolio["Qty"] * portfolio["Avg Price"])
#
# portfolio["Current Value"] = (portfolio["Qty"] * portfolio["Current Price"])
#
# portfolio["Profit/Loss ₹"] = portfolio["Current Value"] - portfolio["Invested Amount"]
#
# portfolio["Profit /Loss %"] = (portfolio["Profit/Loss ₹"]/ portfolio["Invested Amount"]) * 100
#
# print(portfolio)
print(type(portfolio["Qty"]))
print(type(["Qty"]))
