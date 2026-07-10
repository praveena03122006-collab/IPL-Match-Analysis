import pandas as pd

# Read the CSV file
df = pd.read_csv("matches.csv")

# Export cleaned data
df.to_csv("cleaned_ipl_data.csv", index=False)

print("Cleaned data exported successfully!")