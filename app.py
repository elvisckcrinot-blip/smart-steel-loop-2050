import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# Configuration de l'interface
st.set_page_config(
    page_title="SIAB Smart-Steel Loop 2050",
    page_icon="",
    layout="wide"
)

# Style CSS pour le look industriel "Bleu Nuit"
st.markdown("""
    <style>
    /* Fond principal en Bleu Nuit */
    .stApp {
        background-color: #001f3f;
        color: #ffffff;
    }
    
    /* Style des métriques */
    [data-testid="stMetricValue"] {
        color: #00d1ff !important;
    }
    
    /* Conteneurs de métriques avec bordure néon */
    div[data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 209, 255, 0.3);
        padding: 15px;
        border-radius: 10px;
    }

    /* Style des boutons (Contraste Orange Industriel) */
    .stButton>button {
        background-color: #ff851b;
        color: white;
        border-radius: 5px;
        border: none;
        width: 100%;
        font-weight: bold;
    }
    .stButton>button:hover {
        background-color: #ff7400;
        color: white;
    }

    /* Sidebar personnalisée */
    section[data-testid="stSidebar"] {
        background-color: #001529;
    }
    </style>
    """, unsafe_allow_html=True)

# Barre latérale (Navigation Lean)
st.sidebar.image("https://img.icons8.com/fluency/96/factory.png", width=80)
st.sidebar.title("Smart-Steel Control Tower")
st.sidebar.markdown("---")
page = st.sidebar.radio("Navigation", ["Tableau de Bord Exécutif", "Logistique Inverse", "Optimisation Machine Learning"])

# --- PAGE 1 : DASHBOARD EXÉCUTIF ---
if page == "Tableau de Bord Exécutif":
    st.title(" Excellence Opérationnelle SIAB")
    st.subheader("Vision 2050 : Flux Circulaires & Digital Twin")

    # KPIs Métriques
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Lead Time Chargement", "42 min", "-18%")
    col2.metric("Taux de Recyclage", "24%", "+7%")
    col3.metric("Erreurs Livraison", "0.2%", "-92%")
    col4.metric("ROI Logistique", "+5.4%", "Objectif atteint")

    st.markdown("---")

    # Graphique de Flux (Optimisé pour thème sombre)
    st.subheader("Simulation de la Capacité de Distribution (Lean vs Traditionnel)")
    data = pd.DataFrame({
        'Mois': ['Jan', 'Féb', 'Mar', 'Avr', 'Mai', 'Juin'],
        'Capacité Classique': [100, 105, 102, 108, 105, 110],
        'Smart-Steel Loop': [100, 115, 122, 130, 135, 142]
    })
    
    fig = px.line(data, x='Mois', y=['Capacité Classique', 'Smart-Steel Loop'], 
                  color_discrete_map={'Capacité Classique': '#ff4136', 'Smart-Steel Loop': '#2ecc40'})
    
    fig.update_layout(
        template="plotly_dark",
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        font_color="#ffffff"
    )
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 2 : LOGISTIQUE INVERSE ---
elif page == "Logistique Inverse":
    st.header(" Optimisation de la Collecte de Ferraille")
    st.info("Ce module optimise le retour des camions (Milk-Run) depuis les chantiers vers l'usine.")
    
    # Simulation de données de collecte
    locations = pd.DataFrame({
        'lat': [6.365, 6.447, 9.330],
        'lon': [2.441, 2.348, 2.616],
        'Chantier': ['Cotonou Port', 'Abomey-Calavi', 'Parakou Hub'],
        'Stock Dispo (T)': [12, 5, 25]
    })
    st.map(locations)
    st.dataframe(locations, use_container_width=True)

# --- PAGE 3 : MACHINE LEARNING ---
elif page == "Optimisation Machine Learning":
    st.header(" Prédiction de la Demande (Random Forest)")
    st.write("Aide à la décision basée sur l'expertise MIT SC2x.")
    
    with st.container():
        tonnage_voulu = st.slider("Prédire le besoin en acier (Tonnes) pour le mois prochain", 500, 5000, 2500)
        if st.button("Lancer la Simulation de Stock"):
            st.success(f"Probabilité de rupture de stock : {np.random.randint(1, 5)}% avec l'optimisation actuelle.")
            st.info("Recommandation : Augmenter la collecte locale à Parakou de 15% pour sécuriser le flux.")
