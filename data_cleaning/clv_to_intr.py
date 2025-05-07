# covert CLV to integer
def clv_to_intr(df):
    def remove_percentage_char(value):
        if type(value) == str:
            return float(value.strip("%"))
        else:
            return value
    df["customer-lifetime-value"] = df["customer-lifetime-value"].apply(remove_percentage_char)
    return df
