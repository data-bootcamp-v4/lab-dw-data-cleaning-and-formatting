import pandas as pd

def load_data(url):
    data = pd.read_csv(url)
    data.reset_index(drop=True, inplace=True)
    data.columns = [c.lower().strip() for c in data.columns]
    return data