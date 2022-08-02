import hashlib
import getpass
import os

# password = 'Abc123'
# hashpass = hashlib.sha512(password.encode('utf-8')).hexdigest()
# print(hashpass)

# class Hash:
#     def __init__(self,password,pwd):
#         self.password = password
#         self.pwd = pwd

#     def hash_password(self):
#         self.password = hash_pwd
#         hashpass = hashlib.sha256(self.password.encode('utf-8')).hexdigest()
#         with open('password_file.txt','w') as wf:
#             wf.write(hashpass)
#         print('Password hashed successfully!')

#     def verify_pass(self):
#         self.pwd = verify_pwd
#         hashpwd = hashlib.sha256(self.pwd.encode('utf-8')).hexdigest()
#         with open('password_file.txt','r') as rf:
#             read_file = rf.read()
#             if read_file == hashpwd:
#                 print('Credentila authenticated!')
#             else:
#                 print('Authentication failed.')

# hash_pwd = getpass.getpass(prompt='Enter Password: ')
# verify_pwd = getpass.getpass(prompt='Verify password: ')

# hp = Hash(password=hash_pwd,pwd=verify_pwd)
# hp.hash_password()
# hp.verify_pass()

# pass1 = 'Passw0rd' + '1l0v3y0u'
# pass2 = 'SupaSecre3t' + 'M4mm4sF00d'
# pass3 = 'Myp4ass!' + 'N3wM0use'
# pass4 = 'Passw0rd' + 'H4ll4T1ght!'

# h1 = hashlib.sha256(pass1.pwd.encode('utf-8')).hexdigest()
# h2 = hashlib.sha256(pass2.pwd.encode('utf-8')).hexdigest()
# h3 = hashlib.sha256(pass3.pwd.encode('utf-8')).hexdigest()
# h4 = hashlib.sha256(pass4.pwd.encode('utf-8')).hexdigest()

# print(h1)
# print(h2)
# print(h3)
# print(h4)

# salt = os.urandom(64)
# pass1 = 'Passw0rd'

# key = hashlib.pbkdf2_hmac('sha256',pass1.encode('utf-8'),salt,100000)
# print(key)

# class SecurePass:
#     def __init__(self,password='',verify_password=''):
#         self.salt = b''
#         self.gen_key = b''
#         self.password = password
#         self.verify_password = verify_password
#         self.storage = b''

#     def generate_salt(self):
#         #this function generated a 64-bit salt
#         self.salt = os.urandom(128)
#         return self.salt

#     def hash_password(self):
#         #this function hashes user password
#         self.password = ''# this will use variable for user input
#         self.gen_key = hashlib.pbkdf2_hmac('sha256',self.password.encode('utf-8'),self.salt,100000)
#         return self.gen_key

#     def store_key_salt(self):
#         #this function stores both salt and hashed password into text file
#         self.storage = user.generate_salt() + user.hash_password()
#         with open('store_key_salt.txt','wb') as write_storage:
#             ws = write_storage.write(self.storage)

#     def retrieve_secure_pass(self):
#         #this function takes user password and hashes it
#         self.verify_password = '' #this takes user input
#         self.verify_key = hashlib.pbkdf2_hmac('sha256', self.verify_password.encode('utf-8'),self.salt,100000)
#         self.verify_storage = self.salt +self.verify_key

#         with open('vefify_storage.text','wb') as write_verify_storage:
#             wv = write_verify_storage.write(self.storage)
#         with open('store_key_salt.txt','rb') as read_storage:
#             rs = read_storage.read()

#         #verify if they match
#         if self.verify_storage == rs:
#             print('Crendial Authenticated!')
#         else:
#             print('Credential invalid')

# enter_pass = getpass.getpass(prompt=("Enter password: "))
# verify_pass = getpass.getpass(prompt=("Verify password "))

# user = SecurePass()
# user.generate_salt()
# user.hash_password()
# user.store_key_salt()
# user.retrieve_secure_pass()
