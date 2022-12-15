{\rtf1\ansi\ansicpg1252\cocoartf2639
\cocoatextscaling0\cocoaplatform0{\fonttbl\f0\fswiss\fcharset0 Helvetica;}
{\colortbl;\red255\green255\blue255;}
{\*\expandedcolortbl;;}
\margl1440\margr1440\vieww11520\viewh8400\viewkind0
\pard\tx720\tx1440\tx2160\tx2880\tx3600\tx4320\tx5040\tx5760\tx6480\tx7200\tx7920\tx8640\pardirnatural\partightenfactor0

\f0\fs24 \cf0 import psycopg2\
from sql_queries import create_table_queries, drop_table_queries\
\
\
def create_database():\
    """\
    - Creates and connects to the sparkifydb\
    - Returns the connection and cursor to sparkifydb\
    """\
    \
    # connect to default database\
    conn = psycopg2.connect("host=127.0.0.1 dbname=studentdb user=student password=student")\
    conn.set_session(autocommit=True)\
    cur = conn.cursor()\
    \
    # create sparkify database with UTF8 encoding\
    cur.execute("DROP DATABASE IF EXISTS sparkifydb")\
    cur.execute("CREATE DATABASE sparkifydb WITH ENCODING 'utf8' TEMPLATE template0")\
\
    # close connection to default database\
    conn.close()    \
    \
    # connect to sparkify database\
    conn = psycopg2.connect("host=127.0.0.1 dbname=sparkifydb user=student password=student")\
    cur = conn.cursor()\
    \
    return cur, conn\
\
\
def drop_tables(cur, conn):\
    """\
    Drops each table using the queries in `drop_table_queries` list.\
    """\
    for query in drop_table_queries:\
        cur.execute(query)\
        conn.commit()\
\
\
def create_tables(cur, conn):\
    """\
    Creates each table using the queries in `create_table_queries` list. \
    """\
    for query in create_table_queries:\
        cur.execute(query)\
        conn.commit()\
\
\
def main():\
    """\
    - Drops (if exists) and Creates the sparkify database. \
    \
    - Establishes connection with the sparkify database and gets\
    cursor to it.  \
    \
    - Drops all the tables.  \
    \
    - Creates all tables needed. \
    \
    - Finally, closes the connection. \
    """\
    cur, conn = create_database()\
    \
    drop_tables(cur, conn)\
    create_tables(cur, conn)\
\
    conn.close()\
\
\
if __name__ == "__main__":\
    main()}