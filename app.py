import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- LOGIQUE DE CALCUL ---
class SteelEngine:
    @staticmethod
    def calculer_gain_financier(taux_recyclage):
        # Simulation : gain de 0.5% par point de recyclage
        return round(taux_recyclage * 0.5, 2)
    
    @staticmethod
    def predire_besoin_total(demande_client):
        # Simulation IA : demande + 15% de stock de sécurité
        return round(demande_client * 1.15, 0)

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="SIAB - Smart-Steel Loop", layout="wide")

# --- NAVIGATION ---
st.sidebar.title("Navigation Projet")
menu = st.sidebar.radio("Sélectionnez une étape :", 
    ["📊 1. Diagnostic & Dashboard", 
     "♻️ 2. Simulation Recyclage", 
     "🤖 3. Prédiction des Stocks"])

# --- PAGE 1 : DASHBOARD ---
if menu == "📊 1. Diagnostic & Dashboard":
    st.title("Tableau de Bord de Performance (SIAB)")
    st.write("Ce dashboard présente l'impact des optimisations Lean sur les flux de l'usine.")
    
    col1, col2, col3 = st.columns(3)
    col1.metric("Lead Time (Chargement)", "42 min", "-18%")
    col2.metric("Taux de Recyclage", "24%", "+7%")
    col3.metric("Précision Livraison", "99.8%", "+12%")

    st.divider()
    
    st.subheader("Comparaison de la Productivité")
    data = pd.DataFrame({
        'Mois': ['Jan', 'Féb', 'Mar', 'Avr', 'Mai'],
        'Capacité Initiale': [100, 102, 101, 103, 102],
        'Capacité Optimisée': [100, 112, 118, 125, 130]
    })
    fig = px.line(data, x='Mois', y=['Capacité Initiale', 'Capacité Optimisée'], 
                  title="Hausse de capacité (Tonnes/Mois)", markers=True)
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 2 : SIMULATEUR ---
elif menu == "♻️ 2. Simulation Recyclage":
    st.title("Simulateur de Logistique Inverse")
    st.write("Calculez l'économie réalisée en récupérant la ferraille sur les chantiers clients.")
    
    taux = st.slider("Taux de récupération visé (%)", 0, 100, 25)
    
    if st.button("Calculer l'impact sur la marge"):
        gain = SteelEngine.calculer_gain_financier(taux)
        st.success(f"### Résultat : +{gain}% de marge nette")
        st.info("Ce gain provient de la réduction de l'achat de matière première neuve.")

# --- PAGE 3 : PRÉDICTION ---
elif menu == "🤖 3. Prédiction des Stocks":
    st.title("Prédiction Intelligente des Besoins")
    st.write("Utilisation de l'IA pour anticiper les besoins en ferraille et éviter les ruptures.")
    
    demande = st.number_input("Demande client prévue (en Tonnes)", min_value=100, max_value=10000, value=1000)
    
    if st.button("Prédire le stock nécessaire"):
        total = SteelEngine.predire_besoin_total(demande)
        st.subheader(f"Quantité totale à sécuriser : {total} Tonnes")
        st.warning(f"Note : Cela inclut {int(total - demande)} Tonnes de stock de sécurité pour pallier les aléas de transport.")
    
