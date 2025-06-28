def column_names_underscore_lowercase(df):
    df = df.copy()  # optional, if you want to avoid changing the original
    df.columns = [
        col.replace(" ", "_").lower().replace("st", "state") if col.lower() == "st" else col.replace(" ", "_").lower()
        for col in df.columns
    ]
    return df
