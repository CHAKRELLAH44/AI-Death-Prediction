import streamlit as st
from src.model import predict_patient
import base64
import os

# Page configuration with custom logo icon - FULL SCREEN
st.set_page_config(
    page_title="🏥 Mortality Prediction - Medical AI",
    page_icon="dashboard/assets/c-.png",  # Using your custom logo as page icon
    layout="wide",  # Changed from "centered" to "wide" to use full screen
    initial_sidebar_state="collapsed"
)

# Fonction pour charger et encoder le logo en base64
@st.cache_data
def load_logo():
    logo_path = "dashboard/assets/c-.png"
    try:
        if os.path.exists(logo_path):
            with open(logo_path, "rb") as f:
                logo_bytes = f.read()
            logo_base64 = base64.b64encode(logo_bytes).decode()
            return logo_base64
        else:
            return ""
    except Exception as e:
        st.error(f"Error loading logo: {e}")
        return ""

# Charger le logo
if 'logo_base64' not in st.session_state:
    st.session_state.logo_base64 = load_logo()

# CSS personnalisé pour le style
st.markdown("""
<style>
    /* Style général */
    .main {
        padding-top: 1rem;
        max-width: 100%;
    }

    /* Message de bienvenue en grand */
    .welcome-banner {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 50%, #667eea 100%);
        padding: 3rem 2rem;
        text-align: center;
        margin-bottom: 2rem;
        border-radius: 20px;
        box-shadow: 0 15px 35px rgba(0,0,0,0.1);
        animation: welcomeSlide 1.2s ease-out;
        position: relative;
        overflow: hidden;
    }

    /* Style pour le logo en haut à droite */
    .logo-container {
        position: absolute;
        top: 20px;
        right: 30px;
        z-index: 10;
        animation: logoFloat 3s ease-in-out infinite;
    }

    .logo-image {
        width: 80px;
        height: auto;
        border-radius: 10px;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
        transition: transform 0.3s ease;
    }

    .logo-image:hover {
        transform: scale(1.1);
    }

    @keyframes logoFloat {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-10px); }
    }

    .welcome-banner::before {
        content: '';
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background: linear-gradient(90deg, transparent, rgba(255,255,255,0.2), transparent);
        animation: shine 3s infinite;
    }

    .welcome-text {
        color: white;
        font-size: 3.5rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 3px 3px 6px rgba(0,0,0,0.3);
        letter-spacing: 2px;
    }

    .welcome-subtitle {
        color: #e8f4fd;
        font-size: 1.8rem;
        margin-top: 1rem;
        font-weight: 300;
        opacity: 0.95;
    }

    @keyframes welcomeSlide {
        from {
            opacity: 0;
            transform: translateY(-50px) scale(0.9);
        }
        to {
            opacity: 1;
            transform: translateY(0) scale(1);
        }
    }

    @keyframes shine {
        0% { left: -100%; }
        50% { left: 100%; }
        100% { left: 100%; }
    }

    /* Titre principal avec gradient */
    .title-container {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        text-align: center;
        margin-bottom: 2rem;
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
        animation: fadeInDown 1s ease-out;
    }

    .title-text {
        color: white;
        font-size: 2.5rem;
        font-weight: bold;
        margin: 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }

    .subtitle-text {
        color: #f0f0f0;
        font-size: 1.2rem;
        margin-top: 0.5rem;
        opacity: 0.9;
    }

    /* Animation d'entrée */
    @keyframes fadeInDown {
        from {
            opacity: 0;
            transform: translateY(-30px);
        }
        to {
            opacity: 1;
            transform: translateY(0);
        }
    }

    /* Style pour les métriques */
    .metric-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 1.5rem;
        border-radius: 10px;
        color: white;
        text-align: center;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
        transition: transform 0.3s ease;
    }

    .metric-card:hover {
        transform: translateY(-5px);
    }

    /* Style pour les formulaires */
    .stForm {
        background: rgba(255,255,255,0.05);
        padding: 2rem;
        border-radius: 15px;
        border: 1px solid rgba(255,255,255,0.1);
        backdrop-filter: blur(10px);
        box-shadow: 0 8px 32px rgba(0,0,0,0.1);
    }

    /* Boutons stylisés */
    .stButton > button {
        background: linear-gradient(90deg, #667eea 0%, #764ba2 100%);
        color: white;
        border: none;
        border-radius: 25px;
        padding: 0.75rem 2rem;
        font-weight: bold;
        font-size: 1.1rem;
        transition: all 0.3s ease;
        box-shadow: 0 4px 15px rgba(102, 126, 234, 0.4);
    }

    .stButton > button:hover {
        transform: translateY(-2px);
        box-shadow: 0 6px 20px rgba(102, 126, 234, 0.6);
    }

    /* Alertes stylisées */
    .stAlert {
        border-radius: 10px;
        border: none;
        box-shadow: 0 4px 15px rgba(0,0,0,0.1);
    }

    /* Icônes pour les sections */
    .section-header {
        display: flex;
        align-items: center;
        margin: 1.5rem 0 1rem 0;
        font-size: 1.3rem;
        font-weight: bold;
        color: #667eea;
    }

    .section-icon {
        margin-right: 0.5rem;
        font-size: 1.5rem;
    }
</style>
""", unsafe_allow_html=True)

