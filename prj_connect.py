import psycopg2

def connect():
    conn = None 
    try:
        conn = psycopg2.connect(
            database = 'Preneed',
            user = 'postgres',
            password = '08Donthate*', #look up how to hide this in a dev file
            host = 'localhost',
            port = '5432'
        )
        conn.autocommit = True #vs commit in order to connect 
        cur = conn.cursor()
        print('PostgresSQL database version:')
        cur.execute('SELECT version()')
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Databse connection closed.')