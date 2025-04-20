import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Chargement
df = pd.read_csv("data/fraud_data.csv")

X = df.drop("is_fraud", axis=1)
y = df["is_fraud"]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

model = RandomForestClassifier()
model.fit(X_train, y_train)

with open("api/model.pkl", "wb") as f:
    pickle.dump(model, f)

print("✅ Modèle entraîné et sauvegardé")
