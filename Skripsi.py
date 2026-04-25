import streamlit as st
import pandas as pd
import numpy as np
import joblib
import os
from sklearn.base import BaseEstimator, RegressorMixin

# import modul nutrisi (hasil refactor)
from nutrition import get_nutrition_plan


# FIX UNTUK JOBLIB (WAJIB)

def fwd_log(y):
    return np.log(np.asarray(y, float))

def inv_exp(yt):
    return np.exp(np.asarray(yt, float))


class TransformedTargetEstimator(BaseEstimator, RegressorMixin):
    def __init__(self, regressor, fwd=None, inv=None):
        self.regressor, self.fwd, self.inv = regressor, fwd, inv

    def predict(self, X):
        y_pred_t = self.regressor_.predict(X)
        return np.asarray(self.inv(y_pred_t) if self.inv else y_pred_t, dtype=float)


# FUNGSI TRAIL RUN


def calculate_km_effort(distance_km, elevation_gain_m):
    return distance_km + (elevation_gain_m / 100)


def categorize_race(km_effort):
    if km_effort < 42:
        return "Short Trail"
    elif km_effort < 75:
        return "50K"
    elif km_effort < 120:
        return "100K"
    else:
        return "100M"


def format_time(hours_float):
    jam = int(hours_float)
    menit = int((hours_float - jam) * 60)
    return jam, menit


# CONFIG PAGE

st.set_page_config(
    page_title="Trail Running Predictor",
    page_icon="🏃",
    layout="wide"
)

st.title("🏃 Trail Running Finish Time Predictor")
st.markdown("""
Prediksi waktu finis trail running berbasis machine learning.

Fitur:
- Distance & Elevation
- Auto kategori (KM Effort)
- Prediksi waktu
- Rekomendasi nutrisi berbasis research
""")


# LOAD MODEL

MODEL_PATH = "output_Skripsi_Final_Lengkap/Model_D_90_10.pkl"


@st.cache_resource
def load_model():
    if os.path.exists(MODEL_PATH):
        return joblib.load(MODEL_PATH)
    return None


model = load_model()

if model is None:
    st.error(f"❌ Model tidak ditemukan di `{MODEL_PATH}`")
    st.stop()


# SIDEBAR INPUT

st.sidebar.header("🏔️ Input Parameter")

dist = st.sidebar.number_input(
    "Jarak (km)", 1.0, 200.0, 50.0
)

elev = st.sidebar.number_input(
    "Elevation Gain (m)", 0, 15000, 2500
)

month = st.sidebar.slider(
    "Bulan Event", 1, 12, 8
)

weight = st.sidebar.number_input(
    "Berat Badan (kg) [Opsional]", 30, 120, 65
)

# ANALISIS REAL-TIME

km_effort = calculate_km_effort(dist, elev)
category = categorize_race(km_effort)

st.sidebar.markdown("### 📊 Analisis Trail")
st.sidebar.info(f"""
KM Effort: {km_effort:.1f}  
Kategori: {category}
""")

# PREDIKSI

if st.sidebar.button("🔥 Hitung Prediksi"):

    input_df = pd.DataFrame({
        "distance_km": [dist],
        "elevation_gain_m": [elev],
        "race_category": [category],
        "month": [month]
    })

    try:
        prediction = model.predict(input_df)[0]
        jam, menit = format_time(prediction)

        # ==============================
        # HASIL PREDIKSI
        # ==============================
        st.subheader("📈 Hasil Prediksi")

        col1, col2, col3 = st.columns(3)

        col1.metric("⏱️ Jam (Decimal)", f"{prediction:.2f}")
        col2.metric("🕒 Format Waktu", f"{jam}j {menit}m")
        col3.metric("🏔️ KM Effort", f"{km_effort:.1f}")

        st.success(f"""
Estimasi waktu finis:
- {dist} km
- Elevasi {elev} m
- Kategori {category}

👉 sekitar **{jam} jam {menit} menit**
""")

        # ==============================
        # NUTRISI (WAJIB DI DALAM TRY)
        # ==============================
        st.subheader("🍌 Strategi Nutrisi")

        nutrition = get_nutrition_plan(
            hours=prediction,
            weight_kg=weight
        )

        # ===== CARBS =====
        col1, col2 = st.columns(2)
        col1.metric("Karbohidrat / Jam", f"{nutrition['carbs']['per_hour']} g")
        col2.metric("Total Karbohidrat", f"{nutrition['carbs']['total']} g")

        st.info(f"""
📌 Karbohidrat:
- {nutrition['carbs']['note']}
- Konsumsi tiap 20–30 menit
""")

        # ===== HYDRATION =====
        st.markdown("### 💧 Hidrasi")
        st.write(f"- {nutrition['hydration']['per_hour_ml']} / jam")
        st.write(f"- {nutrition['hydration']['note']}")

        # ===== OPTIONAL =====
        if "protein" in nutrition:

            st.markdown("### 🍗 Recovery & Daily Needs")

            col1, col2 = st.columns(2)

            col1.write(f"Protein: {nutrition['protein']['daily_range']}")
            col1.write(nutrition['protein']['note'])

            col2.write(f"Lemak: {nutrition['fat']['daily']}")
            col2.write(nutrition['fat']['note'])

            st.write(f"Kalori Harian: {nutrition['calories']['daily_range']}")

    except Exception as e:
        st.error(f"❌ Error saat prediksi: {e}")
else:
    st.info("Masukkan parameter lalu klik tombol prediksi.")