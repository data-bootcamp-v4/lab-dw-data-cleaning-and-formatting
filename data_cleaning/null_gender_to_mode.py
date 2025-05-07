# fill null vales in gender with mode
df["gender"] = df["gender"].fillna(df["gender"].mode()[0])
