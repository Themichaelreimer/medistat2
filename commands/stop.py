import os, sys
from .common.docker_helpers import (
    detect_docker_compose_command,
    ensure_env_file_exists,
    get_docker_project_name,
    get_docker_compose_version,
)


def run() -> None:
    ensure_env_file_exists()
    command = detect_docker_compose_command()
    project_name = get_docker_project_name()
    compose_version = get_docker_compose_version()

    if compose_version[0] != "2":
        print(
            f"Please ensure you're running docker compose version 2.xx. Detected version {compose_version}"
        )
        exit(1)

    if "--airflow" in sys.argv:
        os.system(f'bash -c "{command} -f docker-compose-airflow.yml -p {project_name} down "')
    else:
        os.system(f'bash -c "{command} -f docker-compose.yml -p {project_name} down"')
