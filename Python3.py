# #Python is a structured and object-oriented programming language (OOP)
# #Python is OOP because of the following features:
# # Class
# # Object/Instance
# # Inheritance
# # Polymorphism
# # Overloading
#
# #Classes and Objects in Python
#
# #Example
# #Employee - John, Scott, Mary etc.
# #Employee is the Class ; John is the Object.
#
# # Definition of a Class.
# # Class is a collection of variables and methods.
# # Classes is a logical entity do not occupy space in the memory.
# # Class is a blueprint.
# # 1 Class can have multiple objects but the objects are independent.
#
# # Definition of an Object/Instance.
# # An Object is an instance of a class.
# # Object is a physical entity that occupies space.
# # Objects are independent of each other.
# # Objects make use of the same methods and variables from the class but their values are different.
#
# #Function and Method
# #A function is written independently.
# #A method is also a function but written inside a class.
#
# #Import python keywords
# import keyword
# #Print the Python keyword list
# print(keyword.kwlist)
#
# print()
# #
# #Create a Class
# class ClassOne:
#     # When a method is created inside the class, the "self" parameter needs to be included by default
#     # "self" argument also indicates this method belongs to this class and represents the class
#     def meth1(self):
#         #"pass" indicates that this method is empty and not being used
#         pass
#     def meth2(self):
#         userinput1 = str(input("Please enter the Employee Name: "))
#         print()
#         print(f"The Employee Name entered is \"{userinput1}\" and will be saved to the Employee database")
# # ClassOne()
# #Create an Object and store in variable
# obj1 = ClassOne()
# #You can call the method using the Class directly OR
# ClassOne().meth1() #Since the method is empty, nothing will be printed
# #You can call the method using the Object
# obj1.meth2()
#
# print()

# # 2 Types of methods that can be defined in the class
# # 1 - Instance Method - A method that can be called only through Object
# # 2 - Static Method - A method that is called directly using the Class
#
# # To define a Static Method, we use the annotation "@staticmethod"
# # A Static Method is common to every object
# # To call the Static Method, we can use the Object and the Class directly.
#
# # 'self' in Instance method.
# # An instance is nothing but an object of the specified class.
# # 'self' is a reference to the instance/object of the class that is calling the method.
# # It must be explicitly declared as the first parameter in instance methods.
# # It is used to access instance attributes and methods within the class.
# # It is automatically passed when you call the method on an instance/object.
#
# # 'self' in Static method
#
# class ClassTwo:
#     #Instance Method
#     def meth3(self):
#         pass
#     #Static Method
#     #Using the static method annotation
#     @staticmethod
#     def meth4(self, num1, num2):
#         total = self + num1 + num2
#         print(f"The result equals \"{total}\"")
#     #Instance Method
#     def meth5(self, name):
#         print(f"The Full Name of the Student is \"{name}\"")
# #
# #Create an Object
# ClassTwo()
# #Store the object in a variable
# obj2 = ClassTwo()
#
# #We can use the object to call the methods.
#
# #Using the object to call this method since it is not a Static method.
# #Since this method is empty and not being used, it will not display any result.
# obj2.meth3()
# print()
# #This is a static method and hence we used the class directly to call this method
# ClassTwo.meth4(11.6, 13.3, 22.7)
# print()
# #This is not a static method. If you use the object to cal this method then nothing will be printed.
# obj2.meth5("Dwayne")
#
# print()
#
# #VARIABLES
# #1 - Local Variables
# #2 - Global Variables
# #3 - Class Variables
#
# #Create a class and identify whether the values of Local, Global or Class variables are used
# class ClassThree:
#     #Class Variables
#     num1,num2, num3 = 3.7, 1.6, 1.1
#     #Create a method to perform subtraction
#     def meth6(self):
#         #We want to use the class variables inside this method
#         print(self.num1-self.num2-self.num3)
#     #Create a method to perform multiplication
#     def meth7(self):
#         #Use the cass variables inside this method
#         print(self.num1*self.num2*self.num3)
# #Above methods are Instance methods and hence can be called only by creating an object
# #Create an object and store in a variable
# obj3 = ClassThree()
# #Call the method using the Object
# obj3.meth6()
# print()
# obj3.meth7()
#
# print()
#
# #Combination of Local, Class & Global Variables.
# #Creating the Global Variables.
# num4,num5,num6 = 3.3, 4.4, 5.5
# #Create the Class.
# class ClassFour:
#     #Create the Class Variables
#     num7,num8,num9 = 6.6, 7.7, 8.8
#     def meth8(self,num10,num11,num12):
#         #Local variables num10, num11 and num12 can be directly accessed
#         print(f"The addition of the \"Local Variables\" equals \"{num10+num11+num12}\".")
#         #Class variables cannot be directly accessed. They will need the help of the "self" argument
#         print(f"The addition of the \"Class Variables\" equals \"{self.num7+self.num8+self.num9}\".")
#         #Global Variables can be accessed from anywhere
#         print(f"The addition of the \"Global Variables\" equals \"{num4+num5+num6}\".")
# #Create an Object and store in the variable
# obj4 = ClassFour()
# #Use the Object to call the Instance Method
# obj4.meth8(9.9, 10.10, 11.11)
#
# print()
#
# #Using the same variables for Global, Class & Local Variables.
# #When variable representation is the same for global, class and local then, how can they be accessed.
# x,y = 17, 9 #Global Variables
# class ClassFive:
#     x,y = 3.3, 1.1   #Class Variables
#     def meth9(self, x, y):  #Local Variables
#         #Using only the Local Variables
#         print(f"The division of the \"local variables\" equals {x/y}.")
#         #Using the Class Variables
#         print(f"The multiplication of the \"class variables\" equals {self.x*self.y}.")
#         #Using the Global Variables - we make use of globals()['variable']
#         print(f"The subtraction of the \"global variables\" equals {globals()['x'] - globals()['y']}")
# obj5 = ClassFive()
# obj5.meth9(46.6, 31.1)
#
# print()
#
# #Creating multiple objects for a single class.
# class ClassSix:
#     def meth10(self, name1,name2):
#         print("The First Name of the Employee is: ")
#         print(name1)
#         print()
#         print("The Last Name of the Employee is: ")
#         print(name2)
#         print()
#         print("The Full Name of the Employee is: ")
#         print(name1, name2)
# obj6 = ClassSix()
# obj6.meth10('Ricardo', 'Quaresma')
# print()
# obj7 = ClassSix()
# obj7.meth10("Cristiano", "Ronaldo")
#
# print()

