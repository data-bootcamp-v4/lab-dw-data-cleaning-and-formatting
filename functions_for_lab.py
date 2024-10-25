# functions_for_lab
def initialize_clenaing(df):
    # Make column names in lower case, and change st for state, replace whitespace for _
    df.columns = df.columns.str.lower()
    df = df.rename(columns={"st": "state"})
    df.columns = df.columns.str.replace(" ", "_")

    # Clean gender data
    df.loc[df["gender"].str.lower().str.startswith("f", na = False), "GENDER"] = "F"
    df.loc[df["gender"].str.lower().str.startswith("m", na = False), "GENDER"] = "M"

    # Replace abvrevations in state column by their full name
    df["state"] = df["state"].replace({"AZ": "Arizona", "Cali": "California", "WA": "Washington"})
    df["education"] = df["education"].replace({"Bachelors": "Bachelor"})

    # Remove % in customer_lifetime_value
        # type(df["customer_lifetime_value"][5]) # the data is a string
    df["customer_lifetime_value"] = df["customer_lifetime_value"].str.replace("%", "")

    df["vehicle_class"] = df["vehicle_class"].replace({"Sports Car": "Luxury",
                                                    "Luxury SUV": "Luxury", 
                                                    "Luxury Car": "Luxury"})

# Handling Customer lifetime value to numeric
    df["customer_lifetime_value"] = df["customer_lifetime_value"].astype(float)

    # Handling number_of_open_complaints
    df["number_of_open_complaints"] = df["number_of_open_complaints"].str.replace(r'\d{1}\/(\d{1})\/\d{2}', r'\1', regex=True)
    return df
