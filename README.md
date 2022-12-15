# Udacity - DataModeling With Postgres
# Sparkify Database

## 1. Purpose of the Sparkify database.

This database is a collection of data for Sparkify's new song app, which contains information on songs on the app, song artists, listening times, app users, and the amount of plays with certain songs. This database is specifically helpful with Sparkify in terms of analyzing the type of music people are interested in and if the range of songs that Sparkify contains in their app is desired by the majority of the population. With the accessibility to analyze this data, Sparkify's team will be able best inform the other departments on how to best target their current users and potential future users.

## 2. Schema and ETL pipeline design.

In this database, I have created a star schema design with the tables songplays in the center and the tables users, songs, artists, and time connected to it. Each file in this database has a purpose. The data file contains all of the Sparkify data in the format of JSON files, this data is accessed and extracted from the other files. The create_tables.py file creates the sparkify database and connects to it, it then connects to the sql_queries.py, which drops the database tables if they exist, then creates the tables, inserts records into them, and queries them. The etl.ipynb file performs the ETL process by processing one file from each area in the data files, transforming them into clean tables, and then loading them into the database. The file etl.py essentially performs the same way as the etl.ipynb except this file contains the ETL pipeline for all the data files to go into the database. The test.ipynb is a testing file to ensure that data was successfully loaded into the database. Finally the run_file.ipynb is the file that runs all of the separate files in one place, so that the ETL process is simpler. The run_file calls to the create_tables.py file to establish a connection to the Sparkify database and to create all of the neccessary tables and queries. Then this file runs the etl.py file to set up the ETL pipeline, and then runs the test.ipynb file to check that everything was loaded successfully. When running this database, kernals must all be restarted so that multiple connections to the Sparkify database are not in place. Then the run_file can be completely run to retrieve the database data.

### Sparkify Database Files:

- data (contains Sparkify data in JSON formats)
- create_tables.py
- etl.ipynb
- etl.py
- sql_queries.py
- test.ipynb
- run_file.ipynb
