import requests
import psycopg2 # PostgreSQL database adapter for Python

# Function to get data from SWAPI
def get_SWAPI_data(url):
    response = requests.get(url)
    return response

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
    # Remove existing character table, in case of changed attributes 
    cur.execute("DROP TABLE IF EXISTS characters")
    # Create character table with the specified attributes 
    columns = ", ".join([f"{attr} TEXT" for attr in attributes]) # Change TEXT to other data types if needed (type(attr))?
    # Create 'character' table if not exists, add primary key column + the attributes
    query = f"""
        CREATE TABLE IF NOT EXISTS characters (
            id SERIAL PRIMARY KEY,
            {columns}
        )
    """
    cur.execute(query) # Excecute SQL command

# Fill character table with data from SWAPI
def fill_table(response, attributes, cur):
    # Loop trough all pages of data
    while response.status_code == 200:
        data = response.json()
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
        # Break loop at last page
        if data['next'] == None:
            break

        # Get response for next page
        response = get_SWAPI_data(data['next'])

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
    cur.execute("SELECT * FROM characters") # * retrieves all columns from specified table
    rows = cur.fetchall() # fetchall(): cursor method that retrieves all rows of the query
    print("Following characters and attributes can be found in the characters table:")
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