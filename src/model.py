import pandas as pd
import joblib

# 📦 Charger le modèle et le préprocesseur
model = joblib.load("data/model/random_forest_model.pkl")
encoder = joblib.load("data/model/feature_encoder.pkl")

def predict_patient(input_data: dict):
    """
    Prend un dictionnaire de données patient en entrée,
    renvoie une prédiction basée sur le modèle entraîné.
    """


    # Prétraitement : convertir 'oui'/'non' en 1/0 pour readmission si présent
    data = input_data.copy()
    if 'readmission' in data:
        if isinstance(data['readmission'], str):
            if data['readmission'].lower() == 'oui':
                data['readmission'] = 1
            elif data['readmission'].lower() == 'non':
                data['readmission'] = 0


    # 🔄 Conversion en DataFrame
    df = pd.DataFrame([data])

    # Ajouter les colonnes manquantes attendues par l'encodeur avec valeur par défaut
    for col in encoder.feature_names_in_:
        if col not in df.columns:
            df[col] = ""  # ou None selon le type attendu

    # Réordonner les colonnes pour correspondre à l'encodeur
    df = df[list(encoder.feature_names_in_)]

    # 🔧 Transformation avec le même encodeur qu'à l'entraînement
    X = encoder.transform(df)

    # 🔍 Prédiction
    prediction = model.predict(X)

    return "Décès probable" if prediction[0] == 1 else "Survie probable"
