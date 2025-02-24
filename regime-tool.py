import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

st.set_page_config(page_title="Marktregime-Analyse", layout="centered")

st.title("📈 Marktregime-Analyse Tool")
st.write("Analysiere die aktuelle Marktlage anhand wirtschaftlicher Kennzahlen und erkenne Marktregime.")

# Nutzereingaben
st.sidebar.header("📊 Parameter-Eingabe")
volatility = st.sidebar.slider("Marktvolatilität (VIX)", min_value=10, max_value=80, value=20)
interest_rate = st.sidebar.slider("Leitzins (%)", min_value=0.0, max_value=10.0, value=2.5)
inflation = st.sidebar.slider("Inflationsrate (%)", min_value=-2.0, max_value=10.0, value=3.0)
correlation = st.sidebar.slider("Aktien-Anleihen Korrelation", min_value=-1.0, max_value=1.0, value=0.2)

def classify_market_regime(volatility, interest_rate, inflation, correlation):
    if volatility < 20 and interest_rate < 3 and inflation < 4:
        return "Stabiles Marktregime", "🟢", "green"
    elif volatility < 35 and correlation < 0.5:
        return "Übergangsregime", "🟡", "yellow"
    else:
        return "Krisenregime", "🔴", "red"

# Bestimmung des Marktregimes
regime, icon, color = classify_market_regime(volatility, interest_rate, inflation, correlation)
st.markdown(f"### {icon} Aktuelles Marktregime: **{regime}**")

# Visualisierung des Regimes
fig, ax = plt.subplots()
categories = ["Stabil", "Übergang", "Krise"]
values = [1 if regime == "Stabiles Marktregime" else 0,
          1 if regime == "Übergangsregime" else 0,
          1 if regime == "Krisenregime" else 0]
ax.bar(categories, values, color=[color if v == 1 else "grey" for v in values])
st.pyplot(fig)

# Strategieempfehlung
st.subheader("📌 Strategieempfehlungen")
if regime == "Stabiles Marktregime":
    st.success("🔹 Klassisches 60/40-Portfolio (60% Aktien, 40% Anleihen) bleibt effektiv.")
    st.success("🔹 Hohe Diversifikation möglich.")
elif regime == "Übergangsregime":
    st.warning("⚠️ Markt ist unsicher, defensive Allokation kann sinnvoll sein.")
    st.warning("🔹 Mögliches Umschichten in liquide Assets oder Gold.")
else:
    st.error("🚨 Krisenregime! Risikomanagement erforderlich.")
    st.error("🔹 Absicherung mit Put-Optionen oder Kapitalerhalt-Strategien empfohlen.")
    st.error("🔹 Hohe Korrelation zwischen Assets - Diversifikation reduziert.")

st.write("💡 Tipp: Spiele verschiedene Szenarien durch, um die Marktstabilität einzuschätzen!")
