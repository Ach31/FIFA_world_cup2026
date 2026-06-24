from datetime import datetime
from airflow import DAG
from airflow.operators.python import PythonOperator
from telecharger_donnees_kaggle import telecharger_et_sauvegarder_donnees

with DAG(
    dag_id="mise_a_jour_donnees",
    start_date=datetime(2026, 6, 23),
    schedule_interval="@once",
    catchup=False,
) as dag:

    telecharger = PythonOperator(
        task_id="telecharger_donnees",
        python_callable=telecharger_et_sauvegarder_donnees,
    )