import kagglehub
import pandas as pd
import os
# Download latest version
path = kagglehub.dataset_download("swaptr/fifa-wc-2026-players")
print("Path to dataset files:", path)

# 2. Trouve le fichier CSV dans le dossier téléchargé
files = os.listdir(path)
#print("Fichiers disponibles :", files)

# 3. Charge le fichier CSV dans un DataFrame Pandas
csv_file = os.path.join(path, files[0])  # Prend le premier fichier (à adapter si nécessaire)
df = pd.read_csv(csv_file, sep=",")
print(df.head())