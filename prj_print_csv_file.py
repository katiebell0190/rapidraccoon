import psycopg2
import csv


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
        password = '08Donthate*', #look up how to hide this in a dev file
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
print_csv_file()