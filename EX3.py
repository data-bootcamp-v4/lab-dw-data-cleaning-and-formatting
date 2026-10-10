"""EX3"""
def ex3_fix_types(insurance_data):
    insurance_data["customer_lifetime_value"]=insurance_data["customer_lifetime_value"].astype(float)
    print(insurance_data["number_of_open_complaints"].unique())
    insurance_data["number_of_open_complaints"]=insurance_data["number_of_open_complaints"].str.split("/").str[1]
    insurance_data["number_of_open_complaints"]=insurance_data["number_of_open_complaints"].astype(float)
    print(insurance_data.dtypes)
    return insurance_data
