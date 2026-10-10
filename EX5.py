"""EX5"""
def ex5_remove_duplicates(insurance_data):
    dupl = insurance_data.duplicated()
    print("Number of duplicated rows:", dupl.sum())


    print("Rows before:", len(insurance_data))
    insurance_data_no_duplicates = insurance_data.drop_duplicates(subset=["customer"],keep="first")
    print("Rows after:", len(insurance_data_no_duplicates))
#It seems there is no duplicate
    return insurance_data