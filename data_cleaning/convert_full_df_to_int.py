# convert all values to int
df = df.select_dtypes(include=["number"]).astype("int")
