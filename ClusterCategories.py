import pandas as pd

df = pd.read_csv('fake_purchase_history_clusters.csv')

cluster_2 = df[df['Cluster'] == 2]

categories = cluster_2['Category'].unique()

print("Product categories in cluster 2:")
print(categories)