import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

# 1. Les Données d'Exemple (Le Manuel scolaire)
# On imagine quelques appartements vendus à Nancy
donnees = {
    'surface': [20, 30, 40, 50, 60, 80, 100],  # m²
    'prix': [60000, 85000, 110000, 140000, 165000, 220000, 280000], # €
    'nb_pieces': [1, 1, 2, 2, 3, 4, 5]
}
df = pd.DataFrame(donnees)

# 2. La Préparation
# X = Les indices (Surface)
# y = La réponse à trouver (Prix)
X = df.drop(columns=['prix'])
y = df['prix']

# 3. La Création du Cerveau (Modèle Linéaire)
model = LinearRegression()

# 4. L'Entraînement (Le "fit")
# C'est là que l'IA trace la droite parfaite entre les points
print("🧠 Entraînement de l'IA en cours...")
model.fit(X, y)
print("✅ Entraînement terminé !")

# 5. Le Test rapide
donnees_a_tester=[[45, 2]]

prediction = model.predict(donnees_a_tester)
print(f"Test : Un appart de 45m² et 2 pièces est estimé à {prediction[0]:.2f} €")
#print(prediction)
# 6. La Sauvegarde (Le Diplôme)
# On enregistre le cerveau entraîné dans un fichier
joblib.dump(model, 'modele_immo.pkl')
print("💾 Modèle sauvegardé sous 'modele_immo.pkl'")