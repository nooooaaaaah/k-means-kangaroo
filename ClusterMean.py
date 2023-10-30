import pandas as pd

df = pd.read_csv('fake_purchase_history_clusters.csv')

cluster_means = df.groupby('Cluster')[['Quantity', 'Price']].mean()

overall_means = df[['Quantity', 'Price']].mean()

# Print the mean values for each cluster and the overall dataset
print("Cluster means:")
print(cluster_means)
print("\nOverall means:")
print(overall_means)