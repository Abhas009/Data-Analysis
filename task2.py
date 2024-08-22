import pandas as pd

# Load the CSV file into a DataFrame
df = pd.read_csv('task2.csv')  

# Display the first few rows
print(df.head())

# Get information about the DataFrame
print(df.info())

# Check for missing values
print(df.isnull().sum())

# Fill missing values in 'SulphidityL-4' with 0
df['SulphidityL-4'] = df['SulphidityL-4'].fillna(0)

# Remove rows with missing values in any column
df = df.dropna()

# Filter rows where 'ChipRate' is greater than 16.5
filtered_df = df[df['ChipRate'] > 16.5]

# Group by 'Observation' and calculate the mean of 'ChipRate'
grouped_df = df.groupby('Observation')['ChipRate'].mean()

