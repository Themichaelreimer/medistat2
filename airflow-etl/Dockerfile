# The airflow team recommends extending the image to add your package requirements
FROM apache/airflow:2.6.2

# Build from project root, not from airflow-etl. This is so we can easily write a
# build command for cli.py from the project root
COPY airflow-etl/requirements.txt .

RUN pip install -r requirements.txt
