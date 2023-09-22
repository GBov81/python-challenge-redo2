import pandas as pd

df = pd.read_csv('https://raw.githubusercontent.com/GBov81/python-challenge-redo/main/Resources/election_data.csv')

print("Election Results:") 
print("------------------------------")
print("Total votes:", df['Candidate'].count())
print("------------------------------")
print(f"Diana DeGette: {round(df['Candidate'].str.contains('Diana').sum() * 100 / df['Candidate'].count(), 3)}%, ({df['Candidate'].str.contains('Diana').sum()})")
print(f"Raymon Anthony Doane: {round(df['Candidate'].str.contains('Ray').sum() * 100 / df['Candidate'].count(), 3)}%, ({df['Candidate'].str.contains('Ray').sum()})")
print("------------------------------")
print("Winner:", max(df['Candidate'], key=df['Candidate'].value_counts().get))
print("------------------------------")