# Message de bienvenue en grand avec logo
st.markdown("""
<div class="welcome-banner">
    <div class="logo-container">
        <img src="data:image/png;base64,{}" class="logo-image" alt="Logo">
    </div>
    <h1 class="welcome-text">👨‍⚕️ Welcome Doctor! 👩‍⚕️</h1>
    <p class="welcome-subtitle">🤖 Prediction Service is working to help you make good decisions</p>
</div>
""".format(st.session_state.get('logo_base64', '')), unsafe_allow_html=True)

# Main title with style
st.markdown("""
<div class="title-container">
    <h1 class="title-text">🏥 Mortality Prediction</h1>
    <p class="subtitle-text">💡 Artificial Intelligence for Medical Diagnosis Support</p>
</div>
""", unsafe_allow_html=True)

# Information section with icons
st.markdown("""
<div class="section-header">
    <span class="section-icon">📋</span>
    Patient Information
</div>
""", unsafe_allow_html=True)

st.markdown("🔍 **Enter patient information to get an AI-based mortality probability prediction.**")

# Mapping dictionary: real names -> codes with icons
medicament_mapping = {
    "💊 Paracetamol": "MED001",
    "💊 Ibuprofen": "MED002",
    "💊 Loratadine": "MED003",
    "💊 Amoxicillin": "MED004",
    "💊 Ventolin": "MED005",
    "💊 Zyrtec": "MED006",
    "🔄 Other": "Autre"
}

# Main container to use full screen
st.markdown("""
<div style="
    max-width: 100%;
    padding: 0 2rem;
">
""", unsafe_allow_html=True)

