#Nested ifs - Alex 

# age = input("Are you older than 18? Y/N: ").capitalize()
# if age == 'Y':
#     #pass
#     resp = int(input("How old are you? "))
#     if resp >= 18 and resp <= 20:
#         print("Go in but must wear writeband")
#     elif resp >= 21:
#         print("Get Drunk. ")
#     else:
#         print("You lid!")
# else:
#     print("You are too young.")

    #pseudo- code
    # greet user
    #print options
        #length
            #KM to Miles
            #code
            #Miles to KM
        #Weight
            #
#Greeting - For HOMEWORK
# Input(Options("How can we help your pet?"))            
#Options:
 # 1. adopting a pet
    # choice = ['Cat', 'Dog', 'Liger']
    # if choice = 'Cat':
    # print("Enter Cat's Name here: ").capitalize().string()
    # elif choice = 1
    # print
    # else choice = 2
    # print
 # 2. finding a lost pet
        # county = [County names]
        # if county = 
    # 3. how to license your dog or horse
    # 4. animal vaccinations
    # 5.pay/nueter informaiton
    # 6. microchipping
# Import module
# import getpass

# username = input("Enter username: ")
# password = getpass.getpass("Enter password: ") 
# #getpass = module.getpass=function(promt - enter password: ",")
# print (username)
# print(password)

#help(getpass)

#What is a loop? It takes you back to a previous place in your code. Two kinds
# a while loop executes a block of statements as long as a condition is true. always needs to count

# a = 1
# while a < 10:
#     print(a)
#     a+=1

# a = 10
# while a < 101:
#     print(a)
#     a+=10
#operators
#x = 5
#x = x  +5 ==> x+=5

#print the numbers 1000 to 1 skipping every 100

# a = 1000
# while a >=0:
#     print(a)
#     a-=100

#print all multiples of 3 between 0 and 30
# a = 3
# while a <=30:
#     print(a)
#     a+=3

# a = 0
# while a <= 30:
#     if a % 3 ==):
#         print(a)
#     a+=1

#break statement - stops loop if the condition is true
# import time
# a =1
# while a < 11:
#     print(a)
#     time.sleep(1)
#     if a == 7:
#         break
#     a+=1

# #getpass and time
# import time
# a = 10
# while a > 0:
#     print(a)
#     time.sleep(1)
#     if a == 2:
#         break
#     a-=1

#escape character = \n
#from time import time
#example doesn't work

# print('jack\'s car' ')
# print('use a blackslash\\')
# print('use a blaslahs\nhere')
# print('use a blaslash\t\here')
#print('usea backslash\r') puts them all at the begining for carriage return so it will print on the same line

# import time
#example doesn't work
# a = 10
# while a > 0:
#     print('\r',a,end=' ')
#     time.sleep(1)
#     if a == 2:
#         break
#     a-=1

#PIP = package managemtn system 
#example doesn't work
# import time
# from playsound import
# a = 10
# while a > 0:
#     print('\r',a,end=' ')
#     time.sleep(1)
#     playsound(r'tick.mp3')
#     if a == 2:
#         break
#     a-=1

# a = 11
# while a >=0:
#     print(a)
#     a-=1

# a = 2
# while a <= 20:
#     print(a)
#     a+=2

#contineu statement - stops the current iteration and continues wiht the next 

# a = 0
# while a < 10:
#     a+=1
#     if a == 5:
#         continue
#     elif a == 8:
#         break
#     print(a)

# password = '123'
# attempts = 3

# while attempts > 0:
#     attemtps -=1
#     pwd = input("Enter password: ")
#     if pwd == password:
#         print("Welcome!")
#         break
#     elif attempts ==0:
#         print("Failed! have been loacked out")
#         break
#     else:
#         print("Incorrect password.Try again.")
#         print(f'You have {attemtps} attempts left.')

while True:
    print("[1] Check number\n[2] Exit")
    choice = input("what would you like to do?")
    if choice == '1':
        while True:
            num = int(input("Enter num:"))
            if num %2 == 0:
                print(f'{num} is even.')
        else: print (f'{num} is odd.')

        another = input("Check another? Y/N: ").captialize().strip()
        if another =='Y':
            continue
        else:
            break
    else:
        print("Goodbye")
        break

    while True:
        print("[1} Convert\n[2] Exit")
        choice = input("What would you like to do?")
        if choice == '1':
            while True:
                kil = int(input("Enter kilomters: "))
                res = kil * 1000
                print(f"{kil} = {res} meteres")

                again = input("Convert antoehr? Y/N").capitalize().strip()
                if again == 'Y':
                    continue
                else:
                    break
        else:
            print("Good bye")
            break