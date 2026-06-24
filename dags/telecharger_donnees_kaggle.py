import kagglehub
import pandas as pd
import os

def telecharger_et_sauvegarder_donnees():
    # 1. Télécharger les données depuis KaggleHub
    print("📥 Téléchargement des données depuis KaggleHub...")
    path = kagglehub.dataset_download("swaptr/fifa-wc-2026-players")

    # 2. Trouver le fichier CSV dans le dossier téléchargé
    files = os.listdir(path)
    csv_file = os.path.join(path, files[0])  # Prend le premier fichier CSV

    # 3. Charger le CSV dans un DataFrame
    df = pd.read_csv(csv_file, sep=",")

    # 4. Sauvegarder le DataFrame en CSV dans /opt/airflow/data/
    output_path = "/opt/airflow/data/players_updated.csv"
    df.to_csv(output_path, index=False)
    print(f"✅ Données sauvegardées dans {output_path}")

    # 5. Retourner le chemin du CSV pour les tâches suivantes
    return output_path