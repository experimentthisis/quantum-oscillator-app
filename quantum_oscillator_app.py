import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
from scipy.special import hermite, factorial

# --- App title and intro ---
st.title("🌀 Quantum Harmonic Oscillator Visualizer")
st.write("""
Explore the probability density of a quantum harmonic oscillator for different energy levels (**n**).
Use the slider below to change n and see how the wavefunction changes.
""")

# --- Slider for n ---
n = st.slider("Select energy level (n)", 0, 10, 0)

# --- Calculate wavefunction ---
x = np.linspace(-5, 5, 1000)
Hn = hermite(n)
psi = (1/np.sqrt(2**n * factorial(n) * np.sqrt(np.pi))) * Hn(x) * np.exp(-x**2 / 2)
prob_density = psi**2

# --- Plot the probability density ---
fig, ax = plt.subplots()
ax.plot(x, prob_density, label=f"n = {n}")
ax.set_xlabel("x")
ax.set_ylabel("|ψ(x)|²")
ax.set_title("Quantum Harmonic Oscillator Probability Density")
ax.legend()

# --- Display plot in Streamlit ---
st.pyplot(fig)

# --- Add explanation section ---
st.markdown("---")
st.subheader("🧠 Explanation")
st.write(f"""
For **n = {n}**, there are **{n + 1} peaks** in the probability density.  
Higher energy levels have more oscillations, representing more possible locations for the particle.  
This reflects how quantum energy levels increase discretely — not continuously.
""")

st.caption("Created by N.I • Electrical Engineering + Quantum Visualization Project")
