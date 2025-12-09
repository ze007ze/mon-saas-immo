import streamlit as st
import pandas as pd

if 'db_utilisateurs' not in st.session_state:
    st.session_state['db_utilisateurs'] = []

class Utilisateur :
    def __init__(self, pseudo, email, grade):
        self.pseudo = pseudo
        self.email = email
        self.grade = grade

st.sidebar.title("Inscription")
pseudo = st.sidebar.text_input("Votre Pseudo")
email = st.sidebar.text_input("Votre Email")
grade = st.sidebar.selectbox("Abonnement", ["Gratuit (0€)", "Pro (19€)"])
st.title("Bienvenue sur mon SaaS")

if st.sidebar.button("Créer mon compte"):
    nouvel_utilisateur = Utilisateur(pseudo, email, grade)
    st.session_state['db_utilisateurs'].append(nouvel_utilisateur)
    st.success(f"Compte créé pour {nouvel_utilisateur.pseudo} !")

st.header("Base de données Clients")
donnees_pour_tableau = []
prix = 0
for user in st.session_state['db_utilisateurs']:
    if user.grade =="Pro (19€)":
        prix = 19
    else:
        prix = 0
    donnees_pour_tableau.append({
        "Pseudo": user.pseudo,
        "Email": user.email,
        "grade": user.grade,
        "prix": prix
    })

# 1. On crée le DataFrame officiel
df = pd.DataFrame(donnees_pour_tableau)

# 2. S'il y a des données, on calcule et on affiche
if not df.empty:
    # LA MAGIE PANDAS : Somme d'une colonne sans boucle !
    ca_total = df['prix'].sum() 
    
    # Widget spécial SaaS pour afficher les gros chiffres
    st.metric(label="Chiffre d'Affaires Mensuel Estimé", value=f"{ca_total} €")
    
    # On affiche le tableau
    st.dataframe(df)
    st.bar_chart(df['grade'].value_counts())




	 
