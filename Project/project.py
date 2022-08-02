import psycopg2

print("Welcome to the Preneed Application")
print("What would you like to do?")
choice = int(input("\n[1] Create Report \n[2] Print report \n[3] Email Report" ))

# #Class 
# for i in choice == 1:
#     #Select from everythig

# def create_db():
#     return(
#         "CREATE DATABASE preneedl;"
#     )

# conn = None
# try:
#     conn = psycopg2.connect(
#         database = 'postgres',
#         user = 'postgres'
#         password = '08Donthate*' #look up how to hide this in a dev file
#         host = 'localhost',
#         port = '5432'
#     )
#     conn.autocommit = True
#     cur = conn.cursor()

#     preneed1_db = create_db
#     cur.execute(preneed1_db)
#     conn.commit()
#     print('[+] Database Created!')
# except(Exception,psycopg2.DatabaseError) as error:
#     print('[-] Failed to connect.')
#     conn.rollback()
# finally:
#     if conn is not None:
#         conn.close()

# def create_table():
#     return(
#         """
#         CREATE TABLE funeral(
#             branch_id SERIAL PRIMARY KEY,
#             user_id  INT UNIQUE NOT NULL,
#             policy_number INT,
#             funeral_home_name VARCHAR (155),
#             funeral_home_location VARCHAR (155),
#             city VARCHAR (155),
#             fh_state VARCHAR (2),
#             zipcode VARCHAR (10),
#             PFA INT,
#             growth INT,
#             PFA_with_Growth INT
#             );
        
#         """
#     )