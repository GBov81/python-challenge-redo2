# Import the pandas library and read budget data from a URL into a DataFrame 'df'.
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/GBov81/python-challenge-redo2/main/PyBank/Resources/budget_data.csv')

# Print the header for the financial analysis.
print("Financial Analysis:")
print("------------------------------")

# Calculate and print the total number of months.
print("Total Months:", df['Profit/Losses'].count())

# Calculate and print the total net sum of profit/losses.
print(f"Total: ${df['Profit/Losses'].sum()}")

# Calculate and print the average change in profit/losses.
print(f"Average Change: ${(df['Profit/Losses'].diff()).mean():.2f}")

# Calculate and print the greatest increase and decrease in profits.
print(f"Greatest Increase in Profits: ${(df['Profit/Losses'].diff()).max()}")
print(f"Greatest Decrease in Profits: ${(df['Profit/Losses'].diff()).min()}")

