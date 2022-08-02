#FUNCTION - A BLOCK of code that does something
#Creating a function

# def my_func(): #definition
#     print('This is my first function!')

# my_func() # tells the definition to print

#Parameters and Arguments

# def info(fname):#<-- parameter is the variable listed inside the parenthesis in the func definition 
#     print(fname)

#info() #parameter must include and argurment

#info('John')#<-- argument is the value sent to the fucntion when it is called


#Number of arguments
#A function can take any number of parameters, but when it is called, it must contain the same number of args

# def info(fname,lname):
#     print(fname,lname)

# info('John','Smith')

# 1. create a function that adds two numbers

# def info(num1,num2):
#     res = num1 + num2
#     print (res)
# info(1,2)

# 2. create a fucntion that creats a persons full name

# def info (fname,lname):
#     info('John','smith')
# 3. Create a function that cretaes employees' email address

# def email(fname,lname):
#     create = f'{fname}.{lname}@email.com'
#     print(create)

# email('katie','bell')


# # 4. Create a function that calculates sales tax

# def sales(sub_total, state_tax):
#     total = sub_total * state_tax + sub_total
#     print('Total: ${:,.2f}'.format(total))

# sales(7,0.05)

#Default Parameter Value
#You can call a function without an argument if the parameter is set to a default value

# def countries(country='N/A'):
#     print(f"I'm from {country}.")

# countries('The United Stsates')
# countries('Italy')
# countries()
    
#1. Create a function that accepts 3 params: username, password, pin. Set the default value for the pin to 0000.
# Call the function 3 times, one of which should have the default value.

# def login (username, password, pin='0000'):
#     print(f'My username is {username}. My password is {password}. My pin is {pin}.')

# login('PM01',1234,'0000')
# login('PM02',3456,' ')
# login('PM03', 789, )
# login('PM04', 4444, 5656)

# def print_func():
#     print("I am a printing function.")
# print_func()

# def returning_func():
#     return "I am a returning function"
# returning_func()

#print() - used only for human benefit: does not affect function itself, useful for understanding how program works
            #useful for debugging
#return = funtion returns value into itself, unseen by human, can be used as argument passed to another function

# def print_and_return():
#     print("I'm printing")
#     return "I'm returning."

# print_and_return()

# par = print_and_return()
# print(par)

# def adder():
#     return 2+2
# add = adder()
# print(add)
# print(add +5)

#Create a function that caluclates tax in NE. ONce you are done take this value(amount) and add 100

# tax  = 0.05
# def ne_tax(amount):
#     total = amount*tax+amount
#     return total
# res = ne_tax(15)

# print(res+100)


# tax = 0.08
# def ca_tax(amount):
#     return amount*tax+amount
# res2 = ca_tax(15)

# print(res2 +100)

from re import X


nyt = 0.09
cat = 0.08
net = 0.05

#functions to calculate tax
# def ny_tax(amount):
#     return amount*nyt+amount
# def ca_tax(amount):
#     return amount*cat+amount
# def ne_tax(amount):
#     return amount*net+amount

# def sales_tax_calc():
#     amount = int(input("Enter amount: "))
#     state = input("Enter state: ")

#     if state == 'ny':
#         ny = ny_tax(amount)
#         print(f"Total: {ny}")
#     elif state == 'ca':
#         ca = ca_tax(amount)
#         print(f"Total: {ca}")
#     elif state == 'ne':
#         ne = ne_tax(amount)
#         print*f"Total: {ne}"
#     else:
#         print("NOt found")
#sales_tax_calc()

# def msg():
#     print("Invalid entry. Try again.")

# msg()

#ARBITRARY ARGUMENTS (*args) if you have varied length arguments

# def message(*args):
#     #function is ready to receive any number of arguments; looks as an array
#     for a in args:
#         print(a)
# message('Python', 'is', 'fun')

# def message2(arg,*args):
#     print("First argu:",arg)
#     for a in args:
#         print('Arguemtns: ',a)
# message2('1','2','3','4')


# def add(num1,num2):
#     print(num1+num2)
# add(2,3)

# Function returns values into itself. These values can be further manipulated at will.
# You puny human cannot see anything that happens inside of it
# If you want to see it, then encapsulate the function call in a print statement
# If the intention is to manipulate the values, then assign it to a variable

#1
def add(num1,num2):
    return num1+num2

num1 = int(input("First: "))
num2 = int(input("Second: "))

add(num1,num2)


#2
def add(num1,num2):
    return num1+num2
add(int(input("First: ")),int(input("Second: ")))

#3
def add(num1,num2):
    num1 = int(input("First: "))
    num2 = int(input("Second: "))
    return num1+num2
add(num1,num2)


#4
def add():
    num1 = int(input("First: "))
    num2 = int(input("Second: "))
    return num1+num2
print(add())
 

def add(num1,num2):
    return num1+num2
x = add(2,3)
print(add(2,3))



def add2(num1,num2):
    print(num1+num2)
add(2,3)

def adder(*nums):
    sum = 0
    for n in nums:
      sum = sum + n
    print(sum)
adder(2,3)
adder(2,3,5)
adder(2,3,5,7)

def employee_OTM(*employees):
    print(employees[0])

employee_OTM("Larry","Curly","Moe")

#Keyword Arguments
def employee_OTM(emp1,emp2,emp3):
    print(emp2)
employee_OTM(emp1 = 'Larry', emp2 = 'Curly', emp3 = 'Moe')

def my_func():
    x = 5
    return x
res = my_func()
print(res)

#Arbitrary keyword arguments(**kwargs)
def employee_OTM(**kwargs):
   for k,v in kwargs.items():
       print(k,v)
employee_OTM(emp1 = 'Larry', emp2 = 'Curly', emp3 = 'Moe', emp4 = 'Laurel', emp5= 'Hardy')