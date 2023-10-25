import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker
fake = Faker()

# Number of data points
n = 1000

# Generate fake product categories
categories = ['Electronics', 'Fashion', 'Home & Living', 'Beauty & Health', 'Books', 'Sports & Outdoors']

# Generate fake product names for each category
products = {
    'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Camera', 'Smartwatch'],
    'Fashion': ['Shirt', 'Dress', 'Shoes', 'Handbag', 'Sunglasses'],
    'Home & Living': ['Sofa', 'Dining Table', 'Lamp', 'Cookware', 'Bed'],
    'Beauty & Health': ['Lipstick', 'Perfume', 'Shampoo', 'Body Lotion', 'Nail Polish'],
    'Books': ['Mystery Novel', 'Science Fiction', 'Romance Novel', 'History', 'Biography'],
    'Sports & Outdoors': ['Basketball', 'Tennis Racket', 'Yoga Mat', 'Camping Tent', 'Cycling Helmet']
}

# Generate random data
data = {
    'Product Name': [],
    'Category': [],
    'Purchase Date': [],
    'Quantity': [],
    'Price': []
}

for _ in range(n):
    category = np.random.choice(categories)
    product_name = np.random.choice(products[category])
    purchase_date = fake.date_between_dates(date_start=datetime.now() - timedelta(days=365), date_end=datetime.now())
    quantity = np.random.randint(1, 6)
    price = np.round(np.random.uniform(10, 1000), 2)
    
    data['Product Name'].append(product_name)
    data['Category'].append(category)
    data['Purchase Date'].append(purchase_date)
    data['Quantity'].append(quantity)
    data['Price'].append(price)

# Create a DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv('fake_purchase_history.csv', index=False)

print("Fake purchase history data generated and saved to 'fake_purchase_history.csv'")
