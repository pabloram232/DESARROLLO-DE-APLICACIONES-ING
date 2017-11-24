#Juan Pablo Ramirez Ibarra ---- GITI9072
import psycopg2
from config import config


def connect():
    """Conect to de postgres database server"""

    connection = None
    try:
        # read connection parameters
        params = config()
        # Connect to the PostgrSQL server
        print('Connecting to the PostgreSQL database.... ')
        connection = psycopg2.connect(**params)

        # create cursor
        cursor = connection.cursor()

        # execute a statement
        print('PostgreSQL database version')
        cursor.execute('SELECT version()')

        # Display the PostgreSQL database server version
        db_version = cursor.fetchone()
        print(db_version)

        cursor.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if connect() is not None:
            connection.close()
            print('Database connection closed')


if __name__ == '__main__':
    connect()
