{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 # DROP TABLES\
\
songplay_table_drop = "DROP TABLE IF EXISTS songplays;"\
user_table_drop = "DROP TABLE IF EXISTS users;"\
song_table_drop = "DROP TABLE IF EXISTS songs;"\
artist_table_drop = "DROP TABLE IF EXISTS artists;"\
time_table_drop = "DROP TABLE IF EXISTS time;"\
\
# CREATE TABLES\
\
songplay_table_create = ("""CREATE TABLE IF NOT EXISTS songplays (\
    songplay_id int PRIMARY KEY NOT NULL, \
    start_time timestamp NOT NULL, \
    user_id int NOT NULL, \
    level int NOT NULL, \
    song_id varchar NOT NULL, \
    artist_id varchar NOT NULL, \
    session_id int NOT NULL, \
    location varchar NOT NULL, \
    user_agent varchar NOT NULL);\
""")\
\
user_table_create = ("""CREATE TABLE IF NOT EXISTS users (\
    user_id int PRIMARY KEY NOT NULL, \
    first_name varchar NOT NULL, \
    last_name varchar NOT NULL, \
    gender varchar NOT NULL, \
    level varchar NOT NULL);\
""")\
\
song_table_create = ("""CREATE TABLE IF NOT EXISTS songs (\
    song_id varchar PRIMARY KEY NOT NULL,\
    title varchar NOT NULL, \
    artist_id varchar NOT NULL, \
    year int NOT NULL, \
    duration int NOT NULL);\
""")\
\
artist_table_create = ("""CREATE TABLE IF NOT EXISTS artists (\
    artist_id varchar PRIMARY KEY NOT NULL, \
    name varchar NOT NULL, \
    location varchar NOT NULL, \
    latitude float NOT NULL, \
    longitude float NOT NULL);\
""")\
\
time_table_create = ("""CREATE TABLE IF NOT EXISTS time (\
    start_time timestamp PRIMARY KEY NOT NULL, \
    hour int NOT NULL, \
    day int NOT NULL, \
    week int NOT NULL, \
    month int NOT NULL, \
    year int NOT NULL, \
    weekday int NOT NULL);\
""")\
\
# INSERT RECORDS\
\
songplay_table_insert = ("""INSERT INTO songplays (songplay_id, start_time, user_id, level, song_id, artist_id, session_id, location, user_agent)\
VALUES (%s, %s, %s, %s, %s)\
ON CONFLICT DO NOTHING;\
""")\
\
user_table_insert = ("""INSERT INTO users (user_id, first_name, last_name, gender, level)\
VALUES (%s, %s, %s, %s, %s)\
ON CONFLICT DO NOTHING;\
""")\
\
song_table_insert = ("""INSERT INTO songs (song_id, title, artist_id, year, duration\
)\
VALUES (%s, %s, %s, %s, %s)\
ON CONFLICT DO NOTHING;\
""")\
\
artist_table_insert = ("""INSERT INTO artists (artist_id, name, location, latitude, longitude)\
VALUES (%s, %s, %s, %s, %s)\
ON CONFLICT DO NOTHING;\
""")\
\
\
time_table_insert = ("""INSERT INTO time (start_time, hour, day, week, month, year, weekday)\
VALUES (%s, %s, %s, %s, %s)\
ON CONFLICT DO NOTHING;\
""")\
\
# FIND SONGS\
# you'll need to get the song ID and artist ID by querying the songs and artists tables to find matches based on song title, artist name, and song duration time. join song and artist tables by artist id, join three tables?\
\
song_select = ("""SELECT song_id and artist_id FROM songs;\
""")\
\
# elect the timestamp, user ID, level, song ID, artist ID, session ID, location, and user agent and set to songplay_data\
\
#songplay_data = \
\
# QUERY LISTS\
\
create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]\
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]}