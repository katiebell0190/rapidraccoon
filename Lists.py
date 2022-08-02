#Python Collections

#List - are ordered; the order never changes, you can add or remove items (changeable), allows duplicates
#Dictionaries - ordered , changeable, do not allow duplicates 
#Tuples - ordered, unchangeable, allow duplicates
#Sets - unordered, unchangeable, do not allow duplicates
#choosing the right data type will make it faster or slower or more/less secure

#Creating a list
#fruits = ['apple','banana', 'orange','kiwi', 'mango']
# print(fruits)

# #Accessing List Items
# print(fruits[2])

# #Negative Indices
# print(fruits[-1])

# #Accessing a Range of Indices
# print(fruits[1:3])

# print(fruits[2:4])

# print(fruits[2:])
# print(fruits[:3])

# fruits = ['apple','banana', 'orange','kiwi', 'mango']

# #Changing Item Values
# fruits[1] = 'blueberry'
# print(fruits)

# #Changing a range of values
# fruits[2:4] = ['lemon','strawberry']
# print(fruits)
# #fruits.replace('lime') replace doesn't work for lists only for strings
# print(fruits)

#Adding Items to List
#fruits = ['apple','banana', 'orange','kiwi', 'mango']
#append() - adds item to the end of list
# fruits.append('melon')
# print(fruits)

# new_list = fruits
# new_list.apend('melon')
# print(new_list)

#fruits = ['apple','banana', 'orange','kiwi', 'mango']
#insert() - adds item to specificed position
#fruits.insert(position, the item you want to add)
# fruits.insert(2,'pineapple')
# print(fruits)

#extend( - adds elements from another list to current list)
# fruits = ['apple','banana', 'orange','kiwi', 'mango']
# fruits2 = ['lemon', 'grapes']
# fruits.extend(fruits2)
# print(fruits)

#fruits = ['apple','banana', 'orange','kiwi', 'mango']
#Removing Items
#remove() - removes specified item - uses name not index 
#fruits.remove('kiwi')
#print(fruits)

#pop() - removes specified index - requires only 1 parameter not mulitple
# fruits.pop(2)
# print(fruits)

#fruits = ['apple','banana', 'orange','kiwi', 'mango']
#clear() - empties list
# fruits.clear()
# print(fruits)

#Statement = del
#del - removes specified index - similar to pop but used different
#   also deletes list completely

# del fruits[0]
# print(fruits)

# del fruits
# print(fruits)

# student_list = ['John', 'Mike','Ashley', 'Vanessa']
# python_class_roster = []
# java_class_roster = []

# python_class_roster.append('John')
# python_class_roster.append('Ashley')
# print("Student Lists: ",python_class_roster)

# java_class_roster.append('Mike')
# java_class_roster.append('Vanessa')
# print("Java Lists: ",java_class_roster)

# student_list.clear()
# print("Student List: ",student_list)

# produce = ['lettuce', 'tomatoes', 'celery', 'onions', 'spinach', 'broccoli']
# print("Produce:",produce)

# unavailable_produce = ['carrots', 'zucchini']
# print("Unavailable:",unavailable_produce)

# usr = input("Select produce: ").lower().strip()
# produce.remove(usr)
# unavailable_produce.append(usr)

# print("Produce:",produce)
# print("Unavailable:",unavailable_produce)

# usr2 = input("Select unavailable:" ).lower().strip()
# produce.append(usr2)
# unavailable_produce.remove(usr2)

# print("Produce:",produce)
# print("Unavailable:",unavailable_produce)

produce = ['lettuce', 'tomatoes', 'celery', 'onions', 'spinach', 'broccoli']
print("Produce:",produce)

unavailable_produce = ['carrots', 'zucchini']
print("Unavailable:",unavailable_produce)

new_produce = "artichoke,squash,potatoes,cabbage"

produce.extend(new_produce.split(','))
print(produce)
#new_produce - ['artichoke', 'squash', 'potatoes', 'cabbabe']
