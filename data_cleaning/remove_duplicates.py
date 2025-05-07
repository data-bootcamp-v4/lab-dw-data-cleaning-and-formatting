# remove duplicates & save them in a new file
df_duplicates = df.copy()

df_duplicates.drop_duplicates(keep = "first")

df_duplicates.to_csv("./data/df_duplicates_lab.csv")
