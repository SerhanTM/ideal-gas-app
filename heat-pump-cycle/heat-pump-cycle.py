# heat_pump_vcc_ideal.py

def vapor_compression_cycle_ideal_gas(Q_dot_out, T1, T3, cp=1005, eta_isentropic=1.0):
    """
    vapor compression cycle (heat pump mode) with ideal gas assumptions.

    Parameters:
        Q_dot_out Heating load at condenser [W]
        T1  Temperature at evaporator outlet / compressor inlet [K]
        T3  Temperature at condenser outlet / expansion inlet [K]
        cp (float): Specific heat at constant pressure [J/kg.K]
        eta_isentropic (float): Isentropic efficiency of the compressor (1.0 = ideal)

    Returns:
        dict: State enthalpies, mass flow rate, compressor work, COP
    """

    # 1. Enthalpies 
    h1 = cp * T1  # Evaporator outlet - compressor inlet
    h3 = cp * T3  # Condenser outlet - expansion valve inlet
    h4 = h3       # Isenthalpic expansion

    # 2. Estimate h2s from isentropic compression (T2s is guessed here)
    pressure_ratio = 3  # Example fixed pressure ratio, can be improved later
    gamma = 1.4         # For air
    T2s = T1 * (pressure_ratio) ** ((gamma - 1) / gamma)
    h2s = cp * T2s

    # 3. Correct for isentropic efficiency
    h2 = h1 + (h2s - h1) / eta_isentropic

    # 4. Calculate required mass flow rate
    m_dot = Q_dot_out / (h2 - h3)  # [kg/s]

    # 5. Compressor power
    W_dot_comp = m_dot * (h2 - h1)  # [W]

    # 6. COP
    COP = Q_dot_out / W_dot_comp

    return {
        "mass_flow_rate_kg_s": m_dot,
        "compressor_power_W": W_dot_comp,
        "COP": COP,
        "h1": h1,
        "h2": h2,
        "h3": h3,
        "h4": h4,
        "T2s": T2s
    }

# Example usage:
if __name__ == "__main__":
    results = vapor_compression_cycle_ideal_gas(
        Q_dot_out=2000,           # Heating load in W
        T1=273.15 + 0,          # Evaporator outlet temp [K]
        T3=273.15 + 35,         # Condenser outlet temp [K]
        cp=1005,                # J/kg.K
        eta_isentropic=1.0      # Perfect compressor
    )

    for key, value in results.items():
        print(f"{key}: {value:.3f}")
