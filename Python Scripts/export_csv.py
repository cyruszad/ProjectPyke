import psycopg2
import pandas as pd

# Connect to PostgreSQL database

conn = psycopg2.connect(
   host="localhost",
   database="Project Pyke",
   user="postgres",
   password="Not Available Publicly",
   port="5432"
)

# Query data from Users table

users_df = pd.read_sql_query("SELECT * FROM Users", conn)
users_df.to_csv('users_data.csv', index=False)

# Query data from Artists table

artists_df = pd.read_sql_query("SELECT * FROM Artists", conn)
artists_df.to_csv('artists_data.csv', index=False)

# Query data from Songs table

songs_df = pd.read_sql_query("SELECT * FROM Songs", conn)
songs_df.to_csv('songs_data.csv', index=False)

# Query data from Streams table

streams_df = pd.read_sql_query("SELECT * FROM Streams", conn)
streams_df.to_csv('streams_data.csv', index=False)

# Close the connection

conn.close()

print("Data exported to CSV files successfully!")