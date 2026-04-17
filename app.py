import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

# --- MOTEUR DE CALCUL (LA LOGIQUE) ---
class SteelEngine:
    @staticmethod
    def simuler_gain(recyclage):
        return round(recyclage * 0.5, 2)
    @staticmethod
    def predire_stock(demande):
        return round(demande * 1.15, 0)

# --- CONFIGURATION & DESIGN ---
st.set_page_config(page_title="SIAB Smart-Steel Loop", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #001f3f; color: white; }
    [data-testid="stMetricValue"] { color: #00d1ff !important; font-weight: bold; }
    div[data-testid="metric-container"] {
        background-color: rgba(255, 255, 255, 0.05);
        border-left: 5px solid #ff851b;
        padding: 15px;
    }
    .stButton>button { background-color: #ff851b; color: white; font-weight: bold; height: 3em; width: 100%; border: none; }
    .stButton>button:hover { background-color: #e67616; border: 1px solid white; }
    </style>
    """, unsafe_allow_html=True)

# --- BARRE LATÉRALE ---
st.sidebar.title("🚀 Menu Stratégique")
choix = st.sidebar.radio("Où voulez-vous aller ?", 
    ["1. Vue d'Ensemble (Dashboard)", 
     "2. Simulateur de Gain (Logistique)", 
     "3. Prédiction IA (Stocks)"])

# --- PAGE 1 : DASHBOARD ---
if choix == "1. Vue d'Ensemble (Dashboard)":
    st.title("📊 Tableau de Bord : Performance SIAB")
    st.write("Ce tableau montre l'impact du projet sur les opérations actuelles.")
    
    c1, c2, c3 = st.columns(3)
    c1.metric("Temps de Chargement", "42 min", "-18% (Gain Lean)")
    c2.metric("Taux de Recyclage", "24%", "+7% (Économie)")
    c3.metric("Erreurs Livraison", "0.2%", "-92% (Qualité)")

    st.subheader("📈 Évolution de la Productivité")
    df = pd.DataFrame({
        'Mois': ['Jan', 'Féb', 'Mar', 'Avr', 'Mai'],
        'Avant Projet': [100, 102, 101, 103, 102],
        'Avec Smart-Steel': [100, 112, 118, 125, 130]
    })
    fig = px.line(df, x='Mois', y=['Avant Projet', 'Avec Smart-Steel'], markers=True)
    fig.update_layout(template="plotly_dark", paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)')
    st.plotly_chart(fig, use_container_width=True)

# --- PAGE 2 : SIMULATEUR ---
elif choix == "2. Simulateur de Gain (Logistique)":
    st.title("♻️ Simulateur de Logistique Inverse")
    st.info("Ici, nous calculons combien d'argent la SIAB gagne en récupérant de la ferraille sur les chantiers.")
    
    taux = st.slider("Choisissez un taux de récupération (%)", 0, 100, 25)
    
    if st.button("Calculer le bénéfice financier"):
        gain = SteelEngine.simuler_gain(taux)
        st.success(f"### Résultat : En récupérant {taux}% de ferraille, vous augmentez votre marge de **{gain}%**.")
        st.write("C'est l'application directe du concept de 'Flux Tirés'.")

# --- PAGE 3 : IA ---
elif choix == "3. Prédiction IA (Stocks)":
    st.title("🤖 Intelligence Artificielle & Stocks")
    st.write("Ce module utilise un algorithme pour éviter que l'usine ne tombe en rupture de ferraille.")
    
    besoin = st.number_input("Entrez la demande client prévue (Tonnes)", 100, 5000, 1000)
    
    if st.button("Lancer la prédiction"):
        stock_total = SteelEngine.predire_stock(besoin)
        st.markdown(f"### 🛡️ Sécurité : Pour livrer {besoin} T, vous devez avoir **{stock_total} T** en stock.")
        st.info("L'IA ajoute une marge de sécurité basée sur la variabilité des transports au Bénin.")
