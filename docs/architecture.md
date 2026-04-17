# Architecture Technique : Smart-Steel Loop 2050

## 1. Séparation des Responsabilités (SoC)
Le projet suit une architecture modulaire pour garantir la maintenabilité industrielle :
- **UI (`app.py`)** : Interface utilisateur Streamlit optimisée pour le terrain.
- **Engine (`models/engine.py`)** : Cœur de calcul et modèles prédictifs (Simulation Random Forest).
- **Data (`data/`)** : Stockage des flux de production et de collecte.

## 2. Logique de Simulation (Inspiration MIT SC2x)
Le moteur de calcul intègre :
- **Probabilistic Forecasting** : Pour anticiper les ruptures de stock de ferraille.
- **Milk-Run Optimization** : Algorithme de calcul de trajectoire pour minimiser les kilomètres à vide (Backhauling).

## 3. Design Industriel
Le thème **Bleu Nuit** et les composants **Poka-Yoke** ont été choisis pour réduire la charge cognitive des opérateurs et assurer une saisie de données "Zéro Erreur".
