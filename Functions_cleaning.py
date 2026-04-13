def standarized_gender_f(gender):
    if gender in ["Femal", "female", "F"]:
        return "F"
    elif gender in ["Male", "M"]:
        return "M"
    else:
        return gender
    

def clean_column_names_f(df):
    df.columns.str.strip().str.replace('_', ' ').str.title()
    return df