# #Methods & Constructors
#
# # Methods.
# # Methods can be given any names.
# # Methods are always written inside a class (Functions are written independently).
# # Methods can take arguments/parameters.
# # To invoke/call the method, we make use of objects (only for static method with annotation, we can use class directly).
# 
# # Constructors.
# # In python, Constructor name is fixed as "def __init__(self):".
# # A Constructor will never return any value.
# # Constructors can take arguments/parameters.
# # A Constructor is directly invoked/called at the time of Object creation itself.
# # Allows the instance variables to be initialized automatically when object is created.
# # If you have multiple objects to create, the constructor centralizes the initialization logic, making it reusable.
# # The constructor ensures all objects of a class have a consistent set of initialized attributes.
#
# # Instance Variables.
# # Instance variables are attributes that are specific to an instance of a class.
# # These variables are defined within a method (usually __init__).
# # They are prefixed with self to make them unique to the instance.
# # They store data that is specific to each object created from the class.
#
# #Example1 (without Constructor)
# class ClassSeven:
#     def meth11(self,name,age,department,salary):
#         return f"""The Employee Details are as follows:
#                     The Employee Name is {name}.
#                     The Employee Age is {age}.
#                     The Employee Department is {department}.
#                     The Employee Salary is {salary}."""
# # Create an Object and store in a variable
# emp1 = ClassSeven()
# # Print the results
# print(emp1.meth11("Adam Smith", 33, 'Technology', 92000))
# print()
# print(emp1.meth11("Karen Mcintosh", 24, 'Human Resources', 50000))
# print()
# print(emp1.meth11("Jake Tyler", 29, 'Finance', 72000))
# print()
# print(emp1.meth11("Stacey Bradley", 37, 'Administration', 64000))
#
# print()
#
# # Example2 (using Constructor)
# class ClassEight:
#     def __init__(self,autoname,model,year):
#         self.autoname = autoname
#         self.model = model
#         self.year = year
#     def meth12(self):
#         return f"""The Automobile details are:
#                     The Automobile Manufacturer is \"{self.autoname}\".
#                     The Model is \"{self.model}\".
#                     The Year of the model make is \"{self.year}\"."""
# # Create the Object, assign to a variable and initialize the instance variables as well
# auto1 = ClassEight("BMW",'M5', 2020)
# auto2 = ClassEight("Chevrolet", 'Corvette', 2019)
# auto3 = ClassEight("Lamborghini", 'Aventador', 2017)
# auto4 = ClassEight("Porsche", '911 GT', 2018)
#
# #Print the Output
# print(auto1.meth12())
# print()
# print(auto2.meth12())
# print()
# print(auto3.meth12())
# print()
# print(auto4.meth12())
#
# print()

