# #Creating a Class
# class Employee:
#     pass

# #objects
# emp1 = Employee()
# emp2 = Employee()

# print(emp1)
# print(emp2)

# emp1.fname = 'Mario'
# emp1.lname = 'Rossi'
# emp1.email = 'Mario.Rossi@company.com'
# emp1.pay = 50000

# emp2.fname = 'Jane'
# emp2.lname = 'Smith'
# emp2.email = 'Jane.Smith@company.com'
# emp2.pay = 60000

# print(emp1.email)
# print(emp2.pay)

#The init function - a constructor from 

# class Employee: #object
#     def __init__(self,fname,lname,pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay

#     #Blueprint
# emp1 = Employee('Mario', 'Rossi', 50000) # object from this class with attributes
# emp2 = Employee('')
# emp3 = Employee('Hans','Mueller', 100000)

# print(emp1.pay)
# print(emp2.pay)
# print(emp3.pay)

#Creat a cat clsss and the following attributes name, age, breed. 
# Create two cat Objects and pass arguments accordingly. Then, print
#each object's info 

# #create the class
# class Cat:
#     def __init__(self,name,age,breed): #create the contstructor function
#         self.name = name                #create the attributes
#         self.age = age
#         self.breed = breed

# #create the objects and reference the class
# cat1 = Cat('Bruno','3', 'Lion')
# cat2 = Cat('Babs',5, 'Tiger')

# #pass the arguments
# print(cat1.name)
# print(cat2.name)
# print(cat1.age)

# class Truck:
#     def __init__(self, brand, model, year, color, price):
#         self.brand = brand
#         self.model = model
#         self.year = year
#         self.color = color
#         self.price = price

# truck1 = Truck('Chevy', 'Silverado', '2017', 'white', 85000)
# truck2 = Truck('Toyota', 'Tacoma', 2020, 'blue', 45000)

# print(truck1.brand)
# print(truck1.model)
# print(truck1.price)
# print(truck2.brand)
# print(truck2.model)
# print(truck2.price)

#3. Create a Trip Calculator class, and add two params: tank size and efficiency (mpg). Create
# a couple of objects and add info about your own vehicles.

# class TripCalc:
#    def __init__(self,tank_size, efficiency):
#        self.tank_size = tank_size
#        self.efficiency = efficiency
    
# car1 = TripCalc(13,35)
# car2 = TripCalc(17,20)

# print(car1.tank_size)
# print(car2.tank_size)


#4. Create a Triangle class that takes three params: side,side2, and side3. Create three objects
# and pass args. 
# Equilateral - all same
# Isosceles - two similar sides
# Scalene - all different sides

# class Triangle:
#     def __init__(self,side1,side2,side3):
#         self.side1 = side1
#         self.side2 = side2
#         self.side3 = side3

# t1 = Triangle(5,5,5)
# t2 = Triangle(6,6,10)
# t3 = Triangle(4,3,2)



# class Employee:
#     def __init__(self,fname,lname,pay):
#         self.fname = fname
#         self.lname = lname
#         self.pay = pay
#         self.email = f"{fname}.{lname}@company.com"

#     def fullname(self):
#         return f'{self.fname} {self.lname}'


# emp1 = Employee('Mario', 'Rossi', 50000)
# emp2 = Employee('Jane','Smith', 60000)
# emp3 = Employee('Hans','Mueller', 100000)

# print(emp1.fullname())
# print(emp2.fullname())
# print(emp3.fullname())

# #print(f"Full Name: {emp1.fullname()}\nWage: {emp1.pay}")

# print(emp1.fullname())
# print(f"{emp1.fname} {emp1.lname}")
# print("{} {}".format(emp1.fname,emp1.lname))

# print(emp1.fullname())
# print(Employee.fullname(emp1)) #Have to mention the object inside 

#1 Using the cat/dog class, create three tight methods: meow, purr, tails_swoosh/ bark, whimper, tail_wag.
#When you call the meow method it should say meow Meow, purr purr, swoosh swoosh

# class Cat:
#     def __init__(self,name,age,breed): #create the contstructor function
#         self.name = name                #create the attributes
#         self.age = age
#         self.breed = breed
#     def meow(self):
#         return 'meow meow'
#     def purr(self):
#         return 'purr purr'
#     def swoosh(self):
#         return 'swoosh swoosh'

# #create the objects and reference the class
# cat1 = Cat('Bruno','3', 'Lion')
# cat2 = Cat('Babs',5, 'Tiger')

# #pass the arguments
# print(cat1.name)
# print(cat2.name)
# print(cat1.age)
# print(cat1.meow()) #when printing call the object.function()
# print(Cat.meow(cat2))
# print(cat2.purr())
# print(cat2.swoosh())

#2. Using the Truck class, create two methods:
#Method 1: cash_discount() gives 10% discount if customer pays cash
#Method 2: interest(): add 5% interest on a 12-month payment
#                       add 8% interest on a 24- month payment
#                       add 10% interest on 36-month payment
#                       return payment plan not found  if other than 12/24/36
# regular code (input) the class, objects, ect
# IF you choose payment plan option1/2/3 or cash 

class Truck:
    def __init__(self, brand, model, year, color, price):
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color
        self.price = price

    def cash_discount(self):
        return self.price/1.05

    def interest(self):
        if choice == 12:
            return self.price*0.05+self.price
        elif choice == 24:
            return self.price*0.08+self.price
        elif choice == 36:
            return self.price*0.10+self.price

# discount = 0.10
# interest12 = .05
# interest24 = .08
# interest36 = 0.10
#def interest(self):
        

truck1 = Truck('Chevy', 'Silverado', '2017', 'white', 85000)
truck2 = Truck('Toyota', 'Tacoma', 2020, 'blue', 45000)

choice = int(input('Enter a payment plan opition 12 months, 24 months or 36 months'))
if choice == 12:
    print(truck1.interest())#add fancy print .2f
elif choice == 24:
    print(truck1.interest())#add fancy print .2f
elif choice == 36:
    print(truck1.interest())#add fancy print .2f
else:
    print("Payment plan option not valid. Try again")


# print(truck1.brand)
# print(truck1.model)
# print(truck1.price)
# print(truck2.brand)
# print(truck2.model)
# print(truck2.price)

print(truck1.cash_discount())

#3. Using the TripCalc class, create two methods:
#Method 1: Returns total trip cost
#Method 2: Return total number of fill ups

#4. Using the triangle class, create two methods:
#M1: returns the area of a triangle (Use Heron's formula - what is that?)
#M2: Returns the type of triangle 

#Create a math class that accepts two params, num1 and num2
#add 4 methods: add, sub, mult, divide
#each method returns the operation
#Create a user menue
#Complete APP

#6 Challenge - create a converter app using classes 
#Class 1: Temperature 
#Class2: Distance
#Class 3: Weight 