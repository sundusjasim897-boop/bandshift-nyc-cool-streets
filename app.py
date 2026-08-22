import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go

st.set_page_config(page_title="BandShift | NYC Cool Streets", layout="wide")

st.title("🌆 BandShift: Predictive Cool Infrastructure for New York City")
st.markdown("Physics-informed urban cooling model combining reflective blue pavements, tiered tree canopies, and high-albedo coatings.")

# District Scenario Controls
st.sidebar.header("Urban Corridor Settings (1 km²)")
pavement_area = st.sidebar.slider("Blue Road Pavement Coverage (%)", 0, 100, 70)
tree_cover = st.sidebar.slider("Canopy Coverage (Flame / Neem Trees) (%)", 0, 50, 30)
roof_albedo = st.sidebar.slider("Rooftop Albedo (Reflectance)", 0.1, 0.9, 0.85)

# Temperature Physics Model (Max capped at <= 50.0°C)
baseline_road_temp = 50.0      # Baseline road peak surface temp (°C)
baseline_sidewalk_temp = 44.0  # Baseline sidewalk surface temp (°C)
baseline_roof_temp = 48.0      # Baseline dark roof surface temp (°C)

# Temperature Drops
pavement_drop = (pavement_area / 100.0) * 10.0   # Up to 10°C drop on pavement
tree_drop = (tree_cover / 100.0) * 12.0          # Up to 12°C drop under canopy
roof_drop = ((roof_albedo - 0.1) / 0.8) * 12.0   # Up to 12°C drop on roofs

final_road_temp = baseline_road_temp - pavement_drop
final_sidewalk_temp = baseline_sidewalk_temp - tree_drop
final_roof_temp = baseline_roof_temp - roof_drop

# Energy & Comfort metrics
ac_energy_saved = (roof_drop * 1.5) + (pavement_drop * 0.4) + (tree_drop * 0.6)
utci_drop = (tree_drop * 0.45) + (pavement_drop * 0.2) + (roof_drop * 0.15)

# Metrics Display
col1, col2, col3 = st.columns(3)
col1.metric("Peak Road Surface Temp", f"{final_road_temp:.1f} °C", f"-{pavement_drop:.1f} °C")
col2.metric("Total District AC Load Saved", f"{ac_energy_saved:.1f} %", "Peak Shaved")
col3.metric("Pedestrian Comfort Improvement (UTCI)", f"-{utci_drop:.1f} °C", "Safer Walking Zone")

# Interactive Comparison Chart
st.subheader("Surface Temperature Comparison (°C)")
fig = go.Figure(data=[
    go.Bar(name='Baseline (Black Asphalt / Standard Roofs)', 
           x=['Road Surfaces', 'Sidewalk Corridors', 'Rooftops'], 
           y=[baseline_road_temp, baseline_sidewalk_temp, baseline_roof_temp],
           marker_color='#d9534f'),
    go.Bar(name='BandShift Interventions (Blue Roads + Canopies)', 
           x=['Road Surfaces', 'Sidewalk Corridors', 'Rooftops'], 
           y=[final_road_temp, final_sidewalk_temp, final_roof_temp],
           marker_color='#0275d8')
])
fig.update_layout(
    barmode='group',
    yaxis=dict(title="Surface Temperature (°C)", range=[0, 55]),
    legend=dict(orientation="h", yanchor="bottom", y=1.02, xanchor="right", x=1)
)
st.plotly_chart(fig, use_container_width=True)
