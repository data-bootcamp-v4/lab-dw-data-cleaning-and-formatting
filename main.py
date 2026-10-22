import pandas as pd

from cleaning import (
    clean_column_names,
    clean_values,
    format_data_types,
    handle_null_values,
    remove_duplicates,
    save_dataset
)


def main():
    url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"

    df = pd.read_csv(url)

    # Exercise 1
    df = clean_column_names(df)

    # Exercise 2
    df = clean_values(df)

    # Exercise 3
    df = format_data_types(df)

    # Exercise 4
    df = handle_null_values(df)

    # Exercise 5
    df = remove_duplicates(df)

    # Save the cleaned dataset
    save_dataset(df)

    print("\nFinal data types:")
    print(df.dtypes)

    print("\nFinal dataset:")
    print(df.head())

    return df


if __name__ == "__main__":
    df = main()