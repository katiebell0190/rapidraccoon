# import getpass
# username = input("Please create a username: ").capitalize().strip
# password = getpass.getpass(prompt = 'Please create a password: ').strip()
# attempt = 3

# print(f"Please login. You have {attempt} attempts to login.")
# while attempt > 0:
#     enter = input("Please enter your username ")
#     enter2 = getpass.getpass(prompt="Please enter your password: ")

#     if username == enter:
#         print(enter2)
#         break
#     else:
#         attempt -=1
#         if attempt >=1:
#             print(f"Invalid. You have {attempt} attempts left. ")
        
#         if attempt == 0:
#             print("You are locked out. Contact Admin.")


while True:
    print("Would you like to [1] Create an account\n [2] Login: ")
    try:
        create = int(input("Create a username: ")
    except ValueError:
        print("Invalid")
        continue
    if select == '1':
        try:
            create = input("Create a username: ")
        except ValueError:
            print("Username not valid.")
            continue
    elif
