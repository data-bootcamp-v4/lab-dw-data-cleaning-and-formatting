# fill null values in CLV with median
df["customer-lifetime-value"] = df["customer-lifetime-value"].fillna(df["customer-lifetime-value"].median())
