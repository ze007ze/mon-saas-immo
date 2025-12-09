import random
import sys

# --- 1. La Classe Personnage (Le Plan) ---
class Personnage:
    """Modélise un joueur unique avec ses attributs et ses actions."""
    
    # Le constructeur : il est appelé quand on crée un nouvel objet (ex: Personnage("Sylvio", ...))
    def __init__(self, nom, sexe, surnom, age, crush):
        # Définition des Attributs (Propriétés) de l'objet
        self.nom = nom
        self.sexe = sexe
        self.surnom = surnom
        self.age = age
        self.crush = crush
        # On stocke toutes les clés d'attributs dans une liste pour le random.sample plus tard
        self.attributs = ["sexe", "surnom", "age", "crush"]

    # Une Méthode : une fonction interne à l'objet.
    def donner_indice(self, cle_attribut):
        """Affiche l'indice correspondant à l'attribut demandé."""
        
        # NOTE : La valeur se trouve dans self.<cle_attribut>. Par exemple, si cle_attribut est "sexe",
        # la valeur est self.sexe. Pour simplifier, nous allons utiliser une manière propre d'accéder à l'attribut dynamique.
        # En Python, on peut utiliser getattr(self, cle_attribut) pour récupérer la valeur de l'attribut
        # dont le nom est contenu dans la variable cle_attribut (c'est plus avancé, mais très propre).
        
        # Utilisons l'accès direct pour simplifier :
        
        if cle_attribut == "sexe":
            # Reprenez votre ancienne logique d'affichage du sexe
            if self.nom in ["chiara", "kesya"]:
                 # self.sexe est la valeur du sexe de l'objet actuel
                 print(f"Cette chienne est une {self.sexe}.")
            else:
                 print(f"Cette personne est un {self.sexe}.")
        
        elif cle_attribut == "surnom":
            # Reprenez votre ancienne logique d'affichage du surnom
            print(f"Le surnom de cet eunuque c'est '{self.surnom}'.")
            
        elif cle_attribut == "age":
            # Reprenez votre ancienne logique d'affichage de l'âge
            print(f"La personne a {self.age} ans.")

        elif cle_attribut == "crush":
            # Reprenez votre ancienne logique d'affichage du crush
            if self.crush == 'beaucoup':
                print(f"Cette personne aime {self.crush} de personnes.")
            else:
                print(f"Cette personne aime {self.crush}.")
        
        else:
            print(f"Erreur: Attribut inconnu ({cle_attribut}).")


# --- 2. Création des Objets (Instances de la Classe) ---
# Le dictionnaire 'joueur' devient une LISTE d'objets (Instances)
LISTE_PERSONNAGES = [
    Personnage("sylvio", 'garçon', 'ibrahim', 18, 'beaucoup'),
    Personnage("bilal", 'Homme poilue', 'gros lardon', 18, 'beaucoup'),
    Personnage("chiara", 'femme en chaleur', 'la tana des neiges', 18, 'thomas'),
    Personnage("alexis", 'petit homme', 'aleskibidi', 17, 'beaucoup'),
    Personnage("mathys", 'garçon', 'le casse couilles', 18, 'kesya'),
    Personnage("alexandre", 'demi homme', 'le jeune parfais', 16, 'eline'),
    Personnage("oscar", 'HOMME', "l'aryan", 18, 'clemence'),
    Personnage("felix", 'HOMO', 'le petit parfais/casse couilles', 17, 'kesya'),
    Personnage("kesya", 'femelle', 'la pute asiatique', 17, 'felix'),
]


# --- 3. Logique du Jeu Principal (Similaire à avant) ---

# Choix aléatoire d'un objet Personnage dans la liste
personnage_a_deviner = random.choice(LISTE_PERSONNAGES)

# Les questions sont choisies directement à partir des attributs de l'objet
questions_choisies = random.sample(personnage_a_deviner.attributs, 4)

nombre_essais = 0 

print("--- Bienvenue dans le Qui est-ce ? Version POO ---")

for cle_attribut in questions_choisies:
    print('____________________________________________________________')
    nombre_essais += 1
    print(f"Indice {nombre_essais}:")
    
    # APPEL DE LA MÉTHODE : L'objet se charge d'afficher son propre indice
    # La logique est maintenant ENCAPSULÉE dans l'objet.
    personnage_a_deviner.donner_indice(cle_attribut)
    
    # Demande de l'idée du joueur (logique identique)
    idee_joueur = input("\nAlors, avez-vous une idée de qui est cette personne ? Entrez le prénom (ou 'non') : ").lower().strip()

    if idee_joueur == personnage_a_deviner.nom.lower():
        print(f"\n✅ BRAVO ! Vous avez trouvé '{personnage_a_deviner.nom}' en {nombre_essais} coup(s).")
        sys.exit()
    elif idee_joueur == "non":
        print('Fais pas ta petite. Poursuivons.')
        continue
    else:
        print("❌ Ce n'est pas la bonne personne. Réfléchissez mieux.")
        
# Fin
print("\n--- ÉCHEC ---")
print(f"Vous avez utilisé tous les indices. La personne à deviner était '{personnage_a_deviner.nom}'.")