import psycopg2
import dotenv
import os

dotenv.load_dotenv(dotenv.find_dotenv())

sql_select_qry = (""" 
                SELECT fhp.policy_number, fhp.issue_date, fhp.status, fhp.policy_type, fhfh.funeral_home_name, fhfh.funeral_home_location, fhfh.fh_state, fha.agt_first_name,fha.agt_last_name,fhp.pfa, fhp.growth,fhpi.pi_first_name,fhpi.pi_last_name, fhpi.pi_address, fhpi.pi_city, fhpi.pi_st,fhpi.pi_zipcode
                FROM funeral_home.policy as fhp
                LEFT JOIN funeral_home.funeral_home as fhfh ON fhp.fh_id = fhfh.fh_id
                LEFT JOIN funeral_home.primary_insured as fhpi ON fhp.user_id = fhpi.user_id
                LEFT OUTER JOIN funeral_home.agent as fha ON fha.fh_id=fhfh.fh_id
                WHERE status = 'active';
            """)

def view_one_row_report(): 
    conn = None 
    try:
        conn = psycopg2.connect(
            database = 'Preneed',
            user = 'postgres',
            password = os.getenv('password'),
            host = 'localhost',
            port = '5432'
        )
        conn.autocommit = True #vs commit in order to connect 
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
view_one_row_report()