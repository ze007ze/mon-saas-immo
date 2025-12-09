from fastapi import FastAPI
import numpy as np
from sklearn.linear_model import LinearRegression

# 1. Entraînement du Modèle (Global - Exécuté une seule fois au démarrage)
# C'est parfait de le faire ici pour la performance.
X = np.array([10, 20, 30, 40, 50]).reshape(-1, 1)
y = np.array([50, 70, 90, 110, 130])

modele = LinearRegression()
modele.fit(X, y)

# 2. Application FastAPI
app = FastAPI()

# 3. Endpoint
@app.post("/predict")
def predict_price(surface: float):
    # Préparation de la donnée
    x_input = np.array([[surface]]) # Manière plus directe de faire le reshape
    
    # Prédiction
    prediction_array = modele.predict(x_input)
    
    # CORRECTION CRITIQUE : 
    # On extrait la valeur unique (float) du tableau numpy
    # Sinon, FastAPI renverra une erreur de sérialisation JSON (TypeError).
    prix_final = float(prediction_array[0])
    
    # On crée le dictionnaire de réponse ICI (Scope local) pour la sécurité
    # Si on le fait en global, plusieurs utilisateurs se marcheraient dessus.
    return {
        "surface_m2": surface,
        "prix_estime": round(prix_final, 2),
        "devise": "k€"
    }
    