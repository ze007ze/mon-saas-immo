import numpy as np
from sklearn.linear_model import LinearRegression
import joblib

X=np.array([10, 20, 30, 40, 50]).reshape(-1,1)
y=np.array([50, 70, 90, 110, 130]).reshape(-1, 1)
modele= LinearRegression()
modele.fit(X, y)
modele.score(X, y)
x=np.array([35]).reshape(-1, 1)
w=np.array([45]).reshape(-1, 1)
pre_01=modele.predict(x)



joblib.dump(modele, "modele_immobilier_v2.joblib")
w=np.array([45]).reshape(-1, 1)
modele_charge=joblib.load("modele_immobilier_v2.joblib")
pre_02=modele_charge.predict(w)
print(pre_02)