def clean_clv(value):
    #Get rid of the % sign in the customer_lifetime_value column
    if type(value) == str:
        return float(value.replace("%",""))
    return value