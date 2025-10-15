def standardize_gender(value):
    #Standardize the values in the gender column
    if type(value) == str:
        if value[0].lower() == "m":
            return "M"
        else:
            return "F"