# data_pipeline_challenge

This repository contains files to build a data pipeline for retrieving and storing Starwars data from SWAPI to a PostgresSQL database.

Files in repository:
* automatic_data_collection.py: python script that creates a task in Windows Task Scheduler, for automatic daily data collection
* docker-compose.yml: file that spins up the PostgreSQL server
* requirements.txt: contains all dependencies needed for the project
* retrieve_data.py: a Python script that fetches character data from SWAPI (https://swapi.py4e.com/) and stores it into the PostgreSQL database
* run_project: file to run to set up project - first the script installs the required dependencies, then the script spins up the PostgreSQL server and the swapi database, it collects data from swapi and adds it to the characters table, the script also creates the automatic data collection taks in Windows Task Scheduler, such that data is collected daily to the database 

Set up the project:
1. Clone repository
2. Download docker desktop
3. In the directory where the repo is located run: pyhton run_project.py