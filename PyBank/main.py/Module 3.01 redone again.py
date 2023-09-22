import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/GBov81/python-challenge-redo2/main/PyBank/Resources/budget_data.csv')

print("Financial Analysis:")
print("------------------------------")
print("Total Months:", df['Profit/Losses'].count())
print(f"Total: ${df['Profit/Losses'].sum()}")
print(f"Average Change: ${(df['Profit/Losses'].diff()).mean():.2f}")
print(f"Greatest Increase in Profits: ${(df['Profit/Losses'].diff()).max()}")
print(f"Greatest Decrease in Profits: ${(df['Profit/Losses'].diff()).min()}")
