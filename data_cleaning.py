def main(url, output_file):
    # Your data cleaning code here
    import pandas as pd
    df = pd.read_csv(url)
    # Clean the data
    df.to_csv(output_file, index=False)
    return df
