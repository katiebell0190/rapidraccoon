import psycopg2
import smtplib
import getpass
import dotenv
import os
from email import encoders
from email.mime.base import MIMEBase
from typing import Text
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

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
            password =  os.getenv('password'),
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
            password = os.getenv('password'),
            host = 'localhost',
            port = '5432'
        )
        conn.autocommit = True 
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

def print_csv_file():

    sql_select_qry = (""" 
                SELECT fhp.policy_number, fhp.issue_date, fhp.status, fhp.policy_type, fhfh.funeral_home_name, fhfh.funeral_home_location, fhfh.fh_state, fha.agt_first_name,fha.agt_last_name,fhp.pfa, fhp.growth,fhpi.pi_first_name,fhpi.pi_last_name, fhpi.pi_address, fhpi.pi_city, fhpi.pi_st,fhpi.pi_zipcode
                FROM funeral_home.policy as fhp
                LEFT JOIN funeral_home.funeral_home as fhfh ON fhp.fh_id = fhfh.fh_id
                LEFT JOIN funeral_home.primary_insured as fhpi ON fhp.user_id = fhpi.user_id
                LEFT OUTER JOIN funeral_home.agent as fha ON fha.fh_id=fhfh.fh_id
                WHERE status = 'active'
            """)

    conn = None 
    conn = psycopg2.connect(
        database = 'Preneed',
        user = 'postgres',
        password = os.getenv('password'),
        host = 'localhost',
        port = '5432'
    )
    conn.autocommit = True
    cur = conn.cursor()
    cur.execute(sql_select_qry)
    fetch_report = cur.fetchall()
    print(fetch_report)

    my_qry = f"COPY ({sql_select_qry}) TO STDOUT WITH CSV DELIMITER ',' HEADER;"
    with open(r'C:\Users\Owner\Desktop\Callers to Coders\Project\inforce.csv','w') as f:
        cur.copy_expert(my_qry,f)


def send_email():
    subject = input("Enter subject: ")
    body = input("Enter message: ")
    senders_email = 'katieb0190@outlook.com'
    receivers_email = ['katieb0190@outlook.com.','caitlin.waszgis@physiciansmutual.com','amaggioni@aiminstitute.org']
    password = getpass.getpass(prompt='Enter password: ')

    message = MIMEMultipart()
    message['From'] = senders_email
    message['To'] = ",".join(receivers_email)
    message['Subject'] = subject

    message.attach(MIMEText(body,'plain'))
    filename = r'C:\Users\Owner\Desktop\Callers to Coders\Project\inforce.csv'
    with open(filename,'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())

    encoders.encode_base64(part)
    part.add_header(
        'Content-Disposition',
        f'attachment; filename={filename}'
        )
    message.attach(part)
    text = message.as_string()
    with smtplib.SMTP("smtp.office365.com:587") as server:
        server.starttls()
        server.login(senders_email,password)
        server.sendmail(senders_email,receivers_email,text)
    print('Email sent')


def main():
    active = True
    while True:
        choice = int(input("Welcome to the Inforce Report App! \nSelect an option: \n[1] View Report \n[2] Print Report \n[3] Email Report\n"))
        if choice == 1:
            view_one_row_report()
        elif choice == 2:
            print_csv_file()
        elif choice == 3:
            send_email()
        else:
            print("Invalid selection.")

main()

