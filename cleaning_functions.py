import pandas as pd


def clean_column_names(insurance_company):
    insurance_company.columns = (insurance_company.columns.str.strip().str.lower()-str.replace(" ", "_"))
    return insurance_company.columns.str.strip().str.lower().str.replace(" ", "_")


def remove_empty_rows(insurance_company):
    return insurance_company.dropna(axis=0, how="all")


def remove_duplicate_rows(insurance_company):
    return insurance_company.drop_duplicates()

def clean_open_complaints(insurance_company):
    """Clean the number_of_open_complaints column."""
    # Adapt this logic after inspecting the column's actual values.
    complaints = (
        insurance_company["number_of_open_complaints"]
        .astype("string")
        .str.split("/")
        .str[1]
    )

    insurance_company = insurance_company.copy()
    insurance_company["number_of_open_complaints"] = pd.to_numeric(
        complaints,
        errors="coerce"
    )

    return insurance_company


def main():

    url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
    insurance_company = pd.read_csv(url)

    insurance_company = clean_column_names(insurance_company)
    insurance_company = remove_empty_columns(insurance_company)
    insurance_company = clean_open_complaints(insurance_company)
    insurance_company = remove_duplicate_rows(insurance_company)

    return insurance_company


if __name__ == "__main__":
    insurance_company = main()
    display(insurance_company)