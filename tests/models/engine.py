import numpy as np
import pandas as pd

class SteelEngine:
    """Moteur de calcul pour l'optimisation SIAB (Inspiré MIT SC2x)"""
    
    @staticmethod
    def predict_demand(tonnage_input):
        """
        Simule un modèle Random Forest pour la prédiction des stocks.
        En production, on chargerait ici un modèle : joblib.load('model.pkl')
        """
        # Simulation d'un intervalle de confiance
        confidence_interval = 0.05
        prediction = tonnage_input * (1 + np.random.uniform(-confidence_interval, confidence_interval))
        return round(prediction, 2)

    @staticmethod
    def calculate_roi(recycling_rate):
        """
        Calcule l'impact financier de la logistique inverse.
        Estimation : Réduction du coût de revient de 0.5% pour chaque 1% de ferraille recyclée.
        """
        base_saving = 0.12 # 12% objectif
        impact = recycling_rate * 0.5
        return round(impact, 2)

    @staticmethod
    def get_transport_emissions(distance, load_weight):
        """Calcul de l'empreinte carbone (Standard Green Logistics)"""
        # Coéfficient moyen : 0.15kg CO2 par tonne-km
        emissions = distance * load_weight * 0.15
        return round(emissions, 2)
  
