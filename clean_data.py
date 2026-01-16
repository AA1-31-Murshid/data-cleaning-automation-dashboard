import pandas as pd

def clean_sales_data(input_path, output_path):
    # 1. Load
    df = pd.read_csv(input_path)
    
    # 2. Fix Dates
    # errors='coerce' turns bad dates into "NaT"
    df['transaction_date'] = pd.to_datetime(df['transaction_date'], errors='coerce')
    df = df.dropna(subset=['transaction_date']) # Remove rows with no date
    
    # 3. Fix Price (The Regex Way)
    # This removes anything that isn't a digit or a decimal point
    df['price'] = df['price'].astype(str).str.replace(r'[^\d.]', '', regex=True)
    df['price'] = pd.to_numeric(df['price'], errors='coerce').fillna(0)
    
    # 4. Standardize Categories
    df['region'] = df['region'].str.strip().str.title()
    df['region'] = df['region'].replace({'N. Tech': 'North', 'S-Region': 'South'})
    
    # 5. Deduplicate
    initial_count = len(df)
    df = df.drop_duplicates()
    print(f"Removed {initial_count - len(df)} duplicate rows.")
    
    # 6. Save
    df.to_csv(output_path, index=False)
    print(f"✅ Clean data saved to {output_path}")

if __name__ == "__main__":
    clean_sales_data('data/raw_sales_data.csv', 'data/cleaned_data.csv')