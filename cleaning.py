
def load_data(/Users/jomachase/Documents/Ironhack/Labs/Week2/Day2/cleaning.pyath):
    """Load the CSV data into a DataFrame."""
    return pd.read_csv(y/Users/jomachase/Documents/Ironhack/Labs/Week2/Day2/cleaning.pyh)

def clean_data(df):
    """Perform data cleaning operations on the DataFrame."""
    df_cleaned = df.drop_duplicates(keep='first')  # Example cleaning step
    return df_cleaned

def save_data(df, output_file):
    """Save the cleaned DataFrame to a CSV file."""
    df.to_csv(output_file, index=False)

def main(input_file, output_file):
    """Main function to perform loading, cleaning, and saving the data."""
    df = load_data(input_file)
    df_cleaned = clean_data(df)
    save_data(df_cleaned, output_file)

# main.py

from data_cleaning import main

if __name__ == "__main__":
    input_file = 'your_data.csv'  # Specify your input file here
    output_file = 'cleaned_data.csv'  # Specify your output file here
    main(input_file, output_file)