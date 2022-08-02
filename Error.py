#ERROR HAN DLING AND VALIDATIONS

num = int(input("Enter number: "))
print(num)

while True:
    try:
        #married to except
        num = int(input("Enter number: "))
    except ValueError:
        print("Invalid Input.")
    else:
        if num == 0:
            raise ValueError("Zero not allowed")
        print(num)
        break

# import time
# a = 10
# try:
#     while a > 0:
#     a-=1
#     print(a)
#     time.sleep(1)
# except KeyboardInterrupt:
#     print("[-] Cancelling...")

# while True:
#     try:
#         username = input("Enter username: ")
#     except ValueError:
#         print("Invalid entry. Try again.")
#     else:
#         if username.isdigit():
#             print("Numbers not allowed.")
#         elif username.isspace():
#             print("Space not allowed.")
#         elif username == '':
#             print("Must enter value")
#         else:
#             print(username)
#             break

# while True:
#     try:
#         num1 = int(input("Enter first num: "))
#         num2 = int(input("Enter second num: "))
#         res = num1 / num2
#     except ValueError:
#         print("Only digits allowed")
#     except ZeroDivisionError:
#         print("Cannot divide number by 0. ")
#     else: 
#         print(f"{num1} / {num2} = {res}")
#         break

#finally - executes regardless whether the try block raises an exception or not; normally used to clean up resources

# while True:
#     try:
#         num1 = int(input("Enter first num: "))
#         num2 = int(input("Enter second num: "))
#         res = num1 / num2
#     except ValueError:
#         print("Only digits allowed")
#     except ZeroDivisionError:
#         print("Cannot divide number by 0. ")
#     else: 
#         print(f"{num1} / {num2} = {res}")
#         break
#     finally:
#         print("Yabbadabbadooo")

# x - creates file and returns error if file already exists (sorry its already there)
#a = append - appends to a  file if specififed file does not exist
#w - creates file if file does not already exists (overwrites everying)


# while True:
#     try:
#         f = open("testfile.txt", 'w')
#         f.write("This is my first file create using Python!")
#         print("File created.")
#         break
#     except IOError:
#         print("Error while creating file.")
#         break
#     finally:
#         f.close()

# while True:
#     try:
#         f = open("testfile.txt", 'a')
#         f.write("I am appending")
#         print("File created.")
#         break
#     except IOError:
#         print("Error while creating file.")
#         break
#     finally:
#         f.close()
