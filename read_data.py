import pandas as pd

# source: https://www.kaggle.com/datasets/jorgesamuelyanas/solana-usdt-historical-data?select=5minute.csv
filename = '5minute.csv'
df = pd.read_csv(filename, header=None)

# remove unnecessary columns
df.drop([0, 5, 6], axis=1, inplace=True)
df.columns = ['open', 'high', 'low', 'close']

# print(df.head())

# Define the number of previous rows to concatenate
num_prev_rows = 3

selected_rows = df.iloc[num_prev_rows-1::num_prev_rows].reset_index(drop=True)
# print(selected_rows.head())

# Loop through each previous row
for prev_row in range(1, num_prev_rows + 1):
    # Create new columns for each previous row
    for col in df.columns:
        selected_rows[f"{col}_prev_{prev_row}"] = [df[col].iloc[i-prev_row] for i in range(num_prev_rows, len(df), num_prev_rows)]

# Drop the first four columns
selected_rows.drop(selected_rows.columns[:4], axis=1, inplace=True)

# print(df.head())
# print(selected_rows.head(1))
