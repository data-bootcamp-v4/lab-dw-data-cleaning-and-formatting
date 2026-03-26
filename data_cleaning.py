import pandas as pd

def load_data(url: str) -> pd.DataFrame:
  return pd.read_csv(url)

# --- Cleaning columns & experimenting --- #
import pandas as pd


def load_data(url: str) -> pd.DataFrame:
    return pd.read_csv(url)


def clean_column_names(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df = df.rename(columns={"st": "state"})
    return df


def clean_gender(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["gender"] = df["gender"].replace({
        "female": "F",
        "Femal": "F",
        "Male": "M"
    })
    return df


def clean_state(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["state"] = df["state"].replace({"Arizona":"AZ","Cali": "CA", "California": "CA","Washington": "WA","Arizona": "AZ", "Nevada": "NV","Oregon": "OR"})
    return df


def clean_education(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["education"] = df["education"].replace({"Bachelors": "Bachelor"})
    return df


def clean_vehicle_class(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["vehicle_class"] = df["vehicle_class"].replace({"Sports Car": "Luxury","Luxury SUV": "Luxury","Luxury Car": "Luxury"})
    return df


def clean_customer_lifetime_value(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df["customer_lifetime_value"] = (df["customer_lifetime_value"].astype(str).str.replace("%", "", regex=False)    )
    df["customer_lifetime_value"] = pd.to_numeric(df["customer_lifetime_value"], errors="coerce")
    return df


def clean_number_of_open_complaints(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    def extract_middle_value(x):
        if pd.isna(x):
            return pd.NA
        x = str(x)
        if "/" in x:
            parts = x.split("/")
            if len(parts) >= 2:
                return parts[1]
        return x

    df["number_of_open_complaints"] = df["number_of_open_complaints"].apply(extract_middle_value)
    df["number_of_open_complaints"] = pd.to_numeric(df["number_of_open_complaints"], errors="coerce")
    return df


def handle_nulls(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()

    cat_cols = df.select_dtypes(include="object").columns.tolist()
    if "customer" in cat_cols:
        cat_cols.remove("customer")

    for col in cat_cols:
        df[col] = df[col].fillna(df[col].mode()[0])

    num_cols = df.select_dtypes(include="number").columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())

    return df


def remove_duplicates(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df = df.drop_duplicates(subset="customer", keep="first")
    df = df.reset_index(drop=True)
    return df


def convert_numeric_to_int(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    num_cols = df.select_dtypes(include="number").columns

    for col in num_cols:
        df[col] = df[col].round().astype(int)

    return df


def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    df = clean_column_names(df)
    df = clean_gender(df)
    df = clean_state(df)
    df = clean_education(df)
    df = clean_vehicle_class(df)
    df = clean_customer_lifetime_value(df)
    df = clean_number_of_open_complaints(df)
    df = handle_nulls(df)
    df = remove_duplicates(df)
    df = convert_numeric_to_int(df)
    return df


def save_data(df: pd.DataFrame, filename: str = "cleaned_data.csv") -> None:
    df.to_csv(filename, index=False)


def main():
    url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"
    df = load_data(url)
    df_clean = clean_data(df)
    save_data(df_clean)
    return df_clean


if __name__ == "__main__":
    cleaned_df = main()
    print(cleaned_df.head())
