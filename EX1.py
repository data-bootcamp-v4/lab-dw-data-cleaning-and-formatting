import pandas as pd

def ex1_load_data(url ="https://raw.githubusercontent.com/data-bootcamp-v4/data/main/file1.csv"):
    insurance_data = pd.read_csv(url)
    insurance_data.columns = (insurance_data.columns.str.strip().str.lower().str.replace(" ", "_"))
    insurance_data = insurance_data.rename(columns={"st": "state"})
    return insurance_data