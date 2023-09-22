# # Import the pandas library and read election data from a URL into a DataFrame 'df'.
import pandas as pd
df = pd.read_csv('https://raw.githubusercontent.com/GBov81/python-challenge-redo2/main/PyPoll/Resources/election_data.csv')

# Print the header for the election results
print("Election Results:")
print("------------------------------")

# Calculate and print the total number of votes
print("Total votes:", df['Candidate'].count())
print("------------------------------")

# Calculate and print the percentage and count of votes for Diana DeGette
print(f"Diana DeGette: {round(df['Candidate'].str.contains('Diana').sum() * 100 / df['Candidate'].count(), 3)}%, ({df['Candidate'].str.contains('Diana').sum()})")

# Calculate and print the percentage and count of votes for Raymon Anthony Doane
print(f"Raymon Anthony Doane: {round(df['Candidate'].str.contains('Ray').sum() * 100 / df['Candidate'].count(), 3)}%, ({df['Candidate'].str.contains('Ray').sum()})")

print("------------------------------")

# Find and print the winner by identifying the candidate with the most votes
print("Winner:", max(df['Candidate'], key=df['Candidate'].value_counts().get))
print("------------------------------")
