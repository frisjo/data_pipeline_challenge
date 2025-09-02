import subprocess

# Install dependencies 
subprocess.run(["pip", "install", "-r", "requirements.txt"], check=True)
# Start the container
subprocess.run(["docker-compose", "up", "-d"], check=True)
# Run the python script for data collection and fetching
subprocess.run(["python", "retrieve_data.py"], check=True)
# Run the python script for automatic data collection task to be set up
subprocess.run(["python", "automatic_data_collection.py"], check=True)