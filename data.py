import pandas as pd
import numpy as np
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# Number of data points
n = 1000

categories = ['Electronics', 'Fashion', 'Home & Living', 'Beauty & Health', 'Books', 'Sports & Outdoors']

products = {
    'Electronics': ['Smartphone', 'Laptop', 'Headphones', 'Camera', 'Smartwatch'],
    'Fashion': ['Shirt', 'Dress', 'Shoes', 'Handbag', 'Sunglasses'],
    'Home & Living': ['Sofa', 'Dining Table', 'Lamp', 'Cookware', 'Bed'],
    'Beauty & Health': ['Lipstick', 'Perfume', 'Shampoo', 'Body Lotion', 'Nail Polish'],
    'Books': ['Mystery Novel', 'Science Fiction', 'Romance Novel', 'History', 'Biography'],
    'Sports & Outdoors': ['Basketball', 'Tennis Racket', 'Yoga Mat', 'Camping Tent', 'Cycling Helmet']
}

data = {
    'Product Name': [],
    'Category': [],
    'Purchase Date': [],
    'Quantity': [],
    'Price': [],
    'CustomerID': [],
    'zipcode': [],
    'discountApplied': [],
}

for _ in range(n):

    customer_id = fake.random_int(min=1000, max=9999)
    zipcode = fake.zipcode()
    num_purchases = np.random.randint(1, 6)
    for _ in range(num_purchases):
        quantity = np.random.randint(1, 6)
        price = np.round(np.random.uniform(10, 1000), 2)
        category = np.random.choice(categories)
        product_name = np.random.choice(products[category])
        purchase_date = fake.date_between_dates(date_start=datetime.now() - timedelta(days=365), date_end=datetime.now())
        discount_applied = np.random.choice([True, False])
        
        data['Product Name'].append(product_name)
        data['Category'].append(category)
        data['Purchase Date'].append(purchase_date)
        data['Quantity'].append(quantity)
        data['Price'].append(price)
        data['CustomerID'].append(customer_id)
        data['zipcode'].append(zipcode)
        data['discountApplied'].append(discount_applied)

# Make sure all arrays have the same length
length = len(data['Product Name'])
for key in data:
    if len(data[key]) != length:
        data[key] += [None] * (length - len(data[key]))

# Create a DataFrame
df = pd.DataFrame(data)

# Save the data to a CSV file
df.to_csv('fake_purchase_history.csv', index=False)

print("Fake purchase history data generated and saved to 'fake_purchase_history.csv'")