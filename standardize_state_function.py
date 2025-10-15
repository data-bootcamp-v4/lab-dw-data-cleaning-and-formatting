def standardize_state(value):
    #Standardize the values in the state column (we want the full name with title case)
    if type(value) == str:
        if value[0].lower() == "a":
            return "Arizona"
        elif value[0].lower() == "c":
            return "California"
        elif value[0].lower() == "w":
            return "Washington"
        else:
            return value.title()