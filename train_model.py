import pandas as pd
import joblib
import os
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# 📌 Charger le jeu de données propre
df = pd.read_csv("data/cleaned_data.csv")

# 🧼 Traitement des colonnes
target_col = "mortalite"
y = df[target_col].apply(lambda x: 1 if x == "oui" else 0)
X = df.drop(columns=[target_col])

# 🔍 Séparation des colonnes catégorielles et numériques
categorical_cols = X.select_dtypes(include=["object"]).columns.tolist()
numerical_cols = X.select_dtypes(include=["int64", "float64"]).columns.tolist()

# ⚙️ Pipeline d'encodage
preprocessor = ColumnTransformer(
    transformers=[
        ("num", StandardScaler(), numerical_cols),
        ("cat", OneHotEncoder(handle_unknown="ignore"), categorical_cols),
    ]
)

# 🔄 Transformation
X_transformed = preprocessor.fit_transform(X)

# 🎯 Train / test
X_train, X_test, y_train, y_test = train_test_split(X_transformed, y, test_size=0.2, random_state=42)

# 🧠 Modèle IA
model = RandomForestClassifier(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

# 💾 Sauvegarde
os.makedirs("data/model", exist_ok=True)
joblib.dump(model, "data/model/random_forest_model.pkl")
joblib.dump(preprocessor, "data/model/feature_encoder.pkl")

print("✅ Modèle et encodeur enregistrés avec succès.")
