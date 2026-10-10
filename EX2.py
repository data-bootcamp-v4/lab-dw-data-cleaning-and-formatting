"""EX2"""
def ex2_clean_categorical(insurance_data):
    print(insurance_data.dtypes)

    print(insurance_data["state"].value_counts()) # some values seems similar AZ/ Arizona ; WA/Washington ; Cali/california
    print(insurance_data["gender"].value_counts()) # Some values are similar F/female/Femal ; Male/M
    print(insurance_data["education"].value_counts()) # Some values are similar Bachelor/Bachelors
    print(insurance_data["vehicle_class"].value_counts()) # Some values are similar Bachelor/Bachelors


    gender_map={"F":"F", "M":"M", "Femal":"F", "Male":"M", "female":"F"}
    state_map={"Oregon":"Oregon","California":"California","Arizona":"Arizona","Cali":"California","Nevada":"Nevada","Washington":"Washington","WA":"Washington","AZ":"Arizona"}
    education_map={"Bachelors":"Bachelor","Bachelor":"Bachelor","College":"College","High School or Below":"High School or Below","Master":"Master","Doctor":"Doctor"}

    vehicle_map= {"Sports Car":"Luxury", "Luxury SUV":"Luxury", "Luxury Car":"Luxury","Four-Door Car":"Four-Door Car","Two-Door Car":"Two-Door Car","SUV":"SUV"}
    insurance_data["gender"]=insurance_data["gender"].map(gender_map)
    insurance_data["state"]=insurance_data["state"].map(state_map)
    insurance_data["education"]=insurance_data["education"].map(education_map)
    insurance_data["customer_lifetime_value"] = (insurance_data["customer_lifetime_value"].str.replace("%", "", regex=False))
    insurance_data["vehicle_class"]=insurance_data["vehicle_class"].map(vehicle_map)
    return insurance_data

