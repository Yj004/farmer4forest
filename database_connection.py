# database-connection.py

import psycopg2
from psycopg2 import sql

# Database connection details
DB_CONFIG = {
    "host": "localhost",
    "port": 5432,
    "dbname": "postgres",
    "user": "postgres",
    "password": "yashs7221",
    "connect_timeout": 10,
    "sslmode": "prefer"
}

# Connect to the PostgreSQL database
def connect_to_db():
    try:
        connection = psycopg2.connect(**DB_CONFIG)
        print("Connected to the database successfully!")
        return connection
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None
