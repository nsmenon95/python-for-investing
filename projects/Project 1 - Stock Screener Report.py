import pandas as pd
import numpy as np


df = pd.read_csv("data/companies.csv")

# print(df.shape)
quality_formula = np.where(
    (df["ROCE"] > 20) &
    (df["Debt to Equity"] < 0.5), "Yes", "NO"
)
df["Quality"] = quality_formula
quality_df = df[df["Quality"] == "Yes"]
print("="*45 ,"\n\t\tQUALITY STOCK SCREENER REPORT\n","="*45)

print("Total Companies Loaded      :", len(df))
print("Companies Passed            :", quality_df.shape[0] )
print("Missing Values              :",df.isna().sum().sum())
print('''
Quality Screen
--------------
ROCE > 20
Debt to Equity < 0.5

------------------------------------------
Top Quality Companies
------------------------------------------
''')
# print(df.sort_values(by=["Company", "ROCE", "PE", "Debt to Equity"], ascending=False).head(3))
print(quality_df[["Company", "ROCE","PE", "Debt to Equity"]].sort_values(by = "ROCE",ascending=False))
print('''
------------------------------------------
Sector Summary
------------------------------------------
''')

sector_summary = quality_df.groupby("Sector").agg({
    "Company" : "count",
    "ROCE" : "mean",
    "Sales Growth": "mean",
    "Debt to Equity" : "mean",
})

sector_summary.columns = ["Companies", "Avg ROCE", "Avg Growth", "Avg Debt"]
print(sector_summary)

print('''
------------------------------------------
Quality Company Summary
------------------------------------------
''')
print("Highest ROCE             :",quality_df["ROCE"].max())

print("Lowest Debt              :",quality_df["Debt to Equity"].min())

print("Average ROCE             :",quality_df["ROCE"].mean())

print("Average Sales Growth     :",quality_df["Sales Growth"].mean())