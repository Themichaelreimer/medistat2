# Medistat2

The next iteration of Medistat, with a focus on Data Engineering technologies and skills

# Project Areas

## CLI
The scope of the CLI is running, building, and configuring the entire application easily.
Requirements for the CLI are stored in `commands/requirements.txt`

|Command | Args | Description|
|--------|------|------------|
|check_service_health| | Checks that all containers are healthy. Retries if the health status is starting.|
|help| | Displays usage and lists available commands. If you run `python3 cli.py` with no args, this runs by default.|

## Airflow-ETL
This module is responsible for all ETL related tasks across the project:
- Collecting public data into the Datalake
- Transforming and Loading into Data Warehouse
- Producing Data Marts if applicable

Most of the actual software engineering in this repo is here, with most of the rest of the project being config and testing.

## Commands
This folder supplies management commands and package requirements to the CLI.

## Config
This folder stores config files for docker services that get mounted into the containers

## Volumes
This folder is intentionally empty. Volumes will be predictably created here as needed, but are all in gitignore.
