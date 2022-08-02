import numpy as np

# #What is an array? = a series of values examples of kinds are lists, dictionaries, tuples, sets

# #Creating an array
# #As List
# a = np.array([1,2,3,4,5])
# print(type(a))

# b = [1,2,3,4,5]
# print(type,(b))

# #Numpy accepts any array like object as data

# #array as tuple
# a=np.array((1,2,3,4,5))
# print(a)

# #Array as sets
# a = np.array({1,2,3,4,5})
# print(a)

# #dictionary
# a = np.array({'a':1, 'b':2,'c':3})
# print(a)

# #Creating an array filled wiht 0's
# a = np.zeros(5)
# print(a)

# #Creating an array filled with 1's
# a = np.ones(5)
# print(a)

# #create an empty array
# a= np.empty(2)
# print(a)

#Array Dimensions
a= np.array([1,2,3,4,5])
print(type(a))

#nd arrays = numpy arrays n-dimension
#1-D,2-D,3-D
#0-d - scalar
#1-d - vector
#2-d = matrix
#3-d = tensor

# #0-D Arrays - each value itself is a 0-D array
# a = np.array(11)
# print(a)
# #1-D array
# a=np.array([1,2,3,4,5])
# print(a)
# #2-D
# a=np.array([[1,2,3],[4,5,6]])

# #3-D
# a=np.array([[[1,2,3,],[4,5,6]],[[7,8,9],[10,11,12]]])
# print(a)
# print(a.ndim)
# print(a.shape)
# print(a.size)

# a=np.array([[[1,2,3,],[4,5,6]],[[7,8,9],[10,11,12]]])
# #a=np.array([[[1,2,3,],[4,5,6]],[[7,8,9],[10,11,12]],[[13,14,15],[16,17,18]]])

# print(a.ndim)
# print(a.shape)
# print(a.size)

#Array indexing
#Accessing 1-D arrays
# a = np.array([1,2,3,4,5])
# print(a[2])
# print(a[2:4])
# print(a[::2])

#Accessing 2-d Arrays
# a= np.array([[1,2,3],[4,5,6]])
# print(a[1,2])
# print(a[0,2])

#Accessing 3-D Arrays
# a=np.array([[[1,2,3,],[4,5,6]],[[7,8,9],[10,11,12]]])
# #print(a[1,1,0])
# print(a[0,1,1])
# print(a[1,0,0])
# print(a[1,1,1])

# #NEgative Indexing
# a= np.array([[1,2,3],[4,5,6]])
# print(a[0,-2])
# print(a[-2,-2])
# print(a[1,-1])

# #Array slicing
# #1-D Arrays
# a= np.array([1,2,3,4,5])
# print(a[0:3])

# #negative slicing
# print(a[:-2])
# print(a[-4:-2])
# #Using STEP

# a = np.array([0,1,2,3,4,5,6,7,8,9,10])
# print(a[1:10:2])

# #w-D arrays
# a = np.array([[0,1,2,3,4],[5,6,7,8,9]])
# print(a[1,1:])
# print(a[:,1:4])
# print(a[0,:3])
# print(a[1,2:5])

# a=np.array([[[1,2,3,],[4,5,6],[7,8,9]],[[10,11,12],[13,14,15],[16,17,18]],[[19,20,21],[22,23,24],[25,26,27]]])

a = np.array([[[1,2,3],[4,5,6],[7,8,9]],
            [[10,11,12],[13,14,15],[16,17,18]],
            [[19,20,21],[22,23,24],[25,26,27]]])
# print(a[2,0,1])
# print(a[2,1,2])
# print(a[2,2,:3])
# #select a particular column

# print(a[1,:,2])
# print(a[:,0,0])
# print(a[1])
# print(a[:,0])
# print(a[:,:,0])

# Elements 16
#print(a[1,2,0])
# Row 22,23,24
#print(a[2,1])
# elements 3,6,9
#print(a[0,:,2])
# elements 3,12,21
#print(a[:,0,2])
# rows [7,8,9],[16,17,18],[25,26,27]
#print(a[:,2,:])
# columns [2,5,8],[11,14,17],[20,23,26]
# print(a[:,:,1])
