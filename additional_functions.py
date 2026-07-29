def cleaning_data (dataf: pd.Series) -> pd.Series:
    dataf.columns = [(column.lower()).replace(" ","_") for column in dataf.columns]
    dataf = dataf.rename(columns={"st": "state"})
    return dataf


def renaming_categorial_values (dataf: pd.Series, old_list: list, new_list: list) -> pd.Series:
    dataf = dataf.astype(str)
    dataf = dataf.replace(old_list, new_list)
    return dataf


def gender_column_cleaning (dataf: pd.Series) -> pd.Series:
    dataf = dataf.str.upper().str.strip().str[0]
    return dataf


