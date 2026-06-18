import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.cluster import DBSCAN
from sklearn.neighbors import kneighbors_graph
from sklearn.cluster import AgglomerativeClustering


df=pd.read_csv('data/cleaned_crime_records.csv')
df=df.sample(n=150000, random_state=42)



X = df[['Latitude','Longitude']]
X = X.astype('float32')

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

def kmeans(k,X_scaled,df):
    kmeans = KMeans(n_clusters=k, random_state=42)
    df['cluster'] = kmeans.fit_predict(X_scaled)
    sil_score=silhouette_score(X_scaled, df['cluster'])
    return df,sil_score

def dbscan(X_scaled,df):
    db = DBSCAN(eps=0.2, min_samples=150, algorithm='kd_tree', n_jobs=-1)
    df['cluster']=db.fit_predict(X_scaled)
    sil_score = silhouette_score(X_scaled, df['cluster'])
    return df,sil_score

def agglomerative(X_scaled,df):
    connectivity = kneighbors_graph(X_scaled, n_neighbors=10, include_self=False, n_jobs=-1)
    model = AgglomerativeClustering(n_clusters=8, connectivity=connectivity, linkage='ward')
    df['cluster'] = model.fit_predict(X_scaled)
    sil_score=silhouette_score(X_scaled,df['cluster'])
    return df,sil_score

kmeans_df,kmeans_score=kmeans(7,X_scaled,df)
db_df,db_score=dbscan(X_scaled,df)
agg_df,agg_score=agglomerative(X_scaled,df)

if kmeans_score>db_score and kmeans_score>agg_score:
    df=kmeans_df
elif db_score>kmeans_score and db_score>agg_score:
    df=db_df
else:
    df=agg_df




