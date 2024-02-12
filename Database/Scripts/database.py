import psycopg2
from sqlalchemy import create_engine

dbname = 'jairBets'
user = 'postgres'
password = '123'
host = 'localhost'
port = '5432'

def connect_to_database():
    try:
        conn = psycopg2.connect(
            dbname=dbname,
            user=user,
            password=password,
            host=host,
            port=port
        )
        return conn
    except psycopg2.Error as e:
        print("Error connecting to the database:", e)
        return None

def database_engine():
    db_string = f'postgresql://{user}:{password}@{host}:{port}/{dbname}'
    try:
        # Create the database engine
        engine = create_engine(db_string)
        return engine
    except Exception as e:
        print("Error connecting to the database:", e)
        return None
