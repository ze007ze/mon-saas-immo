import streamlit as st
import pandas as pd
import sqlite3
import joblib
import hashlib

def verifier_connexion(pseudo, mot_de_passe_input):
    conn = sqlite3.connect("ma_base.db")
    c = conn.cursor()
    mdp_hasher = hashlib.sha256(mot_de_passe_input.encode()).hexdigest()
    c.execute("SELECT mot_de_passe FROM utilisateurs WHERE pseudo = ?",(pseudo,))
    pseudo_chercher = c.fetchone()

    if pseudo_chercher:
        if pseudo_chercher[0] == mdp_hasher:
            st.success(f"mot de passe correct")
            st.session_state['est_connecte'] = True
            st.session_state['pseudo_user'] = pseudo
        else:
            st.error("mot de passe incorrect")
    else:
        st.error(f"mauvais mot de passe pour {pseudo}")
    
    conn.commit()
    conn.close()

def hasher_mdp(mot_de_passe):
    # On encode le texte en bits, puis on le hache avec l'algo SHA-256
    return hashlib.sha256(mot_de_passe.encode()).hexdigest()
# --- FONCTIONS DE GESTION BDD (Le Backend) ---


def init_db():
    """Crée la table si elle n'existe pas encore"""
    conn = sqlite3.connect("ma_base.db")
    c = conn.cursor()
    # Note : On a ajouté la colonne 'telephone'
    c.execute("""
        CREATE TABLE IF NOT EXISTS utilisateurs (
            pseudo TEXT,
            email TEXT,
            mot_de_passe TEXT,
            grade TEXT,
            telephone TEXT
        )
    """)
    conn.commit()
    conn.close()

def ajouter_client_bdd(pseudo, email, mot_de_passe, grade, telephone):
    """Ajoute une ligne dans la base de données"""
    conn = sqlite3.connect("ma_base.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO utilisateurs (pseudo, email, mot_de_passe, grade, telephone) VALUES (?, ?, ?, ?, ?)",
        (pseudo, email, mot_de_passe, grade, telephone)
    )
    conn.commit()
    conn.close()

def lire_tous_clients():
    """Récupère toutes les infos pour les donner à Pandas"""
    conn = sqlite3.connect("ma_base.db")
    c = conn.cursor()
    c.execute("SELECT * FROM utilisateurs")
    data = c.fetchall()
    conn.close()
    return data

# --- CHARGEMENT DE L'IA ---
try:
    modele_ia = joblib.load('modele_immo.pkl')
    ia_disponible = True
except:
    ia_disponible = False

# --- L'INTERFACE (Frontend) ---

# 1. On lance l'initialisation au tout début
init_db()

menu = st.sidebar.radio("", ["Inscription", "Connexion"])

if menu == "Inscription":
    st.sidebar.title("Inscription")
    pseudo = st.sidebar.text_input("Votre Pseudo")
    email = st.sidebar.text_input("Votre Email")
    mot_de_passe = st.sidebar.text_input("Votre mot de passe")
    telephone = st.sidebar.text_input("Votre Numéro")
    grade = st.sidebar.selectbox("Abonnement", ["Gratuit (0€)", "Pro (19€)"])
    mdp = hasher_mdp(mot_de_passe)
    st.title("🏡 Immo")

    if st.sidebar.button("Créer mon compte"):
        ajouter_client_bdd(pseudo, email, mdp, grade, telephone)
        st.success(f"Compte créé pour {pseudo} ! (Sauvegardé en BDD)")
elif menu == "Connexion":
    st.sidebar.title("Connexion")
    pseudo = st.sidebar.text_input("Votre pseudo")
    mdp = st.sidebar.text_input("votre mot de passe", type='password')
    if st.sidebar.button("Se Connecter"):
        verifier_connexion(pseudo, mdp)


# --- ZONE 1 : L'ESTIMATEUR IA (Le Produit) ---
st.divider()
st.header("🔮 Estimateur de Prix (IA)")

if ia_disponible:
    col1, col2 = st.columns(2)
    with col1:
        surface = st.number_input("Surface (m²)", min_value=10, max_value=500, value=50)
    with col2:
        nb_pieces = st.number_input("Nombre de pièces", min_value=1, max_value=10, value=2)
    
    if st.button("Estimer le prix"):
        # On envoie les DEUX variables à l'IA : [[surface, nb_pieces]]
        donnee_a_predire = [[surface, nb_pieces]]
        
        # Prédiction
        prix_estime = modele_ia.predict(donnee_a_predire)[0]
        
        st.balloons()
        st.metric(label="Prix Estimé", value=f"{prix_estime:,.0f} €")
else:
    st.error("Le fichier 'modele_immo.pkl' est introuvable. Lance d'abord entrainement_ia.py !")


# --- ZONE 2 : LE DASHBOARD ADMIN (Le Business) ---
st.divider()
st.subheader("📊 Espace Administration (KPIs)")

donnees_brutes = lire_tous_clients()
# On ajoute la colonne Telephone au DataFrame
df = pd.DataFrame(donnees_brutes, columns=['Pseudo', 'Email', 'mdp', 'Grade', 'Telephone'])

if not df.empty:
    def get_prix(g):
        return 19 if "Pro" in g else 0
    
    df['Prix'] = df['Grade'].apply(get_prix)
    
    st.metric(label="Chiffre d'Affaires Mensuel", value=f"{df['Prix'].sum()} €")
    st.dataframe(df)
    st.bar_chart(df['Grade'].value_counts())
else:
    st.info("La base de données est vide. Ajoutez un client !")

