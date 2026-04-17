import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- LOGIQUE INDUSTRIELLE EXPERTE (SteelEngine) ---
class SteelEngine:
    @staticmethod
    def predict_demand(tonnage_input):
        # Simulation Random Forest : Ajout d'une variabilité de 5% (Inspiration MIT)
        confidence_interval = 0.05
        prediction = tonnage_input * (1 + np.random.uniform(-confidence_interval, confidence_interval))
        return round(prediction, 2)

    @staticmethod
    def calculate_roi(recycling_rate):
        # Impact financier : +0.5% ROI pour chaque 1% de recyclage
        impact = recycling_rate * 0.5
        return round(impact, 2)

    @staticmethod
    def simulate_buffer_stock(avg_demand):
        # Calcul du stock de sécurité (Poka-Yoke numérique)
        # Formule simplifiée : Demande moyenne * Facteur de service (1.2)
        return round(avg_demand * 1.2, 0)

# --- CONFIGURATION DE LA PAGE ---
st.set_page_config(page_title="SIAB Smart-Steel Loop 2050", page_icon="🏗️", layout="wide")

# --- DESIGN "MIDNIGHT BLUE" ---
st.markdown("""
    <style>
    .stApp { background-color: #001f3f; color: #ffffff; }
    [data-testid="stMetricValue"] { color: #00d1ff !important; }
    div[data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.05);
        border: 1px solid rgba(0, 209, 255, 0.3);
        padding: 15px; border-radius: 10px;
    }
    .stButton>button {
        background-color: #ff851b; color: white;
        border-radius: 5px; border: none; width: 100%; font-weight: bold; height: 3em;
    }
    .stButton>button:hover { background-color: #ff7400; border: 1px solid white; }
    section[data-testid="stSidebar"] { background-color: #001529; }
    </style>
    """, unsafe_allow_html=True)

# --- NAVIGATION ---
st.sidebar.image("https://img.icons8.com/fluency/96/factory.png", width=80)
st.sidebar.title("Control Tower")
page = st.sidebar.radio("Navigation", ["Dashboard Exécutif", "Simulateur de Flux", "Prédiction Machine Learning"])

# --- PAGE 1 : DASHBOARD ---
if page == "Dashboard Exécutif":
    st.title("🏗️ Performance Industrielle SIAB")
    col1, col2, col3, col4 = st.columns(4)
    col1.metric("Lead Time Chargement", "42 min", "-18%")
    col2.metric("Taux de Recyclage", "24%", "+7%")
    col3.metric("Erreurs Livraison", "0.2%", "-92%")
    col4.metric("Économie de Carbone", "15.4 T", "+12%")
    
    # Graphique de comparaison
    data = pd.DataFrame({
        'Jour': ['Lundi', 'Mardi', 'Mercredi', 'Jeudi', 'Vendredi'],
        'Sans Optimisation': [85, 88, 82, 90, 87],
        'Smart-Steel Loop': [95, 98, 97, 102, 105]
    })
    fig = px.bar(data, x='Jour', y=['Sans Optimisation', 'Smart-Steel Loop'], barmode='group', title="Productivité Quotidienne (Tonnes)")
    fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 2 : SIMULATEUR DE FLUX (NOUVEAU) ---
elif page == "Simulateur de Flux":
    st.header("🔄 Simulateur de Boucle Circulaire")
    st.write("Calculez l'impact du recyclage sur vos stocks en temps réel.")
    
    col_a, col_b = st.columns(2)
    with col_a:
        ferraille_collectee = st.number_input("Ferraille collectée ce mois (Tonnes)", 0, 1000, 150)
    with col_b:
        objectif_recyclage = st.slider("Cible de recyclage (%)", 10, 80, 25)
    
    if st.button("Simuler l'Impact"):
        gain = SteelEngine.calculate_roi(objectif_recyclage)
        st.markdown(f"### 📊 Résultat : +{gain}% de marge nette logistique.")
        st.progress(objectif_recyclage / 100)
        st.info(f"En recyclant {objectif_recyclage}%, la SIAB économise environ {int(ferraille_collectee * (objectif_recyclage/100))} tonnes de matière première neuve.")

# --- PAGE 3 : MACHINE LEARNING ---
elif page == "Prédiction Machine Learning":
    st.header("🤖 Intelligence Artificielle & Stocks")
    tonnage = st.slider("Demande prévue par le marché (Tonnes)", 500, 5000, 2000)
    
    if st.button("Exécuter Random Forest"):
        pred = SteelEngine.predict_demand(tonnage)
        safety = SteelEngine.calculate_roi(24) # Calcul basé sur KPI actuel
        
        c1, c2 = st.columns(2)
        c1.metric("Besoin Prédit", f"{pred} T")
        c2.metric("Stock de Sécurité Recommandé", f"{SteelEngine.simulate_buffer_stock(tonnage)} T")
        
        st.success(f"La simulation confirme que vous devez sécuriser {pred} tonnes pour éviter toute rupture.")
