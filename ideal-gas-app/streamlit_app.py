# main.py
import streamlit as st

# Ideal gas constant
R = 8.314  # J/mol·K


def calculate_pressure(T, n, V):
    P = (n * R * T) / V  # pressure [Pa] 
    return P / 1000      # convert to kPa

def calculate_temperature(P, n, V):
    
    T = (P * 1000 * V / (n * R)) # Temperature [K]
    return T

st.title("Ideal Gas Calculator")

# Common inputs
n = st.number_input("Amount of substance [mol]", min_value=0.0, value=1.0)
V = st.number_input("Volume [m³]", min_value=0.001, value=0.01)

# Input for either T or P
col1, col2 = st.columns(2)

with col1:
    T_input = st.text_input("Temperature [K]")

with col2:
    P_input = st.text_input("Pressure [kPa]")

# Calculate when button is pressed
if st.button("Calculate"):
    if T_input and not P_input:
        T = float(T_input)
        P_kPa = calculate_pressure(T, n, V)
        st.success(f"Calculated pressure: {P_kPa:.2f} kPa")

    elif P_input and not T_input:
        P_kPa = float(P_input)
        T = calculate_temperature(P_kPa, n, V)
        st.success(f"Calculated temperature: {T:.2f} K")

    else:
        st.warning("Please fill in only one field: either Temperature or Pressure.")
