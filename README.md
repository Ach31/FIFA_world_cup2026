# 📌 FIFA World Cup 2026 - Data Pipeline

Automatisation de la récupération, du traitement et de la visualisation des données des joueurs de la Coupe du Monde 2026 avec **Apache Airflow**, **Docker**, **Python** et **Power BI**.

---

## 📁 Structure du projet

```
.

FIFA_WORLD_CUP2026/
│
├── dags/                          # Dossier pour les workflows Airflow
│   ├── mise_a_jour_donnees.py     # DAG principal pour orchestrer le pipeline
│   └── telecharger_donnees_kaggle.py # Script pour télécharger les données depuis Kaggle
│
├── data/                          # Dossier pour stocker les données
│   └── players_updated.csv        # Fichier CSV généré par le pipeline
│
├── docker-compose.yml             # Configuration Docker pour Airflow + PostgreSQL
│
└── README.md                      # Documentation du projet
```

---

## 🚀 Installation et exécution


### 1️⃣ **Exécution locale (avec Docker)**

#### **Prérequis**
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) installé sur votre machine.
- Un compte [Kaggle](https://www.kaggle.com/) et un **token API** (`kaggle.json`).
  *(Pour obtenir votre token : [Kaggle → Settings → API](https://www.kaggle.com/settings).)*

#### **Étapes**
1. **Cloner ou télécharger** le projet sur votre machine.
2. **Placer le fichier `kaggle.json`** à la racine du projet.
3. **Modifier le `docker-compose.yml`** pour monter `kaggle.json` dans le conteneur :
   ```yaml
   volumes:
     - ./kaggle.json:/root/.kaggle/kaggle.json
4. **Construire et lancer les conteneurs** :
```
docker-compose down -v
docker-compose up --build
```
5. **Accéder à l'interface Airflow** :
Ouvrez votre navigateur et allez sur :
**http://localhost:8080**
(Identifiants par défaut : admin / admin.)

---
## ✨ Fonctionnalités

- **Récupération automatique des données** :
Le pipeline télécharge les dernières données des joueurs depuis le dataset Kaggle swaptr/fifa-wc-2026-players via kagglehub.

- **Traitement et sauvegarde** :
Les données sont traitées avec Pandas et sauvegardées dans un fichier CSV (players_updated.csv) dans le dossier data/.

- **Orchestration avec Airflow** :
Le workflow est planifié et exécuté automatiquement (ex: toutes les 6 heures) ou manuellement via l'interface Airflow.

- **Intégration avec Power BI** :
Le fichier CSV généré peut être importé dans Power BI pour créer des visualisations interactives (ex: nombre de joueurs par position, par équipe, etc.).

---
## 🛠 Technologies utilisées

- **Orchestration** :

- **Apache Airflow 2.8.1** : [Apache Airflow](https://airflow.apache.org/) (pour l'automatisation des workflows).

- **Backend** :

- **Python 3.9+** : [Python 3.9+](https://www.python.org/) (pour les scripts de traitement).
- **Pandas** : [Pandas](https://pandas.pydata.org/) (pour la manipulation des données).
- **KaggleHub** : [KaggleHub](https://github.com/Kaggle/kagglehub) (pour télécharger les datasets depuis Kaggle).

- **Base de données** :

- **PostgreSQL 13** : [PostgreSQL 13](https://www.postgresql.org/) (pour stocker les métadonnées d'Airflow).

- **Conteneurisation** :

- **Docker** : [Nginx Alpine](https://hub.docker.com/_/nginx) (pour servir l'application)(pour déployer Airflow et PostgreSQL).

- **Visualisation** :

- **Power BI** : [Power BI](https://www.microsoft.com/en-us/power-platform/products/power-bi/) (pour l'analyse et les tableaux de bord).

---
## 🤝 Contribuer

Les contributions sont les bienvenues ! Ouvrez une *issue* ou soumettez une *pull request* pour proposer des améliorations.

---
## 📜 Licence

Ce projet est sous licence MIT. Vous êtes libre de l'utiliser, le modifier et le distribuer.


