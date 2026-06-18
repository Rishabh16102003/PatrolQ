# 🚔 PatrolIQ: Crime Intelligence & Hotspot Detection System

## 📌 Project Overview

PatrolIQ is an end-to-end Crime Intelligence and Hotspot Detection System developed to analyze large-scale crime data, identify crime-prone regions, discover spatial crime patterns, and support data-driven policing strategies.

The system combines Exploratory Data Analysis (EDA), Geospatial Analytics, Clustering Algorithms, Temporal Analysis, and Interactive Visualizations to transform raw crime records into actionable intelligence.

---

## 🎯 Objectives

* Analyze historical crime records.
* Identify high-risk crime hotspots.
* Discover hidden crime clusters using unsupervised learning.
* Understand temporal crime trends.
* Support strategic resource allocation and patrol planning.
* Provide interactive visualizations for crime intelligence.

---

## 📊 Dataset

**Source:** Chicago Crime Dataset (2001–Present)

The dataset contains historical crime incidents including:

* Crime Type
* Date & Time
* Geographic Coordinates
* Arrest Information
* Domestic Crime Indicator
* Community Areas
* Police Districts
* Crime Location Details

After preprocessing, relevant features were selected for spatial and temporal crime analysis.

---

## ⚙️ Project Workflow

### 1. Data Collection

* Imported crime records dataset.
* Selected relevant attributes.
* Removed redundant information.

### 2. Data Preprocessing

* Missing value treatment.
* Duplicate removal.
* Feature engineering.
* Date and time extraction.
* Geospatial data preparation.

### 3. Exploratory Data Analysis (EDA)

Analysis performed on:

* Crime distribution
* Most frequent crime categories
* Crime frequency by district
* Monthly crime trends
* Hourly crime patterns
* Arrest statistics

---

### 4. Spatial Hotspot Detection

Crime hotspots were identified using clustering techniques.

Methods used:

* DBSCAN (Density-Based Spatial Clustering)
* Spatial coordinate analysis
* Geographical hotspot visualization

Outputs:

* High-density crime zones
* Noise/outlier detection
* Crime hotspot maps

---

### 5. Dimensionality Reduction Analysis

Principal Component Analysis (PCA) was evaluated to reduce feature dimensions and visualize crime patterns.

**Observation:**

Dimensionality reduction was not adopted because:

* To retain approximately 70% variance, PCA required 5–6 principal components.
* Such high-dimensional representation does not provide meaningful 2D visual interpretation.
* Therefore, original feature space was retained to preserve information and interpretability.

---

### 6. Temporal Crime Analysis

Temporal analysis was performed to understand:

* Crime trends over time
* Seasonal crime patterns
* Monthly variations
* Peak crime hours
* Weekday vs weekend crime behavior

This helps identify when crimes are most likely to occur.

---

### 7. Crime Cluster Intelligence

The clustering pipeline enables:

* Hotspot identification
* Cluster-based crime profiling
* Region-wise crime pattern discovery
* Patrol prioritization support

---

## 🛠️ Technologies Used

### Programming Language

* Python

### Data Processing

* Pandas
* NumPy

### Visualization

* Matplotlib
* Plotly
* Folium
* Streamlit

### Machine Learning

* Scikit-Learn
* DBSCAN
* PCA

### Geospatial Analysis

* GeoJSON
* Latitude/Longitude Processing

---

## 📂 Project Structure

```text
PATROLIQ/
│
├── dashboard.py
├── requirements.txt
│
├── data/
│   ├── cleaned_crime_records.csv
│   ├── clustered_data.csv
│   ├── crime_hotspots.geojson
│   └── visualize.csv
│
├── pages/
│   └── project_overview.py
│
├── src/
│   ├── preprocessing.py
│   ├── clustering.py
│   └── temporal_clustering.py
│
└── notebooks/
    ├── eda.ipynb
    ├── preprocess.ipynb
    ├── dbscan.ipynb
    ├── clustering.ipynb
    └── dimensionality_reduction.ipynb
```

---

## 🚀 Streamlit Dashboard Features

### Dashboard Modules

✅ Project Overview

✅ Crime Data Exploration

✅ Hotspot Detection

✅ Crime Cluster Visualization

✅ Temporal Crime Analysis

✅ Interactive Maps

### Interactive Components

* Crime hotspot maps
* Cluster visualizations
* Trend analysis charts
* Geospatial exploration tools

---

## 📈 Key Insights

* Crime incidents are concentrated in specific geographical regions.
* Density-based clustering effectively identifies crime hotspots.
* Certain time periods exhibit significantly higher crime frequency.
* PCA-based dimensionality reduction was not suitable due to high variance retention requirements.
* Geospatial analytics provides actionable intelligence for patrol planning.

---

## 🔮 Future Enhancements

* Real-time crime monitoring
* Predictive crime hotspot forecasting
* Advanced anomaly detection
* Deep learning-based crime prediction
* Police resource optimization
* Crime severity risk scoring

---

## 👨‍💻 Author

**Rishabh Singh**

Data Science | Machine Learning | Geospatial Analytics

---

## 📜 License

This project is developed for educational and research purposes.
