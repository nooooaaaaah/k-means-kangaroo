from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler
import pandas as pd

df = pd.read_csv('fake_purchase_history.csv')

scaler = StandardScaler()
X = scaler.fit_transform(df[['Quantity', 'Price']])

kmeans = KMeans(n_clusters=3, random_state=42)

kmeans.fit(X)

labels = kmeans.labels_

df['Cluster'] = labels

df.to_csv('fake_purchase_history_clusters.csv', index=False)

print("K-means clustering complete. Results saved to 'fake_purchase_history_clusters.csv'")