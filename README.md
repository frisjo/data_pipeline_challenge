# data_pipeline_challenge

This repository contains files to build a data pipeline for Starwars data.

docker-compose.yml: file that spins up the PostgreSQL server
retrieve_datapy: a Python script that fetches data from SWAPI and stores it into the PostgreSQL database 

To start the database:
1. Clone the repository.
2. Install Docker Desktop (if not installed).
3. Wihtin the repository, where the docker-compose.yml is located run following command: docker-compose up -d
This is to create and start the container.
4. Run the retrieve_data.py script to fetch character data from SWAPI. This scripts creates a table in the swapi database in the PostgresSQL container and fills the table with the character data.

