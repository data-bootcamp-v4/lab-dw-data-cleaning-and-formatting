"""Practica complementaria: Dealing with Dates. Asistencia de IA."""
import pandas as pd


def analyze_shootouts(source):
    data = pd.read_csv(source)
    data["date"] = pd.to_datetime(data["date"], format="%Y-%m-%d", errors="raise")
    data["month"] = data["date"].dt.month
    data["year"] = data["date"].dt.year
    monthly_counts = data.groupby(["year", "month"]).size().rename("shootouts")
    busiest = monthly_counts.loc[monthly_counts.eq(monthly_counts.max())].reset_index()
    return data, monthly_counts, busiest


if __name__ == "__main__":
    url = "https://raw.githubusercontent.com/data-bootcamp-v4/data/main/shootouts.csv"
    df, counts, busiest_periods = analyze_shootouts(url)
    print("Primera fecha:", df["date"].min())
    print("Ultima fecha:", df["date"].max())
    print("Mes y ano con mas tandas (incluidos empates):")
    print(busiest_periods.to_string(index=False))
    print(df.head().to_string(index=False))
    assert counts.sum() == len(df)
    df.to_csv("shootouts_with_dates.csv", index=False)
