import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
import datetime as dt
import seaborn as sns
import matplotlib.pyplot as plt

# need to give encoding because old dataset (Uses UK pound)
df = pd.read_csv("data.csv", encoding='ISO-8859-1')

df.dropna(subset=['CustomerID'], inplace=True)
df = df[df['Quantity'] > 0]

df['Revenue'] = df['Quantity'] * df['UnitPrice']

df['InvoiceDate'] = pd.to_datetime(df['InvoiceDate'])

#this shows how long it's been since each customer purchased
snapshot_date = df['InvoiceDate'].max() + dt.timedelta(days=1)

# RFM table
rfm = df.groupby('CustomerID').agg({
    'InvoiceDate': lambda x: (snapshot_date - x.max()).days,
    'InvoiceNo': 'nunique',
    'Revenue': 'sum'
}).rename(columns={
    'InvoiceDate': 'Recency',
    'InvoiceNo': 'Frequency',
    'Revenue': 'Monetary'
})

scaler = StandardScaler()
rfm_scaled = scaler.fit_transform(rfm)
# Apply K-Means Clustering
kmeans = KMeans(n_clusters=4, random_state=42)
rfm['Cluster'] = kmeans.fit_predict(rfm_scaled)

# Analyze the clusters
print(rfm.groupby('Cluster').mean())
# Visualization
sns.scatterplot(data=rfm, x='Recency', y='Monetary', hue='Cluster', palette='Set2')
plt.title("Customer Segments by Recency and Monetary Value")
plt.show()


