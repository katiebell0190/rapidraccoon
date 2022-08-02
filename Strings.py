#MULTILINE STRINGS

# name = """"this
# is
# a
# multilinestring""""
# print(name)

# ACCESSING STRING ELEMENTS

x = 'Python is fun'
# print(x[2])
# print(x[4])
# print(x[7])
# print(x[11])

# #SLICING STRINGS
# print(x[7:8])
# print(x[7-9])
print(x[0:6])

#METHODS
#function and method
print()
#Methords are related to objects
#function()

# # name = 'John'
# name2 = 'JOHN'
# # upper(name) - returns a sring in upper case
# #lower() - retunrs a string in lower case

# print(name2.upper())
# #capitalize() = capitalizes the first letter
# msg = 'python is fun!'
# print(msg.capitalize())

# #title() - capitalizes all first letters
# country = 'the united states'
# print(country.title())

# #split() - splits a string at a specified separator
# fruits = 'apple,banana,kiwi,mango'

# fruits = "apple,banana,kiwi,mango"
# print(fruits.split(','))

# #format()- formats specified values and inserts them into a place holder
# #very extensive 
# #strip() - returns a trimmed down version of the string. It removes spaces and trailing characters

# xyz = '   Python is fun!   '
# print(xyz.strip())

#TAKING USER INPUT
name = input('Enter name: ')
greet = (f"Hello, {name}! Welcome to Python!")
print(greet)

#Type Casting - Specify the variable type by changing it from what its default