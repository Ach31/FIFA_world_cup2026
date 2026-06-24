# 🌍 FIFA World Cup 2026 - Data Pipeline with Airflow, Docker, and Power BI

**Automatisation de la récupération, du traitement et de la visualisation des données des joueurs de la Coupe du Monde 2026.**

Ce projet utilise **Apache Airflow** pour orchestrer la récupération des données depuis Kaggle, les traiter avec Python, et les rendre disponibles pour une visualisation dans **Power BI**.

---

---

## 📌 **Fonctionnalités**
✅ **Récupération automatique** des données des joueurs depuis Kaggle (via `kagglehub`).
✅ **Traitement et sauvegarde** des données dans un fichier CSV (`players_updated.csv`).
✅ **Orchestration avec Airflow** pour une exécution planifiée (toutes les 6 heures ou manuellement).
✅ **Intégration avec Power BI** pour une visualisation interactive des données.

---

---

## 🛠 **Prérequis**
- [Docker Desktop](https://www.docker.com/products/docker-desktop/) (pour exécuter Airflow et PostgreSQL).
- [Power BI Desktop](https://powerbi.microsoft.com/desktop/) (pour visualiser les données).
- Un compte [Kaggle](https://www.kaggle.com/) et un token API (`kaggle.json`) pour accéder aux datasets.
- (Optionnel) Un compte [Power BI Service](https://app.powerbi.com/) pour publier et rafraîchir automatiquement les rapports.

---

---

## 📁 **Structure du projet**