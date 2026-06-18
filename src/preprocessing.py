import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler

def data_cleaning(df):
    df=df.dropna(subset=['X Coordinate'])# This will drop all null values of coordinates of y as well
    df=df.dropna(subset=['Ward'])
    df=df.dropna(subset=['Community Area'])
    df=df.dropna(subset=['Location Description'])
    #conver date-time column to proper date-time data type
    df['Date'] = pd.to_datetime(df['Date'])
    df['hour'] = df['Date'].dt.hour
    df['day'] = df['Date'].dt.day_name()
    df['month'] = df['Date'].dt.month
    df['year'] = df['Date'].dt.year
    df['weekend'] = df['Date'].dt.dayofweek >= 5
    #only required columns selected 
    cols = [
    'ID','Date','Primary Type','Description',
    'Location Description','Arrest','Domestic',
    'District','Ward','Community Area',
    'Latitude','Longitude'
    ]

    df = df[cols]
    return df

def load_temporal_features(df):
    day_map={
        'Sunday':0,
        'Monday':1,
        'Tuesday':2,
        'Wednesday':3,
        'Thursday':4,
        'Friday':5,
        'Saturday':6,
    }
    df['day']=df['day'].replace(day_map)
    temp_features = df[['hour', 'day', 'month']]
    return temp_features

def scale_features(temp_features):
    X = temp_features
    X = X.astype('float32')

    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(X)
    return X_scaled

