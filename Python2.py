# #Import the required Python keywords
# import keyword
#
# #Print the Python keywords
# print(keyword.kwlist)
#
# print()
#
# #Function is a set of statements that will perform a task
# #1 - Function declaration/creation
# #2 - Calling/Invoking the Function
#
# #Create a function in Python - Example 1
# def add_1(a,b):
#     return a+b
# result = add_1(10.5,5)
# print(result)
#
# print()
#
# #Create a function using parameter and then call the function - Example 2
# def myfun(name):
#     print('Hello', name)
# #Call the function
# myfun('Jensen Ackles')
#
# print()
#
# #Create a function to perform the subtracting of 2 numbers - Example 3
# #Create the method
# def sub(a,b):
#     #Perform the subtraction operation
#     return a-b
# #Call the method by assigning values to the parameters passed and store in variable
# result = sub(13.52,11.32)
# #Print the result
# print("The subtraction result is", result)
#
# print()
#
# #Create a function to perform the multiplication of 2 numbers - Example 4
# def mult(a,b):
#     return a*b
# mult(7.1,6.1)
# print(f"The multiplication result is \"{mult(7.1,6.1)}\"")
#
# print()
#
# #Create a method to display the "none" value
# #If nothing is returned then the value displayed will always be "none"
# def none():
#     return
# none()
# print(f"The result is \"{none()}\"")
#
# print()
#
# #Check the output to see when the "print" statement is not used but only "return"
# def div(a,b):
#     return a/b
# division = div(33.90, 11.30)
# # print(division)
#
# print()

# #Variables
# #Global Variables - Variables created outside the function and can be accessed anywhere
# #Local Variables - Variables created inside the function and can be accessed only within the function
# #When the Global Variable is used inside the function then, "global" keyword is required to be used for variable
#
# #Create a method to demonstrate an example of Global and Local variable
# global_var1 = 3.92
# def meth1():
#     local_var1 = 4.65
#     print(local_var1)
#     print(global_var1)
# meth1()
#
# print()

# #Create a method to demonstrate a mathematical calculation using a method and then calling the method
# def meth2(global_var2, local_var2):
#     return global_var2/local_var2
# meth2(33.3, 11.1)
# print(f"The result is {meth2(33.3, 11.1)}")
#
# print()
#
# #Create a method to create a global variable outside the function and then use it in the function to print value
# global_var3 = 7
# def meth3(local_var3):
#     return global_var3**local_var3
# meth3(3)
# print(f"The result is {meth3(3)}")
#
# print()

# #Create a function to implement the global keyword for a variable
# #Global Variable created
# var4 = 12.5
# def meth5(var5):
#     #This is considered as the new global keyword and will replace the global keyword value represented outside the function
#     global var4
#     var4 = 13.5
#     return var4-var5
# meth5(11.4)
# print(f"The subtraction result is {meth5(11.4)}")
#
# print()

# #Create  method to convert the temperature from Fahrenheit to Celsius
# #Create a Global Variable
# fah_userinput1 = 75
# def fahtocels():
#     global fah_userinput1
#     fah_userinput1 = float(input("Please enter the temperature in Fahrenheit:"))
#     cels = (fah_userinput1 - 32)*5/9
#     print(f"The temperature {fah_userinput1} entered in Fahrenheit equals {cels} degree Celsius")
# fahtocels()
#
# print()

# #Create a method where the Global variable is printed outside the function
# def meth6():
#     global var6
#     var6 = 13.81
#     print(var6)
# meth6()
# #Print the global variable outside the function
# print(var6)
#
# print()

# #Arguments/Paramters can be passed into the function
# #1-Positional Arguments
# #2-Keyword Arguments
# def meth7(a,b):
#     print(a,b)
# meth7(10.5,20.5) #Positional Argument
#
# print()
#
# def meth8(c,d):
#     print(c,d)
# meth8(d=33.3,c=11.1) #Keyword Argument
#
# print()

# #Create a function where a default value is added to the Positional Argument
# #Creating a method to calculate Power
# def meth9(a,b=5.5):
#     print(a,b)
# #Default value for b added as "2.2" but
# meth9(7,3)
# meth9(21)
#
# print()

# #Create a function to calculate the Power
# def calcpower():
#     amp_input1 = float(input("Enter the value in Ampere: "))
#     print()
#     volt_input2 = float(input("Enter the value in Voltage: "))
#     print()
#     watt = amp_input1 * volt_input2
#     print(f"The calculated power equals {watt} Watts.")
#     print()
#     horsepower = watt/746
#     print(f"The Power calculated equals {horsepower} HP")
# calcpower()
#
# print()

# #Positional Argument must always occur before the Keyword Argument
# #Create a function using Keyword Arguments
# def meth10(a,b,c):
#     print(a,b,c)
# meth10(15.3, 16.7, 18.1) #Positional Argument
# meth10(a=21.6,b=22.7,c=24.3) #Keyword Argument
# meth10(33.3,35.5,c=39.9) #Positional & Keyword Argument
# # meth10(a=46.6,b,c) #Positional Argument can never follow a Keyword Argument
# # meth10(52.2,58.8,b=54.4) #Already representing b as a Positional Argument
#
# print()

# #Functions can return multiple values
# def meth11(a,b):
#     if a>b:
#         return a-b
#     else:
#         return a+b
# #print(meth11(46.6, 47.3))
# res = meth11(48.6,44.4)
# print(res)
#
# print()

# def meth12(c,d):
#     if c>d:
#         return c,d
#     if c<d:
#         return d,c
# meth12(31.1,33.3)
# res = meth12(31.1,33.3)
# print(res)
# print(type(res))
#
# print()
