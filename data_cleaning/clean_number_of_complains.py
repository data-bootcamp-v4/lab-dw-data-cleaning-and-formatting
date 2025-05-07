# convert number of complaints into inter
def clean_number_of_complains(value):
    if type(value) == str:
        return int(value.split("/")[1])
    else:
        return value

df["number-of-open-complaints"] = df["number-of-open-complaints"].apply(clean_number_of_complains)
