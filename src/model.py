import pandas as pd
import joblib
import numpy as np

# Load model and preprocessor
model = joblib.load("data/model/random_forest_model.pkl")
preprocessor = joblib.load("data/model/feature_encoder.pkl")

def predict_patient(input_data: dict) -> str:
    """
    Takes patient data as input and returns mortality probability as a percentage.
    """
    try:
        # Expected columns
        expected_columns = ['age', 'sexe', 'type_sanguin', 'maladie', 'id_service', 
                           'medecin_traitant', 'personnel', 'id_medicament', 
                           'readmission', 'numIntervention', 'duree_sejour', 'TrancheAge']

        # Copy input data
        data = input_data.copy()

        # Remove unused columns
        data.pop('nom', None)

        # Add missing columns with default values
        for col in expected_columns:
            if col not in data:
                if col in ['age', 'readmission', 'numIntervention', 'duree_sejour']:
                    data[col] = 0  # Default for numerical columns
                else:
                    data[col] = 'inconnu'  # Default for categorical columns

        # Ensure numerical columns are floats
        numerical_cols = ['age', 'readmission', 'numIntervention', 'duree_sejour']
        for col in numerical_cols:
            try:
                data[col] = float(data[col])
            except (ValueError, TypeError):
                return f"Erreur : La colonne {col} doit contenir une valeur numérique valide."

        # Calculate TrancheAge
        bins = [0, 18, 40, 60, 80, 120]
        labels = ["0-17", "18-39", "40-59", "60-79", "80+"]
        age = float(data['age'])
        data['TrancheAge'] = pd.cut([age], bins=bins, labels=labels, right=False)[0]

        # Create DataFrame
        df = pd.DataFrame([data])

        # Reorder columns
        df = df[expected_columns]

        # Transform data
        X = preprocessor.transform(df)

        # Predict probability
        proba = model.predict_proba(X)[0]
        mortality_proba = proba[1] * 100

        return f"{mortality_proba:.2f}"
    
    except Exception as e:
        return f"Erreur lors de la prédiction : {str(e)}"