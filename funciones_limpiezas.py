import pandas as pd

def cargar_datos(url):
    df = pd.read_csv(url)
    pd.options.display.float_format = '{:,.2f}'.format
    return df

def formatear_columnas(df):
    df.columns = df.columns.str.lower().str.replace(" ", "_")
    df.rename(columns={"st": "state"}, inplace=True)
    return df

def limpiar_valores(df):
    df["state"] = df["state"].map({"Cali": "California", "AZ": "Arizona", "WA": "Washintong"}).fillna(df["state"])
    df["gender"] = df["gender"].map({"Femal": "F", "female": "F", "Male": "M"}).fillna(df["gender"])
    df["education"] = df["education"].map({"Bachelors": "Bachelor"}).fillna(df["education"])
    df["vehicle_class"] = df["vehicle_class"].map({"Sport Car": "Luxury", "Luxury SUV": "Luxury", "Luxury Car": "Luxury"}).fillna(df["vehicle_class"])
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", " ", regex=False)
    return df

def limpiar_open_complaints(df):
    df["number_of_open_complaints"] = df["number_of_open_complaints"].astype(str)
    df["number_of_open_complaints"] = df["number_of_open_complaints"].str.split('/').str[1]
    df["number_of_open_complaints"] = pd.to_numeric(df["number_of_open_complaints"], errors="coerce").astype("Int64")
    return df

def manejar_nulos(df):
    df = df.dropna(how="all")
    df["customer_lifetime_value"] = pd.to_numeric(df["customer_lifetime_value"], errors="coerce")
    df["customer_lifetime_value"] = df["customer_lifetime_value"].fillna(df["customer_lifetime_value"].median())
    df["gender"] = df["gender"].fillna(df["gender"].mode()[0])
    return df

def limpiar_income(df):
    df["income"] = df["income"].astype(str)
    df["income"] = df["income"].str.replace(",", "", regex=False)
    df["income"] = df["income"].str.replace(".", "", regex=False)
    df["income"] = pd.to_numeric(df["income"], errors="coerce")
    df["income"] = df["income"].round().astype("Int64")
    return df

def convertir_tipos(df):
    df["customer_lifetime_value"] = (df["customer_lifetime_value"].map(lambda x: float(str(x).replace(",", ""))).round().astype("Int64"))
    df["monthly_premium_auto"] = df["monthly_premium_auto"].round().astype("Int64")
    df["total_claim_amount"] = df["total_claim_amount"].round().astype("Int64")
    return df

def main(url):
    df = cargar_datos(url)
    df = formatear_columnas(df)
    df = limpiar_valores(df)
    df = limpiar_open_complaints(df)
    df = manejar_nulos(df)
    df = limpiar_income(df)
    df = convertir_tipos(df)
    return df
