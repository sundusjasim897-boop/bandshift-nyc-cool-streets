# BandShift: Predictive Cool Infrastructure for New York City

> **FortyGuard Hackathon 2026 Submission**  
> An evidence-based urban microclimate and cooling framework adapting proven global cooling solutions—high-albedo blue pavements and tiered urban canopy shading—to eliminate urban heat stress in New York City.

---

## 🌆 Overview & Problem Statement
During summer heatwaves, dark asphalt roadways and conventional building surfaces in dense city corridors reach peak temperatures of **45–50°C**, amplifying urban heat island effects and driving heavy air conditioning loads.

**BandShift** provides a practical, low-cost roadmap for retrofitting urban blocks:
1. **Solar-Reflective Blue Roads:** Inspired by high-albedo road trials, reducing road surface temperatures by **7–10°C** ($6–$15/m²).
2. **Tiered Urban Canopy Shading:** 
   - **Wide / Luxury Corridors:** Broad umbrella canopies (10–15 m spread) providing direct shade and dropping surface temperatures by **10–12°C**.
   - **Budget-Friendly Districts:** Resilient, fast-growing trees (e.g., Neem/hardy broadleaf) delivering massive shade coverage at minimal cost.
3. **Integrated Energy & Comfort:** Yields up to **25–35% building cooling energy reduction** and improves pedestrian thermal comfort indices (UTCI).

---

## 📊 Performance Matrix (1 km² Demonstration District)

| Intervention Layer | Baseline Surface Temp | Target Surface Temp | Pedestrian UTCI Shift | Est. Cost |
| :--- | :--- | :--- | :--- | :--- |
| **Cool Blue Pavements** | $50.0^\circ\text{C}$ | $40.0–43.0^\circ\text{C}$ | $-1.5^\circ\text{C to } -2.0^\circ\text{C}$ | $\sim\$6–\$15/\text{m}^2$ |
| **Cool Roofs ($\alpha = 0.85$)** | $48.0^\circ\text{C}$ | $36.0–40.0^\circ\text{C}$ | $-1.0^\circ\text{C to } -1.5^\circ\text{C}$ | $\sim\$5–\$10/\text{m}^2$ |
| **Canopy Shading (Trees)** | $44.0^\circ\text{C}$ | $32.0–35.0^\circ\text{C}$ | $-3.0^\circ\text{C to } -5.0^\circ\text{C}$ | $\sim\$200–\$500/\text{tree}$ |
| **Integrated System** | **$\le 50.0^\circ\text{C}$** | **$34.0–38.0^\circ\text{C}$** | **$-5.0^\circ\text{C to } -7.0^\circ\text{C}$** | **High Net Energy ROI** |

---

## 🛠️ Architecture & Methods
- **Microclimate Simulation:** Multi-surface radiation balancing and albedo reflection modeling.
- **Urban Thermal Indices:** Evaluating Mean Radiant Temperature ($T_{\text{mrt}}$) and Universal Thermal Climate Index (UTCI).
- **Data Integration:** Designed for integration with the FortyGuard Temperature API for live thermal telemetry.

---

## 🚀 Quickstart & Local Setup

```bash
# 1. Install dependencies
python -m pip install streamlit pandas numpy plotly requests

# 2. Run the interactive dashboard
python -m streamlit run app.py
