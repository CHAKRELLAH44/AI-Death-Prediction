import streamlit as st
from src.model import predict_patient

st.set_page_config(page_title="Prédiction Mortalité Patient", layout="centered")

st.title("🧠 Prédiction de la mortalité d’un patient")
st.markdown("Remplissez les informations ci-dessous pour estimer la probabilité de mortalité.")

# Champs UI demandés
nom = st.text_input("Nom")
prenom = st.text_input("Prénom")
sexe = st.selectbox("Sexe", ["Homme", "Femme"])
age = st.number_input("Âge", min_value=0, max_value=120, value=30)
type_sanguin = st.selectbox("Type sanguin", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])
maladie = st.selectbox("Maladie", ["diabète", "hypertension", "asthme", "cancer", "autre"])
medicaments = st.multiselect("Médicaments pris", ["MED001", "MED002", "MED003", "MED004", "MED005", "Autre"])

# Construction du dictionnaire d'entrée pour la prédiction
input_data = {
    "nom": nom.strip(),
    "prenom": prenom.strip(),
    "sexe": sexe,
    "age": age,
    "type_sanguin": type_sanguin,
    "maladie": maladie,
    "id_medicament": ",".join(medicaments),
}

# Bouton de prédiction avec vérification des champs requis
if st.button("🔍 Prédire"):
    if not nom.strip() or not prenom.strip() or len(medicaments) == 0:
        st.warning("❌ Veuillez remplir tous les champs avant de prédire.")
    else:
        resultat = predict_patient(input_data)
        if "Erreur" in resultat:
            st.error(resultat)
        else:
            st.success(f"✅ Résultat : {resultat}")
