import pandas as pd

# Load dataset
df = pd.read_csv("C:/Users/Muktha/OneDrive/Desktop/netflix_titles.csv")
print("Original Shape:", df.shape)
print(df.head())

# Count missing values per column
print("\nMissing values per column:\n", df.isnull().sum())

# Remove Duplicates
df.drop_duplicates(inplace=True)

# Fill Missing Values
df['country'] = df['country'].fillna("Unknown")
df['director'] = df['director'].fillna("Not Available")
df['cast'] = df['cast'].fillna("Not Available")

# Standardize Categorical Columns
df['type'] = df['type'].str.lower().str.strip()
df['listed_in'] = df['listed_in'].str.lower().str.strip()

# Fix Date Formats
df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
df['date_added'] = df['date_added'].dt.strftime('%d-%m-%Y')

# Rename Columns (snake_case)
df.columns = df.columns.str.lower().str.replace(' ', '_')

# Clean duration column
df['duration_cleaned'] = df['duration'].str.extract('(\d+)')  # extract numbers only
df['duration_cleaned'] = pd.to_numeric(df['duration_cleaned'], errors='coerce')

# Save Clean Dataset
df.to_csv("netflix_cleaned.csv", index=False)

print("\nCleaning Completed. Cleaned dataset saved as 'netflix_cleaned.csv'")
print("New Shape:", df.shape)
