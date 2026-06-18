import matplotlib.pyplot as plt
import kagglehub
import os
import pandas as pd

# Download latest version
path = kagglehub.dataset_download("swaptr/fifa-wc-2026-players")
print("Path to dataset files:", path)

# 2. Trouve le fichier CSV dans le dossier téléchargé
files = os.listdir(path)
print("Fichiers disponibles :", files)

# 3. Charge le fichier CSV dans un DataFrame Pandas
csv_file = os.path.join(path, files[0])  # Prend le premier fichier (à adapter si nécessaire)
df = pd.read_csv(csv_file, sep=",")
df_france = df[df["team"] == "France"]
clubs = pd.unique(df_france["club"].dropna())
print(df_france)
print(len(df_france))

nb_per_club=[]
player_per_club=[]
for i in clubs:
    list_player = []
    
    nb=len(df_france[df_france["club"] == i])
    name = df_france[df_france["club"] == i]["player"]
    #print(df_france[df_france["club"] == i]["player"])
    player_per_club.append(name)
    print("nombre de joueur au club "+i+" : "+str(nb))
    nb_per_club.append(nb)
plt.bar(clubs, nb_per_club)
print(player_per_club)
plt.show()