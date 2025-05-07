# clean column names
import pandas as pd

df.columns = [column.lower().replace(" ","-").replace("ST","state") for column in df.columns]
