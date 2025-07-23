
# Hospital AI Project

Projet d'IA pour la prédiction médicale

## Structure du projet

- `data/` : Contient les données brutes et nettoyées
- `notebooks/` : Notebooks pour le nettoyage, feature engineering et entraînement
- `src/` : Code source Python
- `dashboard/` : Fichiers pour le dashboard Power BI

## Installation

1. Cloner le dépôt
2. Créer un environnement virtuel
3. Installer les dépendances :
```bash
pip install -r requirements.txt







| `data/BaseMedicale_Talend.xlsx`            | Données brutes                                          |
| `notebooks/1_data_cleaning.ipynb`          | Lecture + nettoyage (drop, format, null)                |
| `notebooks/2_feature_engineering.ipynb`    | Encodage, sélection des features                        |
| `notebooks/3_model_training.ipynb`         | Entraînement du modèle                                  |
| `data/model/random_forest_model.pkl`       | Modèle IA entraîné                                      |
| `src/database.py`                          | Chargement de données pour l’interface                  |
| `src/model.py`                             | Prediction avec le modèle IA                            |
| `src/utils.py`                             | Fonctions auxiliaires (ex: encodage, calcul taux, etc.) |
| `app.py`                                   | Interface finale Streamlit                              |
| `dashboard/powerful_embed.py`              | Intégration Power BI dans Streamlit                     |
| `dashboard/assets/hospital_dashboard.pbix` | Ton dashboard Power BI exporté                          |
| `requirements.txt`                         | Dépendances Python                                      |
| `README.md`                                | (Optionnel) Explication projet                          |

