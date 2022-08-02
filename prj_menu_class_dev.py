from typing_extensions import Self
import psycopg2

sql_select_qry = (""" 
                SELECT fhp.policy_number, fhp.issue_date, fhp.status, fhp.policy_type, fhfh.funeral_home_name, fhfh.funeral_home_location, fhfh.fh_state, fha.agt_first_name,fha.agt_last_name,fhp.pfa, fhp.growth,fhpi.pi_first_name,fhpi.pi_last_name, fhpi.pi_address, fhpi.pi_city, fhpi.pi_st,fhpi.pi_zipcode
                FROM funeral_home.policy as fhp
                LEFT JOIN funeral_home.funeral_home as fhfh ON fhp.fh_id = fhfh.fh_id
                LEFT JOIN funeral_home.primary_insured as fhpi ON fhp.user_id = fhpi.user_id
                LEFT OUTER JOIN funeral_home.agent as fha ON fha.fh_id=fhfh.fh_id
                WHERE status = 'active'
            """)

class Report:
    def __init__(self,menu,connect,fetch_one,fetch_all,print_CSV_file,send_email,close_connection):
        self.menu = menu
        self.connect = connect
        self.fetch_one = fetch_one
        self.fetch_all = fetch_all
        self.print_CSV_file = print_CSV_file
        self.send_email = send_email
        self.close_connection = close_connection

def menu():
    active = True
    while True:
        choice = int(input("Welcome to the Inforce Report App! \nSelect an option: \n[1] Connect to database \n[2] View Sample Record \n[3] View all records \n[4] Export to CSV file \n[4] Email CSV file \n[5] Close connection\n"))
        print(choice)

def fetch_one():
    conn = None
    try:
        conn = psycopg2.connect(
            database = 'Preneed',
            user = 'postgres',
            password = '08Donthate*', #look up how to hide this in a dev file
            host = 'localhost',
            port = '5432'
        )
        conn.autocommit = True
        cur = conn.cursor()
        print('PostgresSQL database version:')
        cur.execute(sql_select_qry)
        print("The number of rows:", cur.rowcount)
        db_version = cur.fetchone()
        print(db_version)
        cur.close()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Databse connection closed.')

def view_report_all():
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
        cur.execute(sql_select_qry)
        print("The number of rows:", cur.rowcount)
        db_version = cur.fetchall()
        print(db_version)
        cur.close()
    except (Exception,psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
            print('Databse connection closed.')





    
