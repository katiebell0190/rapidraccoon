# from ast import AugAssign


# Practice

# 1

# def employee (fullname, salary='54000'):
#     print(f'Employee full name: {fullname}. Employee Wage: {salary}')
# employee('Katie Bell', '85000')
# employee('Joe Schmow')


# 2
# def check(num1,num2):
#     sum = num1 + num2
#     if sum %2 == 0:
#         print("even")
#     else:
#         print("odd")
# check(1,2)


# #3
# def add():
#     sum = 0
#     for i in range(1,11):
#         sum = sum + i
#     return sum
# x = add()

# #4
# def calc():
#     if x %2 == 0:
#         print("even")
#     else:
#         print("odd")
# calc()

# 5
# def puppies(*breed):
#     print(breed[1])
# puppies('yorkie', 'maltese', 'silky', 'aussie', 'maltipoo')

# 6
# def add_num(*args):
#     sum = 0
#     for a in args:
#         sum = sum + a
#         print(sum)
# add_num(1,5,7,8,9)

# 7
# nums = [14,26,8,24,112,2]
# max_number = max(nums)
# min_number = min(nums)
# print(max_number)
# print(min_number)


# 8
# message = input("Type word: ")
# print("Capital Letters: ", sum(1 for c in message if c.isupper()))
# print("Lower Letter: ",sum(1 for c in message if c.islower()))

#Try Aagain. append to a list and count*

#Project
los_angeles_precipitation = {
    'January': 3.1,
    'February': 3.8,
    'March': 2.4,
    'April': 0.9,
    'May': 0.2,
    'June': 0.1,
    'July': 0,
    'August': 0,
    'September': 0.2,
    'October': .06,
    'November': 1,
    'December': 2.3
}

omaha_precipitation = {
    'January': 0.8,
    'February': 0.9,
    'March': 2.0,
    'April': 2.9,
    'May': 4.8,
    'June': 4.2,
    'July': 3.8,
    'August': 4.6,
    'September': 2.6,
    'October': 2,
    'November': 1.5,
    'December': 1.0
}


#def precipitation():
active = True
while active:
    try:
        menu = input("What would you like to do?\n[1] Check Precipitation in LA\n[2] Check Preciptiation in Omaha \n[3] Exit\n").strip()
    except ValueError:
        print("Invalid Entry. Try Again")
        active = False
    if menu == '1':
        LA = input("What month would you like to check the precipitation in LA?: ").title().strip()
        if LA == 'January':
            print(los_angeles_precipitation.get('January'))
        elif LA == 'February':
            print(los_angeles_precipitation.get('February'))
        elif LA == 'March':
            print(los_angeles_precipitation.get('March'))
        elif LA == 'April':
            print(los_angeles_precipitation.get('April'))
        elif LA == 'May':
            print(los_angeles_precipitation.get('May'))
        elif LA == 'June':
            print(los_angeles_precipitation.get('June'))
        elif LA == 'July':
            print(los_angeles_precipitation.get('July'))
        elif LA == 'August':
            print(los_angeles_precipitation.get('August'))
        elif LA == 'September':
            print(los_angeles_precipitation.get('September'))
        elif LA == 'October':
            print(los_angeles_precipitation.get('October'))
        elif LA == 'November':
            print(los_angeles_precipitation.get('November'))
        elif LA == 'December':
            print(los_angeles_precipitation.get('December'))
            active = False
    elif menu == '2':
        omaha = input("What month would you like to check in Omaha?: ")
        if omaha == 'January':
            print(omaha_precipitation.get('January'))
        elif omaha == 'February':
            print(omaha_precipitation.get('February'))
        elif omaha == 'March':
            print(omaha_precipitation.get('March'))
        elif omaha == 'April':
            print(omaha_precipitation.get('April'))
        elif omaha == 'May':
            print(omaha_precipitation.get('May'))
        elif omaha == 'June':
            print(omaha_precipitation.get('June'))
        elif omaha == 'July':
            print(omaha_precipitation.get('July'))
        elif omaha == 'August':
            print(omaha_precipitation.get('August'))
        elif omaha == 'September':
            print(omaha_precipitation.get('September'))
        elif omaha == 'October':
            print(omaha_precipitation.get('October'))
        elif omaha == 'November':
            print(omaha_precipitation.get('November'))
        elif omaha == 'December':
            print(omaha_precipitation.get('December'))
    elif menu == '3':
        print("Good Bye!")
    else:
        print("Invalid Selection. Please choose option 1,2 or 3.")
        continue
    #Needs to figure out how to put flag here because printing all the options
