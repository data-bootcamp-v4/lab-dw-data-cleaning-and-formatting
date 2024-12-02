def insurance_df_cleaner(df):
    
    df.columns = [column.lower().replace(" ", "_") for column in df.columns]
    df = df.rename(columns = {"st": "state"})
    df.gender = df.gender.replace("Femal", "F").replace("Male", "M").replace("female", "F")
    df.state = df.state.replace("AZ", "Arizona").replace("Cali", "California").replace("WA", "Washington")
    df.education = df.education.replace("Bachelors", "Bachelor")
    df.customer_lifetime_value = df.customer_lifetime_value.str.replace('%', '').astype(float)
    df.vehicle_class = df.vehicle_class.replace(["Sports Car", "Luxury SUV", "Luxury Car"], "Luxury")
    df.dropna(how='all', inplace=True)
    df.customer_lifetime_value.fillna((df[(df['policy_type'] == 'Personal Auto') & (df['vehicle_class'] == 'Four-Door Car')]['customer_lifetime_value'].mean()), inplace=True)
    df.customer_lifetime_value = df.customer_lifetime_value.astype(int)
    df.number_of_open_complaints = df.number_of_open_complaints.apply(lambda x: x.split("/")[1])
    df.number_of_open_complaints = df.number_of_open_complaints.astype(int)
    df.dropna(how='all', inplace=True)
    df.gender = df.gender.bfill()
    df.income = df.income.astype(int)
    df.monthly_premium_auto = df.monthly_premium_auto.astype(int)
    df.total_claim_amount = df.total_claim_amount.astype(int)
    return df