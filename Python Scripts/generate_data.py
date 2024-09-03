import psycopg2
from faker import Faker
import pandas as pd

# Establish a connection to the PostgreSQL database Project Pyke

conn = psycopg2.connect(
   host="localhost",
   database="Project Pyke",
   user="postgres",
   password="Not available publicly",
   port="5432"
)

# Create a cursor object

cur = conn.cursor()

print("Connected to Project Pyke!")

# Initialize Faker for generating synthetic data

fake = Faker()

# Generate Users data

users_data = []
for _ in range(2000):
    users_data.append((
        fake.name(),
        fake.random_int(min=18, max=80),
        fake.city(),
        fake.random_element(elements=("Free", "Premium"))
    ))

# Insert Users data into the Users table

cur.executemany(
    "INSERT INTO Users (name, age, location, subscription_type) VALUES (%s, %s, %s, %s)",
    users_data
)

# Generate Artists data

artists_data = []
for _ in range(50):  # Generate 50 artists
    artists_data.append((
        fake.name(),
        fake.random_element(elements=("Pop", "Rock", "Jazz", "Classical", "Hip-hop")),
        fake.random_int(min=0, max=100)
    ))

# Insert Artists data into the Artists table

cur.executemany(
    "INSERT INTO Artists (name, genre, popularity_score) VALUES (%s, %s, %s)",
    artists_data
)

# Generate Songs data

songs_data = []
for i in range(1, 101):
    songs_data.append((
        f"Song {i}",
        fake.random_int(min=1, max=50),  # Random artist_id between 1 and 50
        fake.date_this_decade(),
        fake.random_element(elements=("Pop", "Rock", "Jazz", "Classical", "Hip-hop")),
        fake.random_int(min=120, max=360)
    ))

# Insert Songs data into the Songs table

cur.executemany(
    "INSERT INTO Songs (title, artist_id, release_date, genre, length) VALUES (%s, %s, %s, %s, %s)",
    songs_data
)

# Generate Streams data

streams_data = []
for _ in range(1000):
    streams_data.append((
        fake.random_int(min=1, max=2000),
        fake.random_int(min=1, max=100),
        fake.date_time_this_year(),
        fake.random_int(min=30, max=300),
        fake.city()
    ))

# Insert Streams data into the Streams table

cur.executemany(
    "INSERT INTO Streams (user_id, song_id, stream_date, stream_duration, location) VALUES (%s, %s, %s, %s, %s)",
    streams_data
)

# Commit the transaction

conn.commit()

# Close the connection

cur.close()
conn.close()

print("Data inserted successfully!")