import pandas as pd
import os

# Charger la feuille "Patients" depuis le fichier Excel
df = pd.read_excel("data/BaseMedicale_Talend.xlsx", sheet_name="Patients")

# Vérification des colonnes disponibles
print("Colonnes disponibles :", df.columns.tolist())

# Nettoyage minimal : suppression des lignes incomplètes
df = df.dropna(subset=["sexe", "age", "maladie", "id_service", "mortalite"])

# Optionnel : création d'une colonne 'TrancheAge'
bins = [0, 18, 40, 60, 80, 120]
labels = ["0-17", "18-39", "40-59", "60-79", "80+"]
df["TrancheAge"] = pd.cut(df["age"], bins=bins, labels=labels, right=False)

# Sauvegarde dans un fichier CSV nettoyé
os.makedirs("data", exist_ok=True)
df.to_csv("data/cleaned_data.csv", index=False)

print("✅ Données nettoyées et enregistrées dans data/cleaned_data.csv")
