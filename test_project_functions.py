import psycopg2
import os

#Functions
#Login
    #getpass
#Menu
#connect to database
#Option1-Create Report = open report from database 
#Option2 = Generate from database into a csv file
#Option3 - email report to email address -user input or hard coded?
#error handling
#pandas
#numpy
#salting & hashing

sql_select_qry = (""" 
                SELECT fhp.policy_number, fhp.issue_date, fhp.status, fhp.policy_type, fhfh.funeral_home_name, fhfh.funeral_home_location, fhfh.fh_state, fha.agt_first_name,fha.agt_last_name,fhp.pfa, fhp.growth,fhpi.pi_first_name,fhpi.pi_last_name, fhpi.pi_address, fhpi.pi_city, fhpi.pi_st,fhpi.pi_zipcode
                FROM funeral_home.policy as fhp
                LEFT JOIN funeral_home.funeral_home as fhfh ON fhp.fh_id = fhfh.fh_id
                LEFT JOIN funeral_home.primary_insured as fhpi ON fhp.user_id = fhpi.user_id
                LEFT OUTER JOIN funeral_home.agent as fha ON fha.fh_id=fhfh.fh_id
                WHERE status = 'active';
            """)


class Report:
 pass

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

def view_one_row_report(): #actives():
    conn = None #does this need to be a function?
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
    conn = None #does this need to be a function?
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

def print_report():
    filename = r'C:\Users\Owner\Desktop\Callers to Coders\Project\inforce.txt'
    fname = os.path.join(os.path.dirname(__file__,filename))
    f = open(fname, 'x',)
    f.close()
    pass

def email_report():
    #distribute csv file to an email address
    #how to encrypte the file
    #input email address or generate email address?
    pass

preneed_object = Report()

def main():
    active = True
    while True:
        choice = int(input("Welcome to the Inforce Report App! \nSelect an option: \n[1] View Report \n[2] Print Report \n[3] Email Report\n"))
        if choice == 1:
            view_one_row_report()
    #function view report print(View Report)
            #print("view report") #this will be view_report function
        elif choice == 2:
            print("Print Report")
        elif choice == 3:
            print("email Report")
        else:
            print("Invalid selection.")
main()