import psycopg2
from psycopg2 import sql
import json
import os

"""
Adding host_facts directly by editing awx db
"""


def fetch_inventory_id(host, database, user, password):
    
    """
    fetchign inventory_id
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
        
        
    # Insert JSON data into the PostgreSQL table
    try:
        
        cursor.execute(
                f"select id, name from main_inventory"
            )
        
        id_inventory_list = cursor.fetchall()
        
    except Exception as e:
        print(f"Error inserting data: {e}")
    finally:
        cursor.close()
        conn.close()
        print("Connection closed.")
        return id_inventory_list
    
    
def update_table(host, database, user, password, list_inventory):
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
        
        
    # # Load the JSON file
    # try:
    #     with open("data.json", "r") as file:
    #         json_data = json.load(file)  # Assumes the file contains a list of JSON objects
    # except Exception as e:
    #     print(f"Error reading the JSON file: {e}")
    #     exit()
    
    # Iterate through the inventory list and find corresponding JSON files
        for id, name in list_inventory:
            json_file_path = os.path.join('host_facts', f'{name}.json')  # File name directly without .json
            if os.path.exists(json_file_path):
                with open(json_file_path, "r") as file:
                    json_data = json.load(file)
                    # Insert JSON data into the PostgreSQL table
                    
                    print(id)
                
                    cursor.execute(
                        "UPDATE main_host set ansible_facts = %s where inventory_id = %s",
                        [json.dumps(json_data), id]  # Convert Python dictionary to JSON string
                        )
                    conn.commit()
                    print("JSON data inserted successfully.")
            else:
                print(f"Warning: JSON file for {name} not found at {json_file_path}")
    
                    
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
    
    list_inventory = fetch_inventory_id(host, database, user, password)

    update_table(host, database, user, password, list_inventory)
