#Standardize the column names of the dataframe
df.columns = (
    df.columns
    .str.strip()
    .str.lower()
    .str.replace(' ', '_')
    .str.replace(r'\bst\b', 'state', regex=True)
    .str.replace('__', '_')
)
df.head()


# Clean 'gender' column
df['gender'] = df['gender'].str.strip().str.lower()
df['gender'] = df['gender'].replace({
    'f': 'F', 'female': 'F', 'femal': 'F',
    'm': 'M', 'male': 'M'
})

# Clean 'state' column
df['state'] = df['state'].replace({
    'AZ': 'Arizona',
    'Cali': 'California',
    'WA': 'Washington'})

# Clean 'education' column
df['education'] = df['education'].replace({
    'bachelors': 'bachelor'
})

# Clean 'customer_lifetime_value' column (remove %)
df['customer_lifetime_value'] = df['customer_lifetime_value'].str.replace('%', '', regex=False)

# Clean 'vehicle_class' column
df['vehicle_class'] = df['vehicle_class'].replace({
    'Sports Car': 'luxury',
    'Luxury SUV': 'luxury',
    'Luxury Car': 'luxury'
})


# 1. Identify duplicate rows in the dataframe
duplicates = df.duplicated()
print(f"Number of duplicate rows: {duplicates.sum()}")

# 2. Decide on strategy
# Let's assume we want to keep only the first occurrence of each duplicated row
# This is a common choice to avoid losing data while removing exact duplicates.

# 3. Drop duplicate rows, keeping the first occurrence
df_cleaned = df.drop_duplicates(keep='first')

# 4. Verify duplicates are handled
duplicates_after = df_cleaned.duplicated().sum()
print(f"Number of duplicates after cleaning: {duplicates_after}")

# 5. Save the cleaned dataframe to a new CSV file
df_cleaned.to_csv('cleaned_dataset.csv', index=False)