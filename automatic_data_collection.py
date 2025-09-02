import subprocess

# Specifies name of task and script to run
task = "automatic_data_collection"
script_path = "retrieve_data.py"

# Command to create a schedueled task
command = [
    "schtasks",
    "/Create", # Schedules a new task
    "/SC", "DAILY", # Schedule type
    "/TN", task, # Name of task
    "/TR", f'python "{script_path}"', # Task/script to run
    "/F" # Overwrite if task alredy exists
]

# Creates the task 
try:
    result = subprocess.run(command, check=True, capture_output=True, text=True)
    print(result.stdout)
except subprocess.CalledProcessError as e:
    print(e.stderr)