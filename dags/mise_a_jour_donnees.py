from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from telecharger_donnees_kaggle import telecharger_et_sauvegarder_donnees

# ⚠️ Correction : Utilise datetime.now() au lieu de datetime.datetime.now()
with DAG(
    dag_id="mise_a_jour_donnees",
    start_date=datetime.now(),  # ✅ Correction ici
    schedule_interval="@once",
    catchup=False,
) as dag:

    telecharger = PythonOperator(
        task_id="telecharger_donnees",
        python_callable=telecharger_et_sauvegarder_donnees,
    )