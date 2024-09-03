-- Analysis Queries:

-- Create the table for artists

CREATE TABLE artists_data (
    artist_id SERIAL PRIMARY KEY,
    artist_name VARCHAR(255) NOT NULL,
    genre VARCHAR(50)
);

-- Create the table for songs

CREATE TABLE songs_data (
    song_id SERIAL PRIMARY KEY,
    artist_id INT REFERENCES artists_data(artist_id),
    song_title VARCHAR(255) NOT NULL,
    duration INT
);

-- Create the table for users (streamers)

CREATE TABLE users_data (
    user_id SERIAL PRIMARY KEY,
    age INT,
    location VARCHAR(255)
);

-- Create the table for streaming data

CREATE TABLE streams_data (
    stream_id SERIAL PRIMARY KEY,
    user_id INT REFERENCES users_data(user_id),
    song_id INT REFERENCES songs_data(song_id),
    stream_date DATE,
    stream_duration INT
);