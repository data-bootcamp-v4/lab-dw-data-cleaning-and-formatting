def standardize_vehicle_classes(value):
    #Merge "Sport Cars", "Luxury SUV" and "Luxury Car" into just "Luxury"
    if type(value) == str:
        if value in ["Sports Car", "Luxury SUV", "Luxury Car"]:
            return "Luxury"
    return value