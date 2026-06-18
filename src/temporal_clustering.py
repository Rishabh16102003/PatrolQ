import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from src.preprocessing import load_temporal_features,scale_features

df=pd.read_csv('/data/cleaned_crime_records.csv')
df= df.sample(n=100000, random_state=42)

temp_features=load_temporal_features(df)
X_scaled=scale_features(temp_features)


def kmeans_temporal(df):
    kmeans_time = KMeans(n_clusters=k)
    df['time_cluster'] = kmeans_time.fit_predict(temp_features)
    sil_score = silhouette_score(X_scaled, df['time_cluster'])
    return df


