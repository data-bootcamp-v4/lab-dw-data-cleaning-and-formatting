import pandas as pd

def clean_columns(df_origin):
    df=df_origin.copy()
    df.columns = (df.columns
    .str.strip()
    .str.lower()
    .str.replace(" ","_")
    )
    return df

def cleaning_invalid_values(df_origin):
    df=df_origin.copy()

    df["gender"]= df["gender"].str.strip().replace({
    "Male":"M",
    "female":"F",
    "Femal":"F"
    })

    df["st"]= df["st"].str.strip().replace({
    "AZ":"Arizona",
    "Cali":"California",
    "WA":"Washington"
    })

    df.loc[df["education"]=="Bachelors",["education"]]="Bachelor"

    df["customer_lifetime_value"]= df["customer_lifetime_value"].str.strip().str.replace("%","")

    condition = df["vehicle_class"].isin([
    "Sports Car",
    "Luxury SUV",
    "Luxury Car"
    ])
    
    df.loc[condition,["vehicle_class"]]="Luxury"
    
    return df

def formatting(df_origin):
    df=df_origin.copy()
    
    df.customer_lifetime_value=df.customer_lifetime_value.map(float)
    df.number_of_open_complaints=df.number_of_open_complaints.map(lambda x : x.split("/")[1] if pd.notna(x) else x).astype("Int64")
    
    return df

def dealing_null_values(df_origin):
    df=df_origin.copy()
    
    df=df.dropna(how="all")
    df["gender"] = df["gender"].fillna("Unknown")
    # df["customer_lifetime_value"] = df["customer_lifetime_value"].fillna("Unknown")

    df[["income","monthly_premium_auto","total_claim_amount"]]=df[["income","monthly_premium_auto","total_claim_amount"]].astype(int)
    df["customer_lifetime_value"]= df["customer_lifetime_value"].map(lambda x: int(x) if pd.notna(x) else x)
    
    
    return df
