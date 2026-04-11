def clean_column_values(df):
    """Handles specific string cleaning for CLV and Complaints."""
    # Clean Customer Lifetime Value
    if 'customer_lifetime_value' in df.columns:
        df['customer_lifetime_value'] = (
            df['customer_lifetime_value']
            .astype(str)
            .str.replace('%', '', regex=False)
            .astype(float)
        )
    
    # Clean Number of Open Complaints (extract middle value)
    if 'number_of_open_complaints' in df.columns:
        df['number_of_open_complaints'] = (
            df['number_of_open_complaints']
            .astype(str)
            .str.replace('.', '', regex=False)
            .str.split('/')
            .str[1]
            .astype(float)
        )
    return df

def handle_nulls(df):
    """Fills numeric nulls with median and categorical with mode."""
    # Numerical: Median
    num_cols = df.select_dtypes(include=['number']).columns
    for col in num_cols:
        df[col] = df[col].fillna(df[col].median())
        
    # Categorical: Mode
    cat_cols = df.select_dtypes(include=['object']).columns
    for col in cat_cols:
        if not df[col].mode().empty:
            df[col] = df[col].fillna(df[col].mode()[0])
    return df

def remove_duplicates(df):
    """Removes exact duplicate rows."""
    return df.drop_duplicates(keep='first')

def format_types(df):
    """Final cast of numeric variables to integers."""
    num_cols = df.select_dtypes(include=['number']).columns
    df[num_cols] = df[num_cols].astype(int)
    return df