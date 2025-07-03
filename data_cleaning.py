import pandas as pd
import re

#changing column name to snake casing
def to_snake_casing(list_of_cols):
    result = []
    for col in list_of_cols:
        if col.isupper():
            result.append(col.lower())
        else:
            new_col = re.sub(r'(?<!^)(?=[A-Z])', '_', col).replace(" ","").lower()
            result.append(new_col)
    return result

def clean_gender(gender_series):
    return gender_series.str.strip().str.lower().replace({
        r'^f(emal?e?)?$': 'F',
        r'^m(al?e?)?$': 'M'
    }, regex=True)
