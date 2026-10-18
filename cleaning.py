
def format_data(df):
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "").astype(float)

    df["number_of_open_complaints"] = df["number_of_open_complaints"].str.split("/").str[1].astype("Int64")

    return df


def clean_nulls(df):
    df = df.dropna()

    return df

def clean_duplicates(df):
    df = df.drop_duplicates()
    df = df.reset_index(drop=True)

    return df

def format_integers(df):
    df["customer_lifetime_value"] = df["customer_lifetime_value"].astype(int)
    df["income"] = df["income"].astype(int)
    df["monthly_premium_auto"] = df["monthly_premium_auto"].astype(int)
    df["total_claim_amount"] = df["total_claim_amount"].astype(int)

    return df

def main():
    import pandas as pd

    df = pd.read_csv("https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv")

    df = df.rename(columns={
        "Customer": "customer",
        "ST": "state",
        "GENDER": "gender",
        "Education": "education",
        "Customer Lifetime Value": "customer_lifetime_value",
        "Income": "income",
        "Monthly Premium Auto": "monthly_premium_auto",
        "Number of Open Complaints": "number_of_open_complaints",
        "Policy Type": "policy_type",
        "Vehicle Class": "vehicle_class",
        "Total Claim Amount": "total_claim_amount"
    })

    df = format_data(df)
    df = clean_nulls(df)
    df = format_integers(df)
    df = clean_duplicates(df)

    return df
