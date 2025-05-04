import pandas as pd
from data_cleaning import standardize_column_names, convert_data_types, handle_missing_values, remove_duplicates

def clean_data(file_path):
    """ Main function to clean and format the dataset. """
    df = pd.read_csv(file_path)

    # Apply cleaning steps
    df = standardize_column_names(df)
    df = convert_data_types(df)
    df = handle_missing_values(df)
    df = remove_duplicates(df)

    # Save cleaned dataset
    df.to_csv("cleaned_dataset.csv", index=False)
    print("Data cleaning completed and saved as cleaned_dataset.csv")
    return df

# Example usage
if __name__ == "__main__":
    clean_data("raw_data.csv")  # Replace with actual file name