# Main form with full screen style
with st.form("patient_form"):
    st.markdown("### 👤 Personal Information")

    # First row - basic information (4 columns to use more space)
    col_nom, col_sexe, col_age, col_sang = st.columns(4)
    with col_nom:
        nom = st.text_input("👤 Patient Name", placeholder="Enter patient name")
    with col_sexe:
        sexe = st.selectbox("⚧ Gender", ["👨 Male", "👩 Female"])
    with col_age:
        age = st.number_input("🎂 Age", min_value=0, max_value=120, value=30, help="Patient age in years")
    with col_sang:
        type_sanguin = st.selectbox("🩸 Blood Type", ["A+", "A-", "B+", "B-", "AB+", "AB-", "O+", "O-"])

    st.markdown("---")
    st.markdown("### 🏥 Medical Information")

    # Medical information - 2 columns for wider fields
    col_maladie, col_med = st.columns([1, 2])  # 1:2 ratio to give more space to medications
    with col_maladie:
        maladie = st.selectbox("🦠 Primary Disease", [
            "🍯 Diabetes",
            "💓 Hypertension",
            "🫁 Asthma",
            "🎗️ Cancer",
            "🔄 Other"
        ])
    with col_med:
        medicaments = st.multiselect(
            "💊 Current Medications",
            list(medicament_mapping.keys()),
            placeholder="Select medications",
            help="Select all medications currently taken by the patient"
        )

    st.markdown("---")
    st.markdown("### 📊 Hospital History")

    # Hospital history - 4 columns to use more space
    col_readm, col_duree, col_spacer1, col_spacer2 = st.columns(4)
    with col_readm:
        readmission = st.number_input(
            "🔄 Number of Readmissions",
            min_value=0,
            max_value=10,
            value=0,
            help="Number of times the patient has been readmitted to the hospital"
        )
    with col_duree:
        duree_sejour = st.number_input(
            "📅 Length of Stay (days)",
            min_value=0,
            value=0,
            help="Expected or current duration of hospital stay"
        )
    with col_spacer1:
        st.markdown("") # Empty space for balancing
    with col_spacer2:
        st.markdown("") # Empty space for balancing

    st.markdown("---")

    # Submit button with style
    col_btn1, col_btn2, col_btn3 = st.columns([1, 2, 1])
    with col_btn2:
        submitted = st.form_submit_button("🔮 Predict Mortality", use_container_width=True)

    if submitted:
        if not nom.strip() or not medicaments:
            st.markdown("""
            <div style="
                background: linear-gradient(90deg, #ff6b6b, #ffa500);
                color: white;
                padding: 1rem;
                border-radius: 10px;
                text-align: center;
                margin: 1rem 0;
                box-shadow: 0 4px 15px rgba(255,107,107,0.3);
            ">
                ⚠️ <strong>Warning!</strong> Please fill in the required fields (Name, Medications).
            </div>
            """, unsafe_allow_html=True)
        else:
            # Display spinner during processing
            with st.spinner('🔄 Analysis in progress... Please wait'):
                # Convert real names to codes for the model
                medicaments_codes = []
                for med in medicaments:
                    # Clean medication icons for mapping
                    med_clean = med.replace("💊 ", "").replace("🔄 ", "")
                    if med_clean in [k.replace("💊 ", "").replace("🔄 ", "") for k in medicament_mapping.keys()]:
                        for key, value in medicament_mapping.items():
                            if med_clean in key:
                                medicaments_codes.append(value)
                                break

                # Clean other fields
                sexe_clean = sexe.replace("👨 ", "").replace("👩 ", "")
                maladie_clean = maladie.replace("🍯 ", "").replace("💓 ", "").replace("🫁 ", "").replace("🎗️ ", "").replace("🔄 ", "")

                # Input dictionary
                input_data = {
                    "nom": nom.strip(),
                    "sexe": sexe_clean,
                    "age": age,
                    "type_sanguin": type_sanguin,
                    "maladie": maladie_clean.lower(),
                    "id_medicament": ",".join(medicaments_codes),
                    "readmission": readmission,
                    "duree_sejour": duree_sejour
                }

                # Predict
                resultat = predict_patient(input_data)

            # Display results with style
            if "Erreur" in resultat or "Error" in resultat:
                st.markdown(f"""
                <div style="
                    background: linear-gradient(90deg, #ff6b6b, #ff8e8e);
                    color: white;
                    padding: 1.5rem;
                    border-radius: 15px;
                    text-align: center;
                    margin: 1rem 0;
                    box-shadow: 0 8px 25px rgba(255,107,107,0.3);
                    animation: shake 0.5s ease-in-out;
                ">
                    ❌ <strong>Error:</strong> {resultat}
                </div>
                """, unsafe_allow_html=True)
            else:
                # Determine color according to risk
                try:
                    prob_value = float(resultat)
                    if prob_value < 20:
                        color_gradient = "linear-gradient(90deg, #00c851, #00ff88)"
                        risk_level = "🟢 LOW"
                        icon = "✅"
                    elif prob_value < 50:
                        color_gradient = "linear-gradient(90deg, #ffbb33, #ffd700)"
                        risk_level = "🟡 MODERATE"
                        icon = "⚠️"
                    else:
                        color_gradient = "linear-gradient(90deg, #ff4444, #ff6b6b)"
                        risk_level = "🔴 HIGH"
                        icon = "🚨"
                except:
                    color_gradient = "linear-gradient(90deg, #667eea, #764ba2)"
                    risk_level = "📊 RESULT"
                    icon = "📈"

                st.markdown(f"""
                <div style="
                    background: {color_gradient};
                    color: white;
                    padding: 2rem;
                    border-radius: 15px;
                    text-align: center;
                    margin: 1.5rem 0;
                    box-shadow: 0 8px 25px rgba(0,0,0,0.2);
                    animation: fadeInUp 0.8s ease-out;
                ">
                    <h2 style="margin: 0; font-size: 1.8rem;">{icon} Analysis Result</h2>
                    <hr style="border: 1px solid rgba(255,255,255,0.3); margin: 1rem 0;">
                    <p style="font-size: 1.3rem; margin: 0.5rem 0;">
                        <strong>Patient:</strong> {nom.strip().title()}
                    </p>
                    <p style="font-size: 2rem; margin: 1rem 0; font-weight: bold;">
                        Mortality Probability: {resultat}%
                    </p>
                    <p style="font-size: 1.2rem; margin: 0.5rem 0;">
                        <strong>Risk Level:</strong> {risk_level}
                    </p>
                </div>
                """, unsafe_allow_html=True)

                # Ajout d'une animation CSS pour les résultats
                st.markdown("""
                <style>
                    @keyframes fadeInUp {
                        from {
                            opacity: 0;
                            transform: translateY(30px);
                        }
                        to {
                            opacity: 1;
                            transform: translateY(0);
                        }
                    }

                    @keyframes shake {
                        0%, 100% { transform: translateX(0); }
                        25% { transform: translateX(-5px); }
                        75% { transform: translateX(5px); }
                    }
                </style>
                """, unsafe_allow_html=True)

# Close main container
st.markdown("</div>", unsafe_allow_html=True)

# Footer with information - full width
st.markdown("---")
st.markdown("""
<div style="
    text-align: center;
    padding: 2rem;
    color: #666;
    font-size: 1rem;
    background: linear-gradient(135deg, rgba(102, 126, 234, 0.1), rgba(118, 75, 162, 0.1));
    border-radius: 15px;
    margin: 2rem 0;
    box-shadow: 0 4px 15px rgba(0,0,0,0.05);
">
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap; margin-bottom: 1rem;">
        <div style="margin: 0.5rem;">🤖 <strong>Medical AI System</strong></div>
        <div style="margin: 0.5rem;">⚕️ <strong>Diagnostic Support Tool</strong></div>
        <div style="margin: 0.5rem;">🔒 <strong>Secure and Confidential Data</strong></div>
    </div>
    <hr style="border: 1px solid rgba(102, 126, 234, 0.2); margin: 1rem 0;">
    <p style="font-size: 1.1rem; color: #e74c3c; font-weight: bold;">
        ⚠️ This system helps with immediate decision-making in emergencies, but only God knows the hour of death.
    </p>
</div>
""", unsafe_allow_html=True)

                