def connect():
    conn = None 
    conn = psycopg2.connect(
        database = 'Preneed',
        user = 'postgres',
        password = '08Donthate*', #look up how to hide this in a dev file
        host = 'localhost',
        port = '5432'
    )
    conn.autocommit = True #vs commit in order to connect 
    cur = conn.cursor()
    cur.execute(sql_select_qry)
    print('PostgresSQL database version:')

def view_select_one():
    cur.execute(sql_select_qry)
    db_version = cur.fetchone()
    print(db_version)

def view_select_all():
    cur.execute(sql_select_qry)
    db_version = cur.fetchall()
    print(db_version)

def close():
    cur.close()
    print('Databse connection closed.')