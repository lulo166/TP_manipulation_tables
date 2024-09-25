import sqlite3

# Connect to the database
conn = sqlite3.connect('communes_nord.db')

# Create a cursor object
cursor = conn.cursor()

# Execute the query to get table information
cursor.execute("PRAGMA table_info(evolution);")

# Fetch all results
columns = cursor.fetchall()

# Print the primary key columns
for column in columns:
    if column[5]:  # The 6th element (index 5) indicates if the column is a primary key
        print(f"Primary Key Column: {column[1]}")

# Close the connection
conn.close()
