import subprocess

def run() -> None:
    """
        This command builds all required docker images for deployment
    """

    return subprocess.run(['docker', 'build', '.', '--file', 'airflow-etl/Dockerfile', '-t', 'airflow-etl'])
