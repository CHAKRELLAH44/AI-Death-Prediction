
# Hospital AI Project

Projet d'IA pour la prédiction médicale

## Structure du projet

- `data/` : Contient les données brutes et nettoyées
- `notebooks/` : Notebooks pour le nettoyage, feature engineering et entraînement
- `src/` : Code source Python

## Installation

1. Cloner le dépôt
2. Créer un environnement virtuel
3. Installer les dépendances :

```bash
pip install -r requirements.txt
```




Le cycle résumé :

1-L’interface (Streamlit) envoie les infos du patient (nom, âge, etc.).(app.py)

2-model.py les transforme en DataFrame.
    - Un DataFrame est une structure de données du module pandas (comme un tableau Excel mais en Python).
    - Scikit-learn (la bibliothèque utilisée pour le modèle) attend les données sous ce format pour faire la prédiction
=> Transformer dakchi li dkhel l tableau 

2-Le feature_encoder.pkl encode ces données.
Ajoute toutes les colonnes manquantes attendues par le pipeline d’encodage (feature_encoder.pkl) avec des valeurs par défaut ("" ou np.nan)

3-Le modèle Random Forest (random_forest_model.pkl) prédit :
      0 ou 1 (survie ou décès)
      le pourcentage de probabilité





