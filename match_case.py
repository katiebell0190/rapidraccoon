# subject = ''

# #match - evaluates the subject data or object
# match subject:#can be anything (literal, data, object)
#     case '<pattern 1>': #subject is compared with pattern
#         '<action 1>' #action is called based on case statement pattern
#     case '<pattern 2>':
#         '<action 2>'
#     case '<pattern 3>':
#         '<action 3>'    
#     case _:             #wildcard or equievelent to the else
#         '<wildcard>'

# #BASIC EXAMPLE 

# car = int(input( "Enter option: "))
# if car == 1:
#     print('Ford')
# elif car == 2:
#     print('Nissan')
# elif car == 3:
#     print('Honda')
# elif car ==4:
#     print('Buick')
# elif car == 5:
#     print('Chrystler')
# else:
#     print('Not valid.')

#case verion
    
# car = int(input( "Enter option: "))
# match car:
#     case 1:
#         print('Ford')
#     case 2:
#         print('Nissan')
#     case 3:
#         print('Honda')
#     case 4:
#         print('Buick')
#     case 5:
#         print('Chrystler')
#     case _:
#         print('Not valid')

# #MULTIPLE CASES
# car = input( "Enter option: ")
# if car == 'Ford' or car == 'Buick' or car == 'Chrystler':
#     print('American')
# if car == 'Honda' or car == 'Nissan':
#     print('Japanese')
# else:
#     print('Not Valid')

# car = input( "Enter option: ")
# match car:
#     case 'Ford'| 'Buick' | 'Chrystler': # | (hype) works as or above the \ #& = and
#         print('American')
#     case 'Honda' | 'Nissan':
#         print('Japanese')
#     case _:
#         print('Not valid')

#MATCH CASE WITH COLLECTIONS
# car_brands = ['Ford','Ferrari','Chevrolet','Lamborghini']
# match car_brands:
#     case['Ford','Chevrolet']:
#         print('American cars')
#     case ['Ferrari','Lamborghini']:
#         print('Italian')
#     case ['Ford','Ferrari','Chevrolet','Lamborghini']:
#         print('Both American and Italian Cars')
#     case _:
#         print('not found')

# usr = input('Select all even nums from 1 to 5: ').split()
# match usr:
#     case['2','4'] : print('Correct!')
#     case _: print('Incorrect!')
    
# #USING CONSTANTS AS PATTERNS
# class Switch:
#     on = 1
#     off = 0

# status = 1

# match status:
#     case Switch.on:
#         print('Switch is on.')
#     case Switch.off:
#         print('Switch is off.')

# #GUARD - INLINE IF STATMENTS
# num = 0
# match num:
#     case num if num == 0:
#         print('ZeroDivisionError')
#     case num if num %2 == 0:
#         print('Even')
#     case num if num %2 != 0:
#         print('Odd')