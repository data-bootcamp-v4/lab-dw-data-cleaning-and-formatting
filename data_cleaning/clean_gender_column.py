#clean gender column
def clean_gender_column(df):
    def gender_category(value):
        if value == "Male":
            return "M"
        elif value == "female":
            return "F"
        elif value == "Femal":
            return "F"
        else:
            return value

    df["gender"] = df["gender"].apply(gender_category)
    return df
