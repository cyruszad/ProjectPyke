-- Analysis Queries:

-- 1. Total number of streams per artist

SELECT a.artist_name, COUNT(s.stream_id) AS total_streams
FROM artists_data a
JOIN songs_data so ON a.artist_id = so.artist_id
JOIN streams_data s ON so.song_id = s.song_id
GROUP BY a.artist_name
ORDER BY total_streams DESC;

-- 2. Average stream duration per artist

SELECT a.artist_name, AVG(s.stream_duration) AS avg_stream_duration
FROM artists_data a
JOIN songs_data so ON a.artist_id = so.artist_id
JOIN streams_data s ON so.song_id = s.song_id
GROUP BY a.artist_name
ORDER BY avg_stream_duration DESC;

-- 3. Stream counts by genre

SELECT a.genre, COUNT(s.stream_id) AS total_streams
FROM artists_data a
JOIN songs_data so ON a.artist_id = so.artist_id
JOIN streams_data s ON so.song_id = s.song_id
GROUP BY a.genre
ORDER BY total_streams DESC;

-- 4. Stream count by user location

SELECT u.location, COUNT(s.stream_id) AS total_streams
FROM users_data u
JOIN streams_data s ON u.user_id = s.user_id
GROUP BY u.location
ORDER BY total_streams DESC;

-- 5. Number of unique users per artist

SELECT a.artist_name, COUNT(DISTINCT s.user_id) AS unique_users
FROM artists_data a
JOIN songs_data so ON a.artist_id = so.artist_id
JOIN streams_data s ON so.song_id = s.song_id
GROUP BY a.artist_name
ORDER BY unique_users DESC;