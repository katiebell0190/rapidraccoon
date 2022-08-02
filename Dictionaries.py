# #Dict - ordered, changeable, do not allow duplicates

# fav_truck = {
#     'brand': 'Ford',
#     'model': 'Raptor',
#     'year': 2022,
# }
# print(fav_truck)
# print(len(fav_truck))

# # #Accessing Items
# # #individual values
# # #if i want to access brand. Create a variable
# # b = fav_truck['brand']
# # print(b)
# # b = fav_truck.get('model')
# # print(b)

# # #Checking if an item exists
# # if 'brand' in fav_truck:
# #     print("Found")
# # else:
# #     print("Not Found")

# # #Getting a list of all keys in dict
# # k = fav_truck.keys()
# # print(k)

# # #getting a list of all values in dict
# # v = fav_truck.values()
# # print(v)

# # #Returing key/value partes
# # kv = fav_truck.items()
# # print(kv)

# # #adding items to dict
# # fav_truck['color'] = 'Murdered-Out Black'
# # print(fav_truck)

# # fav_truck.update({'engine': 'V8'})
# # print(fav_truck)

# # #Deleting items
# # fav_truck.pop('engine')
# # print(fav_truck)

# #del fav_truck['color']
# #print(fav_truck)

# #del fav_truck - will delete the entire dictionary

# fav_truck.popitem()
# print(fav_truck)

# fav_truck.clear()
# print(fav_truck)

# #defcon.org
# #Looping through a dict

# for i in fav_truck:
#     print(i)

#     #return all values
# for i in fav_truck:
#     print(fav_truck[i])

#     for i in fav_truck.values():
#         print(i)

#     for i,j in fav_truck.items()
#         print(i,j)

#Nested DIctionaries
#1st TYPE
# python_class = {
#     'st1':{
#         'fname': 'Patrick',
#         'lname': 'Ennen',
#         'id': 'PM001',
#         'gender':'M',
#     },
#     'st2':{
#         'fname': 'Sean',
#         'lname': 'Mitchell',
#         'id': 'PM002',
#         'gender': 'M',
    
#     },
#     'st3':{
#         'fname':'Caitlin',
#         'lname': 'Waszsgis',
#         'id': 'PM004',
#         'gender': 'F',
#     },
#     'st5':{
#         'fname': 'Samuel',
#         'lastname': 'Sidzyik',
#         'id': 'PM0005',
#         'gender':'M',
#     },
#     'st6':{
#         'fname': 'Andrew',
#         'lname': 'Teeter',
#         'id': ' PM006',
#         'gender': 'M',
#     },
# } 

# print(python_class)

# #2nd TYPE
# st1 ={'fname': 'Patrick',
#         'lname': 'Ennen',
#         'id': 'PM001',
#         'gender':'M',
# }

# st2 ={'fname': 'Sean',
#         'lname': 'Mitchell',
#         'id': 'PM002',
#         'gender':'M',
# }

# st3 ={'fname': 'Mathew',
#         'lname': 'Williams',
#         'id': 'PM003',
#         'gender':'M',
# }

# st4 ={'fname': 'Caitlin',
#         'lname': 'Waszgis',
#         'id': 'PM004',
#         'gender':'F',
# }
# st5 ={'fname': 'Samuel',
#         'lname': 'Sidzyik',
#         'id': 'PM005',
#         'gender':'M',
# }
# st6 ={'fname': 'Andrew',
#         'lname': 'Teeter',
#         'id': 'PM006',
#         'gender':'M',
# }

# #the value is...
# python_class2 = {
#     'st1' : st1,
#     'st2' : st2,
#     'st3': st3,
#     'st4': st4,
#     'st5': st5,
#     'st6': st6
# }

from turtle import Turtle


python_class = {
    'st1':{
        'fname': 'Patrick',
        'lname': 'Ennen',
        'id': 'PM001',
        'gender':'M',
    },
    'st2':{
        'fname': 'Sean',
        'lname': 'Mitchell',
        'id': 'PM002',
        'gender': 'M',
    
    },
    'st3':{
        'fname':'Caitlin',
        'lname': 'Waszsgis',
        'id': 'PM004',
        'gender': 'F',
    },
    'st5':{
        'fname': 'Samuel',
        'lastname': 'Sidzyik',
        'id': 'PM0005',
        'gender':'M',
    },
    'st6':{
        'fname': 'Andrew',
        'lname': 'Teeter',
        'id': ' PM006',
        'gender': 'M',
    },
} 

    #Adding a new nested diction
# python_class ['st7'] = {
#     'fname': 'Joan',
#     'lname': 'Smith',
#     'id': 'PM007',
#     'gender': 'F'
#     },
# print(python_class)



#Accessing items in a  nested looptwo [dictionary name][keyname]
# print(python_class['st1']['fname'])
# a = print(python_class['st1']['fname'])
# print(a)

# b = python_class['st2'].get('fname')
# print(b)

# id = input("Enter student ID: ")
# for student in python_class:
#     st_id = python_class[student].get('id')
#     if id != st_id:
#         print("Not found")
#     else:
#         print("Found")

#USING FLAGS - to signal the program to decide if the program should continue or only a specific section

# while True:
#     pwd1 = input("Enter password: ")
#     pwd2 = input("Re-Enter password: ")
#     if pwd1 == pwd2:
#         print("Welcome")
#         break
#     else:
#         print("Not a match.")
#"while this is false, something is not going to happen, but i'm going to set the flag to go off at a certain piont"
# active = True:
# while active:
#     pwd1 = input("Enter password: ")
#     pwd2 = input("Re-Enter password: ")
#     if pwd1 == pwd2:
#         print("Welcome")
#         active = False
#     else:
#         print("Not a match.")

# while True:
#     id = input("Enter student ID: ")
#     active = False #initialize flag variable to false(run or not run)
#     for student in python_class:
#         st_id = python_class[student].get('id')
#         if id != st_id:
#             continue
#         else:
#             active = True #flag is assigned to Ture before breaking out of loop
    
#     if active == True: #shifting conditions to a second block outside the for loop for it to work- always do if there are flags involved 
#         print("Found!")
#         break
#     else:
#         print("Not found.")

    #Adding a new nested diction
# python_class ['st7'] = {
#         'fname': 'Joan',
#         'lname': 'Smith',
#         'id': 'PM007',
#         'gender': 'F'
#     }
# print(python_class)


# st_counter = 6
# while True:
    
#     new_fname = input("Please enter new student first name: ").capitalize().strip()
#     new_lname = input("Please enter new student last name:  ").capitalize().strip()
#     new_id = input("Please enter student ID: ").upper().strip()
#     new_gender = input("Please enter new student gender: ").upper().strip()
   
#     st_counter +=1
#     st_next = (f'St{st_counter}')
#     python_class [st_next] = {'fname': new_fname, 'lname': new_lname, 'id': new_id, 'gender': new_gender}
#     print(python_class)

#     again = input("Do you want to add another student? Y/N :").capitalize()
#     if again != 'Y':
#         break
#Deleting a value     
python_class['st1'].pop('gender')
print(python_class)

#Deleting a student
del python_class['st1']
print(python_class)


#Homework - 
# 
# Assignment 1 - Create a menu
#Create dictionary with fname/lname & username/password
#Give me something to identify you are who you say you are
#1 Forgot username - return username
#2 Reset password
#3 Exit

#Assignment 2 - 
#Create a dictionary with 5 items for sale. Each item must contain the following key/value pairs: 
#brand, price, availablitiy (Y/N or T/F)
#user can: search, edit, add, delete items
#with validations and everything you love

#Assignment 3-





