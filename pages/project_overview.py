import streamlit as st


# st.image(
#     "https://images.unsplash.com/photo-1516321497487-e288fb19713f",
#     use_container_width=True
# )

st.set_page_config(
    page_title="PatrolIQ - Project Description",
    page_icon="🚔",
    layout="wide"
)

st.title("🚔 PatrolIQ - Smart Safety Analytics Platform")

st.markdown("---")

st.markdown("""
## 📖 Project Overview

**PatrolIQ** is an AI-powered Urban Safety Intelligence Platform developed to analyze large-scale crime data and support data-driven decision-making for law enforcement agencies.

The platform processes **500,000 crime records** sampled from the **Chicago Crime Dataset** and applies **Unsupervised Machine Learning techniques** to uncover crime hotspots, temporal crime patterns, and high-risk regions across the city.

The objective is to transform raw crime data into actionable intelligence that helps police departments optimize patrol deployment, improve resource allocation, and enhance public safety.
""")

st.markdown("---")

st.subheader("🎯 Project Objectives")

st.markdown("""
- Identify geographic crime hotspots across Chicago.
- Discover temporal crime patterns such as peak crime hours and seasonal trends.
- Compare multiple clustering algorithms for hotspot detection.
- Visualize complex crime patterns using dimensionality reduction techniques.
- Track machine learning experiments using MLflow.
- Deploy an interactive Streamlit application for crime intelligence analysis.
""")

st.markdown("---")

st.subheader("🧠 Machine Learning Techniques Used")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    **Clustering Algorithms**
    
    • K-Means Clustering
    
    • DBSCAN
    
    • Hierarchical Clustering
    """)

with col2:
    st.success("""
    **Dimensionality Reduction**
    
    • PCA (Principal Component Analysis)
    
    • UMAP
    
    • t-SNE
    """)

st.markdown("---")

st.subheader("📊 Dataset Information")

st.table({
    "Feature": [
        "Data Source",
        "Total Available Records",
        "Records Used",
        "Input Features",
        "Crime Categories",
        "Geographic Features",
        "Temporal Features"
    ],
    "Details": [
        "Chicago Crime Dataset",
        "7.8 Million+",
        "500,000",
        "22+ Variables",
        "33 Crime Types",
        "Latitude, Longitude, District, Ward",
        "Hour, Day, Month, Season"
    ]
})

st.markdown("---")

st.subheader("⚠️ PCA Analysis & Dimensionality Reduction Findings")

st.warning("""
### Important Observation

The project requirements suggested reducing the dataset into **2–3 principal components**
while retaining approximately **70% of the original variance**.

However, after performing PCA analysis, it was observed that:

• Retaining **70%+ variance required approximately 5–6 principal components**

• Restricting PCA to only **2 or 3 components caused significant information loss**

• Since 5–6 dimensions are difficult to visualize effectively, PCA did not provide a
simple and meaningful low-dimensional representation suitable for interpretation

Therefore, PCA was used primarily for variance analysis and feature contribution
understanding rather than final visualization.
""")

st.success("""
**Alternative Approach Used**

To achieve meaningful visualization of complex crime patterns,
UMAP and t-SNE were utilized because they provide better 2D representations
of high-dimensional crime data and reveal cluster structures more effectively.
""")

st.markdown("---")

st.subheader("📈 Key Outcomes")

st.markdown("""
✅ Identified high-crime geographic zones

✅ Detected peak crime hours and seasonal patterns

✅ Compared clustering algorithms using evaluation metrics

✅ Built interactive crime intelligence dashboards

✅ Implemented MLflow experiment tracking

✅ Developed a production-ready Streamlit application
""")

st.markdown("---")

st.subheader("💡 Business Impact")

st.markdown("""
The PatrolIQ platform can assist:

### 🚓 Police Departments
- Optimize patrol route allocation
- Improve response time
- Identify high-risk areas
- Support proactive policing strategies

### 🏙️ City Administration
- Enable data-driven urban planning
- Improve public safety initiatives
- Support strategic resource allocation

### 🚑 Emergency Response Teams
- Prioritize emergency deployments
- Improve situational awareness
- Coordinate multi-agency response efforts
""")

st.markdown("---")

st.info("""
**PatrolIQ combines crime analytics, machine learning, and interactive visualization
to transform large-scale crime datasets into actionable public safety intelligence.**
""")