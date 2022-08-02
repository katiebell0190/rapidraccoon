import psycopg2

# def get_connection():
#     try:
#         conn= psycopg2.connect(
#         database= 'tight_database',
#         user= 'postgres',
#         password= '08Donthate*',
#         host='localhost',
#         port='5432'
#     )
#         if conn is not None:
#             print("[+] Connection established!")
#         else:
#             print('[-] Connection failed.')
#     except(Exception, psycopg2.DatabaseError) as error:
#         print((error))
#     finally:
#         if conn is not None:
#             conn.close()
#             print("[+] Connection closed.")

# get_connection()

# conn= psycopg2.connect(
# database= 'tight_database',
# user= 'postgres',
# password= '08Donthate*',
# host='localhost',
# port='5432'
# )

# cur = conn.cursor()
# cur.execute('SELECT * FROM customer;')

# print(cur.fetchone(),'\n')
# print(cur.fetchmany(3)) #list of tuples that gets
# print(cur.fetchall())

# cur.close()
# conn.close()

# try:
#     conn= psycopg2.connect(
#     database= 'tight_database',
#     user= 'postgres',
#     password= '08Donthate*',
#     host='localhost',
#     port='5432'
#     )

# cur = conn.cursor()
# # create_table = """CREATE TABLE department(
# #                 id SERIAL PRIMARY KEY,
# #                 product_name VARCHAR(255) NOT NULL,
# #                 price MONEY NOT NULL);"""

# cur.execute(create_table)
# # conn.commit()
# # conn.rollback()

# insert_value = """INSERT INTO department(product_name,price)
#                   Values
#                     ('apple',0.45);
#             """
# cur.execute(insert_value)
# conn.commit()
# print('{=} Database updated! ')
# cur.close()
# conn.close()

# try:
#     conn = psycopg2.connect(
#         database = 'postgres',
#         user = 'postgres',
#         password = '08Donthate*',
#         host = 'localhost',
#         port = '5432'
#     )
#     conn.autocommit = True
#     cur = conn.cursor()
#     create_db = 'CREATE DATABASE social;'
#     cur.execute(create_db)
#     conn.commit()
#     print("[+] Database created!")

# except(Exception,psycopg2.DatabaseError) as error:
#     print('Failed to create database'.format(error))
#     conn.rollback()
# conn.close()

#SQL TRANSACTION - 
#ACID - atomicity, consistency, Isolation, Durability

#countries, states, cities, users, posts, comments, likes, message, following

def create_tables():
    return(
        """
        CREATE TABLE countries(
            country_id SERIAL,
            country_name VARCHAR(50) NOT NULL,
            PRIMARY KEY(country_id),
            UNIQUE(country_name)
            );
        CREATE TABLE states(
            state_id SERIAL,
            state_name VARCHAR(50) NOT NULL,
            country_id INT NOT NULL,
            PRIMARY KEY(state_id),
            FOREIGN KEY(country_id) REFERENCES countries(country_id),
            UNIQUE(state_name,country_id)
            );
        CREATE TABLE cities(
            city_id SERIAL,
            city_name VARCHAR(50) NOT NULL,
            state_id INT NOT NULL,
            PRIMARY KEY(city_id),
            FOREIGN KEY(state_id) REFERENCES states(state_id)
            );
        CREATE TABLE users(
            user_id SERIAL,
            username VARCHAR(50) NOT NULL,
            password VARCHAR(50) NOT NULL,
            email VARCHAR(50) NOT NULL,
            city_id INT NOT NULL,
            profile_pic_url VARCHAR(255),
            dob DATE NOT NULL,
            date_updated DATE,
            PRIMARY KEY(user_id),
            FOREIGN KEY(city_id) REFERENCES cities(city_id),
            UNIQUE(username,email)
            );
        CREATE TABLE posts(
            post_id SERIAL,
            user_id INT NOT NULL,
            caption VARCHAR(255),
            date_created DATE NOT NULL,
            date_updated DATE,
            PRIMARY KEY(post_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id)
            );
        CREATE TABLE comments(
            comment_id SERIAL,
            post_id INT NOT NULL,
            user_id INT NOT NULL,
            content TEXT,
            date_created DATE NOT NULL,
            date_updated DATE,
            PRIMARY KEY(comment_id),
            FOREIGN KEY(post_id) REFERENCES posts(post_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id)
            );
        CREATE TABLE likes(
            user_id INT NOT NULL,
            post_id INT NOT NULL,
            date_created DATE NOT NULL,
            PRIMARY KEY(user_id,post_id),
            FOREIGN KEY(post_id) REFERENCES posts(post_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id)
            );
        CREATE TABLE messages(
            message_id SERIAL,
            post_id INT NOT NULL,
            user_id INT NOT NULL,
            content TEXT,
            date_created DATE NOT NULL,
            date_updated DATE,
            PRIMARY KEY(message_id),
            FOREIGN KEY(post_id) REFERENCES posts(post_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id)
            );
        CREATE TABLE following(
            following_id SERIAL,
            user_id INT NOT NULL,
            date_created DATE NOT NULL,
            PRIMARY KEY(following_id,user_id),
            FOREIGN KEY(user_id) REFERENCES users(user_id),
            FOREIGN KEY(following_id) REFERENCES users(user_id)
            );
        """
    )

def create_db():
    return(
        "CREATE DATABASE social;"
    )

conn = None
try:
    conn = psycopg2.connect(
        database = 'social',
        user = 'postgres',
        password = '08Donthate*',
        host = 'localhost',
        port = '5432'
    )
    conn.autocommit = True
    cur = conn.cursor()
    social_tables = create_tables()
    cur.execute(social_tables)
    conn.commit()
    print('[+] Tables created!')

except(Exception,psycopg2.DatabaseError) as error:
    print("[-] Failed to connect.")
    conn.rollback()

finally:
    if conn is not None:
        conn.close()
