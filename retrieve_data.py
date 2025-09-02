import requests
import psycopg2 # PostgreSQL database adapter for Python

# Function to get data from SWAPI
def get_SWAPI_data(url):
    response = requests.get(url)
    return response.json()

# Connect to PostgreSQL, swapi db
def connect_to_db():
    conn = psycopg2.connect(
        dbname="swapi",
        user="user",
        password="password",
        host="localhost",
        port="5432"
    )
    return conn

# Create a character table in the swapi db
def create_table(cur, attributes):
    # remove existing character table, in case of changed attributes 
    cur.execute("DROP TABLE IF EXISTS characters")
    columns = ", ".join([f"{attr} TEXT" for attr in attributes])
    query = f"""
        CREATE TABLE IF NOT EXISTS characters (
            id SERIAL PRIMARY KEY,
            {columns}
        )
    """
    cur.execute(query)

# Fill character table with data from SWAPI
def fill_table(data, attributes, cur):
    characters = data['results']
    columns = ", ".join([f"{attr}" for attr in attributes])
    # print("columns", columns)
    for character in characters:
        values = tuple(character[attr] for attr in attributes)
        # Since number of attributes can vary, create placeholders dynamically
        placeholders = ", ".join(["%s"] * len(attributes))
        # print("values", values)
        # print("placeholders", placeholders)
        cur.execute(
            f"INSERT INTO characters ({columns}) VALUES ({placeholders})",
            values
        )

# Connect, create table, and fill table 
def data_to_db(data, attributes):
    # Connect to swapi db
    conn = connect_to_db()
    # Create object to interact with db
    cur = conn.cursor()
    # Create charater table if not exists
    create_table(cur, attributes)
    # Save changes
    conn.commit()
    # Insert character data
    fill_table(data, attributes, cur)
    # Save changes
    conn.commit()

    # Check content of character table in db
    # Query and print all rows
    cur.execute("SELECT * FROM characters")
    rows = cur.fetchall()
    for row in rows:
        print(row)

    # Close communication with the database
    cur.close()
    conn.close()

# Fetch data from SWAPI
data = get_SWAPI_data("https://swapi.py4e.com/api/people/")
# Specify which attributes of the characters to store in table
attributes = ['name', 'height', 'mass', "eye_color"]
data_to_db(data, attributes)

