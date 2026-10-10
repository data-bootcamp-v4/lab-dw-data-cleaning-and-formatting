"""EX4"""
def ex4_handle_missing(insurance_data):
    print(insurance_data.isnull())
    print(insurance_data.info())
    print(insurance_data.isna().sum())
#there are 1071 filled rows and they are all at the top. if we drop the empty lines it will be clearer.
    insurance_data=insurance_data.dropna(subset="customer")
    print(insurance_data.isnull())
    print(insurance_data.info())
    print(insurance_data.isna().sum())
#there are already 1071 filled rows. gender and customer_life_value are not totaly filled. I choose to fill the blank for the customer_life_value with the median, and the gender with "unknown"  
    median_customer_lifetime_value=insurance_data["customer_lifetime_value"].median()
    insurance_data["customer_lifetime_value"]=insurance_data["customer_lifetime_value"].fillna(median_customer_lifetime_value)
    insurance_data["gender"]=insurance_data["gender"].fillna("Unknown")
    print(insurance_data.isnull())
    print(insurance_data.info())
    print(insurance_data.isna().sum())
    return insurance_data