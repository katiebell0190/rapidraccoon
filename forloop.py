#for loop is used to iterate over a sequence (could be a string, list, touple, dictionary)


#for every item in this list then do something
# 
# for f in fruit_list:
#     do something

# fruits = ['apple', 'banana', 'orange', 'mango']
# for f in fruits: "#for every item in this sequence"
#     print(f)

#     my_string = 'I love Python'
#     for s in my_string:
#         print(s)

# fruits = ['apple', 'banana', 'orange', 'mango']
# for f in fruits:
#     print(f, end=',')

#break statement - discards mango
# fruits = ['apple', 'banana', 'orange', 'mango']
# for f in fruits:
#     print(f)
#     if f == 'orange':
#         break

#the print can be before or after but the result will be vastly different
#fruits = ['apple', 'banana', 'orange', 'mango']
# for f in fruits:
#     if f == 'orange':
#         print(f)
#         break - stops iteration even if it is true

#continue - it allows it to keep going but will skip an iteration
# fruits = ['apple', 'banana', 'orange', 'mango']

# for f in fruits:
#     if f == 'orange':
#         continue
#     print(f)

    #create a list from 1-10. Iterate over each number. Skip number 5 and stop at 9. Instead of simply printing 5, print "skipped"

# numbers = ['1','2','3','4','5','6','7','8','9','10']
# for n in numbers:
#     if n == '5':
#         print("skip")
#         continue
#     elif n == '10':
#         break
#     print(n)

#range() - returns a sequence of predefined numbers
#  default start is 0
# 10 doesnt mean 0 to 10 it means 10 numbers starting with 0

# for i in range(1,10):
#     print(i)

#up to 50
# for i in range(10,50,5):
#     print(i)

#to include 50 
# for i in range(10,51,5):
#     print(i)

#next for loop

from multiprocessing.sharedctypes import Value


fruits = ['apple', 'banana', 'orange', 'mango']
adjectives = ['delicious', 'healthy', 'nutritious', 'juicy']

# for f in fruits:
#     for a in adjectives:
#         print(f,a)


# for i in range(5):
#     for j in range(i+1):
#         print('*', end='')
#     print('')

# my_string = 'Hello'
# for i in my_string:
#     print(i.capitalize())

#Create a times table

print("Welcome to Python times table!")
incorrect = []
while True:
    try: 
        times_table = int(input("Which table would you like to learn?\n"))
    except ValueError:
        print("Invalid Entry. Enter a number you would like to see multiplied.")
    else:
        for i in range(1,11):
            while True:
                print(f"{times_table} x {i} = ? ")
                ask = int(input("answer: "))
                answer = (times_table*i)
                
                if ask == answer:
                    print("Correct!")
                    break
                elif ask != answer:
                    print("Incorrect answer. Try again!")
                    incorrect.append(f"{times_table} x {i} = {times_table*i} -> Your answer: {ask}")
                    continue
                    #needs to repeat question before allowing to go to next interation
            
        print("These are the answers you missed: ")
        if incorrect:
            for i in incorrect:
                print(i)
        else:
            print("Congratulations! You got all the answers correct!")
            break
    
        user = int(input("Learn another table? 1 for YES, 2 for NO :\n"))
        if user == 1:
            continue

        else:
            print("Goodbye")
            break
    break
    
