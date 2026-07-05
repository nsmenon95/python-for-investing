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
print("="*45)
print("\t\tPORTFOLIO SUMMARY")
print("="*45)
print("Total Stocks : ",portfolio.shape[0])

portfolio["Invested Amount"] = (portfolio["Qty"] * portfolio["Avg Price"])
portfolio["Current Value"] = (portfolio["Qty"] * portfolio["Current Price"])
portfolio["Profit/Loss ₹"] = portfolio["Current Value"] - portfolio["Invested Amount"]
portfolio["Profit/Loss %"] = (portfolio["Profit/Loss ₹"]/ portfolio["Invested Amount"]) * 100

total_invested = portfolio["Invested Amount"].sum()
print("Total Invested : ",total_invested)

total_current = portfolio["Current Value"].sum()
print("Current Value : ",total_current)

overall_profit = portfolio["Profit/Loss ₹"].sum()
print("Overall Profit : ",overall_profit)

overall_return = (overall_profit/total_invested)*100
print("Overall Return : ",overall_return)