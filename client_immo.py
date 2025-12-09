import requests

url = 'http://127.0.0.1:8000/predict'
reponse = requests.post(url, params = {'surface':50})
data = reponse.json()
print(f"Le serveur IA estime le bien à {float(data['prix_estime'])} k€")