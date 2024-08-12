import sqlite3
import pandas as pd

# Connect to the SQLite database
db_path = r'C:\Users\Satar\OneDrive\Python Projects\challenge.db'
conn = sqlite3.connect(db_path)

# Load the conversions and conversions_backend tables into pandas DataFrames
conversions_df = pd.read_sql_query("SELECT * FROM conversions", conn)
conversions_backend_df = pd.read_sql_query("SELECT * FROM conversions_backend", conn)

# Close the database connection
conn.close()

# Ensure the data types are consistent between the two DataFrames
conversions_df['revenue'] = conversions_df['revenue'].astype(float)
conversions_backend_df['revenue'] = conversions_backend_df['revenue'].astype(float)

# Merge the two DataFrames on conv_id to compare them
merged_df = conversions_df.merge(conversions_backend_df, on='conv_id', suffixes=('_conv', '_backend'))

# Create a dictionary to store the number of discrepancies for each column
discrepancy_count = {
    'user_id': 0,
    'conv_date': 0,
    'market': 0,
    'revenue': 0
}

# Identify discrepancies between the two tables
for column in discrepancy_count.keys():
    discrepancies = merged_df[merged_df[f'{column}_conv'] != merged_df[f'{column}_backend']]
    discrepancy_count[column] = discrepancies.shape[0]

# Print the number of discrepancies for each column
print("Number of discrepancies between each identical column:")
for column, count in discrepancy_count.items():
    print(f"{column}: {count}")

# List all discrepancies
all_discrepancies = merged_df[(merged_df['user_id_conv'] != merged_df['user_id_backend']) |
                              (merged_df['conv_date_conv'] != merged_df['conv_date_backend']) |
                              (merged_df['market_conv'] != merged_df['market_backend']) |
                              (merged_df['revenue_conv'] != merged_df['revenue_backend'])]

print("\nDiscrepancies found:")
print(all_discrepancies)

# Save the discrepancies to a CSV file
all_discrepancies.to_csv('discrepancy_summary.csv', index=False)
