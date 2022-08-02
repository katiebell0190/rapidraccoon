import os
# filename = 'python.txt'
# fname = os.path.join(os.path.dirname(__file__),filename)
# f = open(filename,'r')
# print(f.read())
# f.close()

#writing to file
filename = 'python.txt'
f = open(filename,'a')
f.write('I am appending to the file.')
f.close()

file_name = input("enter file name: ")
file_data = input("enter some data")
fname = os.path.join(os.path.dirname(__file__),f"{filename}.txt") #f{will pull in user input}
f = open(file_name, 'w')
f.write(file_data)
f.close()
