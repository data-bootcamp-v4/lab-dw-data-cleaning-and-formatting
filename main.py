import data_cleaning

def main():
    """Executes the full data cleaning pipeline."""
    filepath = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
    output_filepath = "cleaned_data.csv"

    # Load dataset
    df = data_cleaning.load_data(filepath)

    # Apply cleaning functions step by step
    df = data_cleaning.standardize_column_names(df)
    df = data_cleaning.clean_gender(df)
    df = data_cleaning.clean_state(df)
    df = data_cleaning.clean_education(df)
    df = data_cleaning.clean_customer_lifetime_value(df)
    df = data_cleaning.clean_vehicle_class(df)
    df = data_cleaning.fix_open_complaints(df)
    df = data_cleaning.handle_missing_values(df)
    df = data_cleaning.convert_numeric_columns(df)
    df = data_cleaning.remove_duplicates(df)

    # Save cleaned data
    data_cleaning.save_cleaned_data(df, output_filepath)

    print("Data cleaning completed! Cleaned file saved as:", output_filepath)

# Run the main function
if __name__ == "__main__":
    main()