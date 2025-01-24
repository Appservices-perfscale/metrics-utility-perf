import psycopg2
from psycopg2 import sql
import json

"""
Adding host_facts directly by editing awx db
"""

def update_table(host, database, user, password):
    """
    Function to update a table in a PostgreSQL database dynamically
    """
    try:
        # Connect to the PostgreSQL database
        conn = psycopg2.connect(
            host=host,
            database=database,
            user=user,
            password=password
        )

        # Create a cursor object to interact with the database
        cursor = conn.cursor()
        print(conn)

    except (Exception, psycopg2.Error) as error:
        print("Error while updating table:", error)
        
        
    # Load the JSON file
    try:
        with open("data.json", "r") as file:
            json_data = json.load(file)  # Assumes the file contains a list of JSON objects
    except Exception as e:
        print(f"Error reading the JSON file: {e}")
        exit()
        
        
    # Insert JSON data into the PostgreSQL table
    try:

        cursor.execute(
            "UPDATE main_host set ansible_facts = %s where id = 3014",
            [json.dumps(json_data)]  # Convert Python dictionary to JSON string
        )
        conn.commit()
        print("JSON data inserted successfully.")
    except Exception as e:
        print(f"Error inserting data: {e}")
        conn.rollback()
    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")

# Example usage:
if __name__ == "__main__":
    host = "54.164.45.196"
    database = "awx"
    user = "larry"
    password = "larry1"

    update_table(host, database, user, password)
