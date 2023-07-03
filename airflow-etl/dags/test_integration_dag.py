"""
    This DAG tests that the Airflow worker container can communicate with all the services it needs to
"""

from airflow import DAG
from airflow.decorators import task
from datetime import datetime, timedelta

with DAG(
    "airflow_integration_test",
    description="Tests relevent components can communicate with Airflow",
    start_date=datetime(2023, 1, 1),
    schedule=timedelta(days=1),
    catchup=False,
    tags=["Test"],
    default_args={
        # "email": ['YOUR_EMAIL_HERE']
        # "email_on_failure": True
        "retries": 3,
        "retry_delay": timedelta(minutes=2),
    },
) as test_dag:

    @task
    def run():
        print("Hello world")

    run()
