import pandas as pd

print("="*45)
print("\t\tLOAD DATA")
print("="*45)
portfolio = pd.read_csv("data/portfolio.csv")
print(portfolio.shape)
portfolio.head()
portfolio.info()
print(portfolio.isna().sum().sum())
# print("="*45)
# print("\t\tCALCULATED COLUMNS")
# print("="*45)
portfolio["Invested Amount"] = (portfolio["Qty"] * portfolio["Avg Price"])
portfolio["Current Value"] = (portfolio["Qty"] * portfolio["Current Price"])
portfolio["Profit/Loss ₹"] = portfolio["Current Value"] - portfolio["Invested Amount"]
portfolio["Profit/Loss %"] = (portfolio["Profit/Loss ₹"]/ portfolio["Invested Amount"]) * 100


print("="*45)
print("\t\tPORTFOLIO SUMMARY")
print("="*45)

print("Total Stocks :current Value ",portfolio.shape[0])

total_invested = portfolio["Invested Amount"].sum()
print(f"Total Invested :  ₹ {total_invested:,.2f}")

total_current = portfolio["Current Value"].sum()
print(f"Current Value : ₹{total_current:,.2f}")

overall_profit = portfolio["Profit/Loss ₹"].sum()
print("Overall Profit : ",overall_profit)

overall_return = (overall_profit/total_invested)*100
print(f"Overall Return : {overall_return:.2f}%")

print("="*45)
print("\t\tBEST AND WORST PERFORMER")
print("="*45)
best_index = portfolio["Profit/Loss %"].idxmax()
best = portfolio.loc[best_index]
worst_index = portfolio["Profit/Loss %"].idxmin()
worst = portfolio.loc[worst_index]

print("-"*45)
print("\t\tBEST PERFORMER")
print("-"*45)
print("Stock                      : ", best["Stock"])
print("Return %               : ", best["Profit/Loss %"])
print("Profit ₹                  : ", best["Profit/Loss ₹"])

print("-"*45)
print("\t\tWORST PERFORMER")
print("-"*45)
print("Stock                      : ", worst["Stock"])
print("Return %               : ", worst["Profit/Loss %"])
print("Profit ₹                  : ", worst["Profit/Loss ₹"])

print("="*45)
print("\t\tPORTFOLIO ALLOCATION")
print("="*45)
portfolio["Allocation %"] = (portfolio["Current Value"]/ total_current)*100
print(portfolio[["Stock","Current Value","Allocation %"]])
sort_allocation = portfolio.sort_values(by="Allocation %", ascending=False)
print(sort_allocation)
print(portfolio["Allocation %"].sum())

print("-"*45)
print("\t\tLARGEST HOLDING")
print("-"*45)

largest_holding_index = portfolio["Allocation %"].idxmax()
largest_holding = portfolio.loc[largest_holding_index]
print("Stock                : ",largest_holding["Stock"])
print(f"Allocation        : {largest_holding["Allocation %"]:.2f}%")