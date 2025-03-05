import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 📂 Charger le fichier avec le bon séparateur
file_path = "altitude_bassin_garonne.csv"
df = pd.read_csv(file_path, sep=";")

# 🔍 Vérifier les colonnes disponibles
print(df.columns)

# 📊 Nettoyage des données
df["altitude"] = df["altitude"].str.replace(",", ".").astype(float)
df["longitude"] = df["longitude"].str.replace(",", ".").astype(float)
df["latitude"] = df["latitude"].str.replace(",", ".").astype(float)

# 📈 Tracer le graphique (profil altimétrique en fonction de la longitude)
plt.figure(figsize=(12, 6))
sns.lineplot(x=df["longitude"], y=df["altitude"], marker="o", linestyle="-", color="b")

plt.xlabel("Longitude")
plt.ylabel("Altitude (m)")
plt.title("Profil altimétrique du bassin de la Garonne")
plt.grid(True)
plt.show()
