import pandas as pd
{
 "cells": [
  {
   "cell_type": "markdown",
   "id": "edba81bb",
   "metadata": {},
   "source": [
    "Functions"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "1e816a62",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Defining functions to convert all column names in lower case\n",
    "def lowercase_columns(df):\n",
    "    df.columns = df.columns.str.lower()\n",
    "    return df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "415a880e",
   "metadata": {},
   "source": [
    "def replace(df):\n",
    "    df.columns = df.columns.str.replace(\" \", \"_\")\n",
    "    return(df)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "id": "fe21ea86",
   "metadata": {},
   "outputs": [],
   "source": [
    "def rename_columns(df, columns_dict):\n",
    "    df = df.rename(columns=columns_dict)\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "aef549cb",
   "metadata": {},
   "outputs": [],
   "source": [
    "def mapping(df, column_name, value_map):\n",
    "    df[column_name] = df[column_name].map(value_map)\n",
    "    return df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "id": "5c384002",
   "metadata": {},
   "outputs": [],
   "source": [
    "def replace_column_value(df, column, column_dict):\n",
    "    df[column] = df[column].replace(column_dict)\n",
    "    return df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "id": "c100e34d",
   "metadata": {},
   "outputs": [],
   "source": [
    "def process_column(df, column_name, char_to_replace, new_type):\n",
    "    df[column_name] = df[column_name].str.replace(char_to_replace, '').astype(new_type)\n",
    "    return df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 6,
   "id": "16b367ea",
   "metadata": {},
   "outputs": [],
   "source": [
    "def split_and_select_num(df, column_name, delimiter, part_index):\n",
    "    df[column_name] = df[column_name].str.split(delimiter).str[part_index]\n",
    "    df[column_name] = pd.to_numeric(df[column_name], errors='coerce')\n",
    "    return df"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "base",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.7"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
