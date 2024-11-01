def rename_columns(data, columns_map):
    data.rename(columns=columns_map, inplace=True)

def replace_values(data, column, replacements):
    data[column].replace(replacements, inplace=True)