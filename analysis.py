import pandas as pd
from data_cleaning import main

def analyze_data():
    # Load and clean the data
    df = main()

    # Review statistics for total claim amount and customer lifetime value
    print("Statistics for total claim amount:")
    print(df['total_claim_amount'].describe())
    print("\nStatistics for customer lifetime value:")
    print(df['customer_lifetime_value'].describe())

    # Identify customers with high policy claim amount and low customer lifetime value
    high_claim_threshold = df['total_claim_amount'].quantile(0.75)
    low_clv_threshold = df['customer_lifetime_value'].quantile(0.25)

    high_claim_low_clv_df = df[
        (df['total_claim_amount'] > high_claim_threshold) &
        (df['customer_lifetime_value'] < low_clv_threshold)
    ]

    # Calculate summary statistics for the high claim and low CLV data
    summary_stats = high_claim_low_clv_df[['total_claim_amount', 'customer_lifetime_value']].describe()
    print("\nSummary statistics for high claim amount and low customer lifetime value:")
    print(summary_stats)

    # Save the filtered data to a new CSV file
    high_claim_low_clv_df.to_csv('high_claim_low_clv_customers.csv', index=False)

if __name__ == "__main__":
    analyze_data()