# app.py
from shapely.geometry import MultiPoint
import geopandas as gpd
import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import json

# ---------------------------------------------------
# PAGE CONFIG
# ---------------------------------------------------

st.set_page_config(
    page_title="Crime Intelligence Dashboard",
    layout="wide"
)

st.title("🚔 Crime Intelligence Dashboard")

# ---------------------------------------------------
# LOAD DATA
# ---------------------------------------------------

@st.cache_data
def load_data():
    df=pd.read_csv('data/visualize.csv')
    return df

df = load_data()

# ---------------------------------------------------
# SIDEBAR FILTERS
# ---------------------------------------------------

# st.sidebar.header("Filters")

# crime_types = st.sidebar.multiselect(
#     "Select Crime Type",
#     options=df["Primary Type"].unique(),
#     default=df["Primary Type"].unique()
# )

# selected_year = st.sidebar.slider(
#     "Select Year",
#     int(df["Year"].min()),
#     int(df["Year"].max()),
#     int(df["Year"].max())
# )

# df = df
# df[
#     (df["Primary Type"].isin(crime_types)) &
#     (df["Year"] == selected_year)
# ]

# ---------------------------------------------------
# KPI SECTION
# ---------------------------------------------------

total_crimes = len(df)

arrests = df["Arrest"].sum()

domestic_cases = df["Domestic"].sum()

crime_types_count = df["Primary Type"].nunique()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Crimes", f"{total_crimes:,}")
col2.metric("Total Arrests", f"{arrests:,}")
col3.metric("Domestic Cases", f"{domestic_cases:,}")
col4.metric("Crime Categories", crime_types_count)

st.divider()

# ---------------------------------------------------
# CHOROPLETH MAPBOX
# ---------------------------------------------------

st.subheader("🗺 Crime Zone Choropleth Map")

# GeoJSON File
# with open("data/crime_hotspots.geojson") as f:
#     geojson = json.load(f)

# Aggregate crime count by zone
polygons = []

for cluster_id, group in df[df['cluster'] != -1].groupby('cluster'):
    points = list(zip(group['Longitude'], group['Latitude']))
    
    if len(points) > 2:
        hull = MultiPoint(points).convex_hull
        polygons.append({
            'cluster': cluster_id,
            'size': len(points),
            'geometry': hull
        })

gdf = gpd.GeoDataFrame(polygons, crs="EPSG:4326")
geojson = gdf.__geo_interface__

fig_map = px.choropleth_mapbox(
    gdf,
    geojson=geojson,
    locations=gdf.index,
    color='size',
    color_continuous_scale=["green", "yellow", "red"],  # 🔥 your requirement
    mapbox_style="open-street-map",
    center={
        "lat": df["Latitude"].mean(),
        "lon": df["Longitude"].mean()
    },
    zoom=9,
    opacity=0.5
)

fig_map.update_layout(
    margin=dict(l=0, r=0, t=0, b=0),
    height=450,
)

list_district=df[(df['cluster']==(df['cluster']
    .value_counts().reset_index()
    .index[0]))]['District'].unique()



st.plotly_chart(fig_map, use_container_width=True)
st.markdown(
    f"<h4 style='color:#FF0000;'font-size:20px;'>NOTE-: Districts Having high Crime Density{list_district}</h4>",
    unsafe_allow_html=True
)

st.divider()

# ---------------------------------------------------
# SEABORN HEATMAP
# ---------------------------------------------------

st.subheader("🔥 Crime Heatmap by Hour and day")
col1,col2=st.columns(2)
with col1:
    heatmap_data = df.pivot_table(index='hour',
                columns='time_cluster', aggfunc='size',
                fill_value=0)

    fig, ax = plt.subplots(figsize=(14,9))

    sns.heatmap(
        heatmap_data,
        cmap="Reds",
        annot=False,
        linewidths=0.5,
        ax=ax
    )

    ax.set_title("Crime Frequency by Hour Heatmap")

    st.pyplot(fig)

    st.markdown(
    f"<h4 style='color:#FF0000;'font-size:20px;'>from 4pm till 12am Crime Rate is high </h4>",
    unsafe_allow_html=True
)
with col2:

# ---------------------------------------------------
# TOP CRIME TYPES
# ---------------------------------------------------

    st.subheader("📊 Top Crime Types")

    crime_chart = (
        df["Primary Type"]
        .value_counts()
        .head(10)
        .reset_index()
    )

    crime_chart.columns = ["Crime Type", "Count"]

    fig_bar = px.bar(
        crime_chart,
        x="Crime Type",
        y="Count",
        color="Count",
        text_auto=True
    )


    st.plotly_chart(fig_bar, use_container_width=True)
st.divider()
# ---------------------------------------------------
# RAW DATA
# ---------------------------------------------------
col1,col2=st.columns(2)
with col1:
    st.subheader("🚔 Proportion of Arrests")

    colors = ['#ff9999', '#66b3ff']
    explode = (0, 0.1)

    fig, ax = plt.subplots(figsize=(12, 8))

    ax.pie(
        df['Arrest'].value_counts().values,
        explode=explode,
        labels=df['Arrest'].value_counts().index,
        colors=colors,
        autopct='%1.1f%%',
        shadow=True,
        startangle=140
    )

    ax.set_title('Proportion of Arrests')
    ax.axis('equal')

    st.pyplot(fig)
    st.markdown(
    "<h4 style='color:#FF0000;'font-size:20px;'>Low Arrest Percentage is the clear" \
    "reason of high Crime rate</h4>",
    unsafe_allow_html=True
    )

with col2:
    st.subheader("Season-wise Crime Distribution🚔")
    # Create figure
    fig, ax = plt.subplots(figsize=(12,8))

    # Title
    ax.set_title(
        'Season-Wise Crime Distribution',
        fontsize=18,
        color='#1E3A8A'
    )

    # Countplot
    sns.countplot(
        y=df['season'],
        order=df['season'].value_counts().index,
        palette='coolwarm',
        ax=ax
    )

    # Axis labels
    ax.set_xlabel('Crime Count', fontsize=14)
    ax.set_ylabel('Season', fontsize=14)

    # Display in Streamlit
    st.pyplot(fig)
    st.markdown(
    "<h4 style='color:#FF0000;'font-size:20px;'>Season-wise Crime is evenly distributed"
    ",But in winter's crime rate is a bit less</h4>",
    unsafe_allow_html=True
    )

with st.expander("View Raw Data"):
    st.dataframe(df)