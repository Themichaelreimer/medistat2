import os, sys


def run() -> None:
    if "--airflow" in sys.argv:
        os.system("docker compose -f docker-compose-airflow.yml run airflow-init")
