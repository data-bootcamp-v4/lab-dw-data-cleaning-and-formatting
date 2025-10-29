#cleaning.py — Reusable data-cleaning utilities for the customer dataset.

from __future__ import annotations

import numpy as np
import pandas as pd
from typing import Dict, Iterable, List, Optional, Tuple

def standardize_text(
    df: pd.DataFrame,
    cols: Optional[Iterable[str]] = None,
    lower: bool = True,
    strip: bool = True,
) -> pd.DataFrame:
    
    """Normalize text columns (strip spaces, set lowercase).

    Parameters
    ----------
    df : DataFrame
    cols : columns to normalize; if None, all object/string columns
    lower : convert to lowercase
    strip : strip leading/trailing whitespace

    Returns
    -------
    DataFrame (same object, modified in place style but returns df for chaining)
    """
    if cols is None:
        cols = df.select_dtypes(include=["object", "string"]).columns

    for c in cols:
        s = df[c].astype("string")
        if strip:
            s = s.str.strip()
        if lower:
            s = s.str.lower()
        df[c] = s
    return df

def drop_nulls(df: pd.DataFrame, subset: Iterable[str], verbose: bool = True) -> pd.DataFrame:
    """Drop rows where any of the subset columns are null."""
    before = len(df)
    df = df.dropna(subset=list(subset))
    after = len(df)
    if verbose:
        print(f"Dropped {before - after} rows with nulls in {list(subset)}")
    return df

def fill_categorical(df: pd.DataFrame, fill_map: Dict[str, object]) -> pd.DataFrame:
    """Fill NA values for categorical/text columns using a mapping."""
    for col, value in fill_map.items():
        df[col] = df[col].fillna(value)
    return df


def impute_mean(df: pd.DataFrame, cols: Iterable[str]) -> pd.DataFrame:
    """Impute numeric columns with their mean (ignores NA)."""
    for col in cols:
        mean_val = pd.to_numeric(df[col], errors="coerce").mean()
        df[col] = pd.to_numeric(df[col], errors="coerce").fillna(mean_val)
    return df


def round_numeric(
    df: pd.DataFrame, decimals: int = 2, cols: Optional[Iterable[str]] = None
) -> pd.DataFrame:
    """Round numeric columns to a given number of decimals."""
    if cols is None:
        cols = df.select_dtypes(include=["float64", "float32", "float16"]).columns
    df[list(cols)] = df[list(cols)].round(decimals)
    return df


def convert_float_to_Int64(
    df: pd.DataFrame,
    cols: Optional[Iterable[str]] = None,
    method: str = "round",
) -> Tuple[pd.DataFrame, Dict[str, str]]:
    
    """Convert float columns to Int64 using a specified rounding method."""

#Detecta las columnas float si no se especifican:
    if cols is None:
        cols = df.select_dtypes(include=["float64", "float32", "float16"]).columns

#Inicializa un report para guardar el resultado de cada columna:
    report: Dict[str, str] = {}

#Itera por las columnas y aplica la conversión controlando el tipo de redondeo:
    for col in cols:
        s = pd.to_numeric(df[col], errors="coerce")
        if method == "floor":  # redondea hacia abajo
            s = np.floor(s)
        elif method == "ceil": # redondea hacia arriba
            s = np.ceil(s)
        elif method == "half_up":   # 0.5 siempre arriba
            s = np.floor(s + 0.5)
        else:            # default pandas round uses bankers rounding
            s = s.round()
        try:
            df[col] = s.astype("Int64")      #Convierte a Int64, que es el tipo entero nullable de pandas (permite NA):
            report[col] = "converted to Int64"
        except Exception as e:
            report[col] = f"skipped: {e!s}"  #En caso de error, registra el motivo en el reporte
    
    return df, report #Devuelve el DataFrame modificado + el diccionario report con el resultado por columna

def detect_duplicates(
    df: pd.DataFrame, subset: Optional[Iterable[str]] = None, keep: str = "first"
) -> pd.Series:
    """Return a boolean mask of duplicated rows according to subset of columns."""
    return df.duplicated(subset=list(subset) if subset is not None else None, keep=keep)


def drop_duplicates_by(
    df: pd.DataFrame, subset: Iterable[str], keep: str = "first"
) -> pd.DataFrame:
    """Drop duplicates by a subset of columns and return the result."""
    return df.drop_duplicates(subset=list(subset), keep=keep)


"""
    def main ----> Full cleaning + formatting pipeline used in the notebook.

    Steps
    -----
    1) Drop rows with null id (customer)
    2) Standardize text (strip + lower)
    3) Fill gender with 'unknown'
    4) Impute mean for specified numeric columns
    5) Round floats to avoid micro-differences
    6) Convert selected numeric columns to nullable Int64
    7) (Optional) Drop duplicate rows by a given key

    Returns
    -------
    cleaned_df, report

    PARA EMPEZAR:

    from cleaning import main as clean_main
    cleaned_df, report = clean_main(customer_df)
    """


def main(
    df: pd.DataFrame,
    *,
    id_col: str = "customer",
    gender_col: str = "gender",
    mean_impute_cols: Optional[Iterable[str]] = ("customer_lifetime_value",),
    text_cols: Optional[Iterable[str]] = None,
    int_policy_cols: Optional[Iterable[str]] = ("income", "monthly_premium_auto", "total_claim_amount"),
    duplicate_key: Optional[Iterable[str]] = None,
    rounding_method: str = "round",
    decimal_round: int = 2,
) -> Tuple[pd.DataFrame, Dict[str, object]]:
    
    report: Dict[str, object] = {}

    # Work on a copy to avoid side-effects
    df = df.copy()

    # 1) Drop rows with null id
    before = len(df)
    df = drop_nulls(df, subset=[id_col])
    report["dropped_null_id_rows"] = before - len(df)

    # 2) Standardize text (strip + lower)
    df = standardize_text(df, cols=text_cols)

    # 3) Fill gender with 'unknown' (si existe la columna)
    if gender_col in df.columns:
        missing_before = int(df[gender_col].isna().sum())
        df[gender_col] = df[gender_col].fillna("unknown")
        report["gender_filled"] = missing_before

    # 4) Impute mean for specified numeric columns (si existen)
    actually_imputed = []
    if mean_impute_cols:
        cols_to_impute = [c for c in mean_impute_cols if c in df.columns]
        if cols_to_impute:
            df = impute_mean(df, cols_to_impute)
            actually_imputed = cols_to_impute
    report["mean_imputed_cols"] = actually_imputed

    # 5) Round floats to avoid micro-differences
    df = round_numeric(df, decimals=decimal_round)

    # 6) Convert selected numeric columns to nullable Int64
    converted_report: Dict[str, str] = {}
    if int_policy_cols:
        target_int_cols = [c for c in int_policy_cols if c in df.columns]
        if target_int_cols:
            df, converted_report = convert_float_to_Int64(
                df, cols=target_int_cols, method=rounding_method
            )
    report["int_conversion"] = converted_report

    # 7) (Optional) Drop duplicate rows by a given key
    if duplicate_key:
        key = list(duplicate_key)
        dupes_count = int(df.duplicated(subset=key, keep=False).sum())
        df = drop_duplicates_by(df, subset=key, keep="first")
        report["duplicates_removed_by_key"] = dupes_count
        report["duplicate_key_used"] = key

    # Final summary
    report["nulls_after"] = df.isnull().sum().to_dict()
    report["dtypes_after"] = df.dtypes.astype(str).to_dict()
    report["rows_final"] = len(df)

    return df, report
