import pandas as pd
import numpy as np
import random
from datetime import datetime, timedelta

def generate_dirty_data(rows=100):
    data = []
    regions = ['North', 'north', 'N. Tech', 'South', 'S-Region', 'West']
    products = ['Laptop', 'Mouse', 'Monitor', 'Keyboard', None]
    
    for i in range(rows):
        # 1. Date Disaster (Mixed formats and strings)
        date_choices = [
            datetime(2023, 1, 1) + timedelta(days=i),
            f"2023-{random.randint(1,12):02d}-{random.randint(1,28):02d}",
            "Jan 2023", 
            "N/A"
        ]
        date = random.choices(date_choices, weights=[70, 15, 10, 5])[0]
        
        # 2. Currency Confusion (Strings vs Numbers)
        price_choices = [
            random.uniform(100, 1500),
            f"${random.randint(100, 1500)}",
            f"{random.randint(100, 1500)}.00 USD",
            "?"
        ]
        price = random.choices(price_choices, weights=[60, 20, 15, 5])[0]
        
        # 3. Category Chaos
        region = random.choice(regions)
        product = random.choice(products)
        
        data.append([date, region, product, price])

    df = pd.DataFrame(data, columns=['transaction_date', 'region', 'product_name', 'price'])
    
    # 4. The Duplicate Ghost (Adding 5 exact duplicates)
    duplicates = df.sample(5)
    df = pd.concat([df, duplicates], ignore_index=True)
    
    # 5. Missing Values (Randomly nulling 10% of the Product Name)
    return df

# Save to CSV
dirty_df = generate_dirty_data(200)
dirty_df.to_csv('raw_sales_data.csv', index=False)
print("✅ 'raw_sales_data.csv' created with 5 intentional flaws!")
