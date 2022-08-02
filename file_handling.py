#open() close()

# filename = r 'C:\Users\Desktop' 'python.txt'
# #to use the open function you have to create a variable
# # first parameter is the variable, second parameter is the mode
# f = open(filename,'r')
# print(f.read())
# f.close

#ARelative Path
import os
filename = 'python.txt'
fname = os.path.join(os.path.dirname(__file__,filename))
f = open(filename, 'r')
f.close()