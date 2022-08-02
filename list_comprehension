# expression = ' ' #output
# iterable = ' '
# condition = ' '



# obj = [expression for item in iterable if condition == True ]

# my_list = [1,2,3,4]
# for item in my_list:
#     print(item)

#1 take items from alist and append to another list
# fruit_list = ['apple', ' banana', 'cherry','kiwi','mango']
# new_fruit_list = []

# for f in fruit_list:
# #     new_fruit_list.apped(f)
# # print(new_fruit_list)

# new_fruit_list = [f for f in fruit_list]
# print(new_fruit_list)

# do something for every item in this list

#2. add only 'kiwi to the new list

# for f in fruit_list:
#     if f == 'kiwi':
#         print(f)

#

#3 Add all item to new list as los as item is not kiwi
# new_fruit_list = [f for f in fruit_list if f != 'kiwi']
# print(new_fruit_list)

#THE EXPRESSION = it is both the cfurrent item in the iterationad the output
#                  it can also be manipulated before it joins the new list
# CONDITION IN TH EXPRESSION - expressions may also contain conditions                 
#IN list comprehension, conditions DO NOT act as a filter
# instead they are used to maniupate the output

#4 If the item is kiwi, then it should be repalced by raspberry. Otherwise,
#item remains the same

# fruit_list = ['apple', ' banana', 'cherry','kiwi','mango']
# new_fruit_list = []


# new_fruit_list = [f if f != 'kiwi' else 'raspberry' for f in new_fruit_list]
# print(new_fruit_list)

#give me all of these unless its kiwiw then put raspberry if it is kiwi


#OLD WAY
# for f in fruit_list:
#     if f == 'kiwi':
#          new_fruit_list.append('raspberry')
#     else:
#         new_fruit_list.append(f)
# print(new_fruit_list)

#THE ITERABLE - iterables can be any object (list, tuples, strings, sets...)

# a = [n for n in range(10)]
# print(a)

#for every item in the range then print every item

#add conditional (produce only even)

# a  = [n for n in range(10) if n%2==0]
# print(a)

#LIST COMPREHENSION WITH NESTED CONDITIONALS
#6 print nums 0 to 50 
# the first conditional requires only numbers 25 and up
# the second conditional requires only those divible by 3

# for n in range(50):
#     if n >= 25:
#         if n%3 == 0:
#             print(n)

# a = [n for n in range(50) if n >= 25 and n%3 == 0]
# print(a)

#LIST COMPREHENSION WITH SINGLE NESTED IF/ELSE

#replace numers less than 5 iwth the word 'kerfuffle

from re import S, X


num_list = [1,2,3,4,5,6,7,8,9,10]

# for n in num_list:
#     if n < 5:
#         print('kerfuffle')
#     else:
#         print(n)


# new_fruit_list = [f if f != 'kiwi' else 'raspberry' for f in new_fruit_list]
# print(new_fruit_list)


# new_num = [n if n > 5 else 'kerfuffle' for n in num_list]
# print(new_num)

#LC WITH MULTIPLE NESTED IF/ELSE
#7. replae all nubmers divislbe by 3 with 'skidaddle'
#replace all numbers divisble by 5 with ' nimcompoop'
# replace every thing else with 'fuddy duddy'



# new_num = [n if n > 5 else 'kerfuffle' for n in num_list]
# print(new_num)

# new_num_list = []
# for n in num_list:
#     if n%3 == 0:
#         new_num_list.append('skiddadle')
#     elif n%5 == 0:
#         new_num_list.append('nimcompoop')
#     else:
#         new_num_list.append('funddy-duddy')
# print(new_num_list)

#myfirst try - incorrect
# new_num_list = [n if n%3 == 0 'skidaddle' elif n%5 == 0 'nimcompoop' else 'fuddy-duddy' for n in new_num_list]
# print(new_num_list)


#start with the output = do thise 2nd part is the iterate and 3rd part is filter (not in this example )
# new_num_list = [ 'skidaddle' if n%3==0 else 'nincompoop' if n%5 == 0 else 'fuddy-duddy' for n in num_list]
# print(new_num_list)

#LC WITH NESTED FOR LOOP
nums = [1,2,3]
letters = ['a','b','c']
combo = []

#tuple
# for n in nums:
#     for l in letters:
#         #print(n,l)
#         combo.append((n,l))
# print(combo)

#lists
# for n in nums:
#     for l in letters:
#         #print(n,l)
#         combo.append([n,l])
# print(combo)

#sets
# for n in nums:
#     for l in letters:
#         #print(n,l)
#         combo.append({n,l})
# print(combo)

#start with the output = do thise 2nd part is the iterate and 3rd part is filter (not in this example )

#LC WITH NESTED FOR LOOP
nums = [1,2,3]
letters = ['a','b','c']
combo = []

#tuple
# for n in nums:
#     for l in letters:
#         #print(n,l)
#         combo.append((n,l))
# print(combo)

# combo = [[n,l] for n in nums for l in letters]
# print(combo)

# combo1 = [{n,l} for n in nums for l in letters]
# print(combo)

#1 Find all nums from 1 to 100 that are divisible by 7

# n =  [n for n in range(100) if n%7==0]
# print(n)

#2. FInd all nums from 1 to 1000 that have a 3 in them 

# n = [n for n in range(1000) if n %10 == 3]
# print(n)

#sam

#[j for j in range(1,1001) for i in str(j) if int(i) == 3]


# nums = [i for i in range(1000)]
# div3 = [x for x in nums if '3' in str(x)]
# print(div3)

#4 count the number of spaces in a string
string = "The quick brown fox jumped over the lazy dog"
#print(string.count(' '))

# for s in string:
#     if s == ' ':
#         print(s)

spaces = [s for s in string if s == ' ']
print(spaces.count(' '))