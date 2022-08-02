# #Single INheritance - when a child class inherits a single parent class
# from typing_extensions import Self


# class Parent:
#     def parent_func(self):
#         print("Parent class function.")
# class Child(Parent):
#     def child_func(self):
#         print("child class function.")
# ob = Child()
# ob.parent_func()
# ob.child_func()

# #Parent class
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# #child class
#     #you can add parameters to the child class 
#     #takes parent class name as params
# class Labrador(Dog):
#     def __init__(self,name,age,playfulness):#__init__ takes soem params as parent calss and adds new params
#         super().__init__(name,age)#inherits all properties from parent class but takes NO PARAMS
#         self.playfulness = playfulness

# dogo1 = Labrador('Sammy',5,'Very playful')
# dogo2 = Labrador('Dookie',14,'Mostly playful')

# print(dogo1.name,dogo1.age,dogo1.playfulness)

# #HIERARCHIACAL INHERITANCE - When multiple class inherit the same class

# class Parent:
#     def parent_func(self):
#         print("Parent class function.")
# class Child1(Parent):
#     def child1_func(self):
#         print("child1 class function.")
# class Child2(Parent):
#     def child2_func(self):
#         print("child2 class function.")
# class Child3(Parent):
#     def child3_func(self):
#         print("child3 class function.")

# ob = Child1()
# ob.parent_func(Self)
# ob.child_func()

# ob = Child2(Self)
# ob.parent_func()
# ob.child2_func()

# ob = Child3(Self)
# ob.parent_func()
# ob.child2_func()

#  #Parent class
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# #child class
#     #you can add parameters to the child class 
#     #takes parent class name as params
# class Labrador(Dog):
#     def __init__(self,name,age,playfulness):#__init__ takes soem params as parent calss and adds new params
#         super().__init__(name,age)#inherits all properties from parent class but takes NO PARAMS
#         self.playfulness = playfulness
# #Child2 class
# class Pit(Dog):
#     def __init__(self,name,age,strength):
#         super().__init__(name,age)
#         self.strength = strength
# dogo1 = Labrador('Sammy',5,'Very playful')
# dogo3 = Pit('Apollo',8,'Beast')
# print(dogo3.name,dogo3.age,dogo3.strength)

# #MULTIPLE INHERITANCE -  when a child inherits fro more than one parent class 
# class Parent1:
#     def parent1_func(self):
#         print('Parent1 class function')
# class Parent2:
#     def parent2_func(self):
#         print('Parent2 class function')
# class Child(Parent1,Parent2):
#     def child_func(self):
#         print('Child class function')

# ob = Child()
# ob.parent1_func()
# ob.parent2_func()
# ob.child_func()

# #Parent1 class
# class Poodle:
#         def __init__(self,playfulness):
#             self.playfulness = playfulness

# #Parent2 class
# class Labrador:
#     def __init__(self,wits):
#         self.wits = wits

# #Child class
# class Labradoodle(Poodle,Labrador):
#     def __init__(self, playfulness, wits):
#         Poodle.__init__(self,playfulness)
#         Labrador.__init__(self, wits)

# dogo4 = Labradoodle('Very playful','Very Smart')
# print(dogo4.playfulness,dogo4.wits)

# #MRO = Method resolution order - the oder python calls them. 1st parent class, parent2 

# #MULTILEVVEL INHERITANCE - when a chid becomes the parent of anther class (grandchild)
# class Parent:
#     def parent_func(self):
#         print("Parent class fucntion.")

# #Child class
# class Child(Parent):
#     def child_func(self):
#         print("Child class function.")

# #Grandchild class
# class Grandchild(Child):
#     def grandchild_func(self):
#         print("Grandchild class fucntion.")

# ob = Grandchild()
# ob.parent_func()
# ob.child_func()
# ob.grandchild_func()

# # Parent class
# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# #child class
  
# class Labrador(Dog):
#     def __init__(self,name,age,playfulness):#__init__ takes soem params as parent calss and adds new params
#         super().__init__(name,age)#inherits all properties from parent class but takes NO PARAMS
#         self.playfulness = playfulness
# class Puppy(Labrador):
#     def __init__(self,name,age,playfulness,potty_trained):
#         super().__init__(name,age,playfulness) #can't add anything new with these two. have to initialize potty_trained
#         self.potty_trained = potty_trained

# dogo5 = Puppy('Dookie',2,'very playful','Yes')
# print(dogo5.name,dogo5.age,dogo5.playfulness,dogo5.potty_trained)

# #HYBRID INHERITANCE - a combo of more than one type of inheritance
# #                      STAY AWAY FROM IT. DO NOT TOUCH IT WITH A 100 FT POLE!

# class Parent:
#     def parent_func(self):print("Parent class function.")
# class Child1(Parent):
#     def child1_func(self):
#         print('Child 2 class fucntion.')
# class Child2(Parent):
#     def child2_func(self):
#         print('CHild 2 class fucntion.')
# class Grandchild(Child1,Child2):
#     def grandchild_func(self):
#         print("Grandchild class function")

# ob = Grandchild()
# ob.grandchild_func() 


# class Dog:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

# #child class
# class Labrador(Dog):
#     def __init__(self,name,age,playfulness):
#         super().__init__(name,age)
#         self.playfulness = playfulness

# #child class 2
# class Poodle(Dog):
#     def __init__(self,name,age,potty_trained):
#         super().__init__(name,age)
#         self.potty_trained = potty_trained

# #Grandchild Class
# class Labradoodle(Labrador):
#     def __init__(self,name,age,playfulness,fur):
#         super().__init__(name,age,playfulness)
#         self.fur = fur

# dogo6 = Labradoodle('Dookie',4,'Very Playful','Smooth')
# print(dogo6.playfulness,dogo6.fur) #why isnt my fur working?


# CALLING THE __INIT__ method of a parent class

