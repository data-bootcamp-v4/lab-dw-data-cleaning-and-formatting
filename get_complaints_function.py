def get_complaints(value):
    #Split the values in the number_of_open_complaints column to get only the number in the middle
    if type(value) == str:
        return int(value.split("/")[1])
    return value