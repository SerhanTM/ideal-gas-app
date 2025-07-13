import streamlit as st

def heat_pump_cop(T_hot_C, T_cold_C, real_efficiency, mode='Heating'):
    T_hot_K = T_hot_C + 273.15
    T_cold_K = T_cold_C + 273.15

    if T_hot_K == T_cold_K:
        return float('inf'), float('inf')

    if mode == 'Heating':
        cop_ideal = T_hot_K / (T_hot_K - T_cold_K)
    else:  # cooling
        cop_ideal = T_cold_K / (T_hot_K - T_cold_K)

    cop_real = cop_ideal * real_efficiency
    return cop_ideal, cop_real

# --- UI ---
st.set_page_config(page_title="Heat Pump COP", layout="centered")

st.title("Heat Pump COP Calculator")

#  Mode selection — top of page with buttons
mode = st.radio(
    "Select operating mode:",
    options=["Heating", "Cooling"],
    index=0,
    horizontal=True
)

st.write("Estimate the ideal and real COP of a heat pump based on temperatures and efficiency.")

#  Inputs
T_hot = st.number_input("Hot side temperature (°C)", value=35.0)
T_cold = st.number_input("Cold side temperature (°C)", value=0.0)
efficiency = st.slider("System efficiency (0–1)", min_value=0.1, max_value=1.0, value=0.45)

#  Calculate on button press
if st.button("Calculate COP"):
    cop_ideal, cop_real = heat_pump_cop(T_hot, T_cold, efficiency, mode)
    st.success(f"Mode: {mode.capitalize()}")
    st.success(f"Ideal COP: {cop_ideal:.2f}")
    st.success(f"Real COP (with efficiency): {cop_real:.2f}")