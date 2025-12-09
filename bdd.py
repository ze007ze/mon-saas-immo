import streamlit as st
import pandas as pd
import sqlite3

# --- FONCTIONS DE GESTION BDD (Le Backend) ---

def init_db():
    """Crée la table si elle n'existe pas encore"""
    conn = sqlite3.connect("ma_base.db")
    c = conn.cursor()
    c.execute("""
        CREATE TABLE IF NOT EXISTS utilisateurs (
            pseudo TEXT,
            email TEXT,
            grade TEXT,
            telephone TEXT
        )
    """)
    conn.commit()
    conn.close()

def ajouter_client_bdd(pseudo, email, grade, telephone):
    """Ajoute une ligne dans la base de données"""
    conn = sqlite3.connect("ma_base.db")
    c = conn.cursor()
    c.execute(
        "INSERT INTO utilisateurs (pseudo, email, grade, telephone) VALUES (?, ?, ?, ?)",
        (pseudo, email, grade, telephone)
    )
    conn.commit()
    conn.close()

def lire_tous_clients():
    """Récupère toutes les infos pour les donner à Pandas"""
    conn = sqlite3.connect("ma_base.db")
    c = conn.cursor()
    c.execute("SELECT * FROM utilisateurs")
    data = c.fetchall() # Renvoie une liste de tuples
    conn.close()
    return data

# --- L'INTERFACE (Le Frontend) ---

# 1. On lance l'initialisation au tout début
init_db()

st.sidebar.title("Inscription")
pseudo = st.sidebar.text_input("Votre Pseudo")
email = st.sidebar.text_input("Votre Email")
telephone = st.sidebar.text_input("votre numéro")
grade = st.sidebar.selectbox("Abonnement", ["Gratuit (0€)", "Pro (19€)"])

st.title("Mon SaaS (Connecté BDD)")

if st.sidebar.button("Créer mon compte"):
    # On appelle la fonction SQL au lieu de la classe
    ajouter_client_bdd(pseudo, email, grade, telephone)
    st.success(f"Compte créé pour {pseudo} ! (Sauvegardé en BDD)")


# --- LE DASHBOARD (Data Science) ---

st.header("Base de données Réelle")

# 1. On récupère les données fraîches depuis le disque dur
donnees_brutes = lire_tous_clients()

# 2. On transforme en DataFrame (Tableau Excel)
df = pd.DataFrame(donnees_brutes, columns=['Pseudo', 'Email', 'Grade', 'Telephone'])

# 3. Logique Business (Calcul du prix)
# On crée une petite fonction pour convertir le grade en prix
def get_prix(g):
    return 19 if "Pro" in g else 0

if not df.empty:
    # On applique le calcul du prix sur toute une colonne d'un coup
    df['Prix'] = df['Grade'].apply(get_prix)
    
    # Calcul du total
    ca_total = df['Prix'].sum()
    
    # Affichage
    st.metric(label="Chiffre d'Affaires Mensuel", value=f"{ca_total} €")
    st.dataframe(df)
    st.bar_chart(df['Grade'].value_counts())
else:
    st.info("La base de données est vide. Ajoutez un client !")