def standardize_education(value):
    #Standardize the values in the education column all Bachelors should be 'Bachelor')
    if type(value) == str:
        return "Bachelor" if value[0].lower() == "b" else value.title()
    return value