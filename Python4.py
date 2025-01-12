import keyword
print(keyword.kwlist)

# Example1 - Revising the use of constructor
class ClassTen:
    name1 = "John Terry"
    def __init__(self,name1):
        print (f"""The Captain of the Chelsea Mens Team is \"{self.name1}\".
The Vice Captain of the Chelsea Mens Team is \"{name1}\".""")
player1 = ClassTen("Frank Lampard")

print()

# Example2
# Create an "Employee" class with constructor accepting 4 parameters - name, age, department, salary
# Create a method "display" which will print the values of the Employee
class Employee:
    def __init__(self,name,age,dept,sal):
        self.name = name
        self.age = age
        self.dept = dept
        self.sal = sal
    def display(self):
        return f"""Employee Details:
The Employee Name is \"{self.name}\".
The Employee Age is \"{self.age}\".
The Employee Department is \"{self.dept}\".
The Employee Salary is \"{self.sal}\"."""

# Creating the objects and
employee1 = Employee("James Ballanger", 35, "Technology", 100000)
employee2 = Employee("Presley Rbello", 33, "Human Resources", 72000)
employee3 = Employee("Jaden Monteiro", 21, "Security", 55000)
employee4 = Employee("Gaurav Singh", 24, "IT Infrastructure", 64000)

print(employee1.display())
print()
print(employee2.display())
print()
print(employee3.display())
print()
print(employee4.display())

print()

# In Python, the Constructor can only be defined as "def __init__(self)".
# However, we can also create an additional constructor to print values as well.
# Also remember, we can never return any value using a constructor, however there is an exception.
# We make use of the String Constructor which is defined as "def __str__(self)".
# This constructor will return a string type of constructor only. It will not return an integer value.

# Example3
# In Example2, we made use of a constructor for the instance variables and method to display the value.
# In Example3, we will make use of 2 constructors. 1 for instance variables and other to return the value.
# However, this example will be a fail because we are making use of an __str__(self) constructor and try to return an integer value.
class Player:
    def __init__(self,name,age,position,skill):
        self.name = name
        self.age = age
        self.position = position
        self.skill = skill
#     def __str__(self):
#         return f"""Player Attributes:
# The Player Name is \"{self.name}\".
# The Player Age is \"{self.age}\".
# The Player Skill Level is \"{self.position}\".
# The Player Position is \"{self.skil}\"."""

    def __str__(self):
        return self.name,self.age,self.position,self.skill

# As seen below when the object is printed, an error will be thrown because integer type variable cannot be printed.
# "age" and "skill" cannot be printed.

player1 = Player("Mohammed Salah",33,"Left Wing Attacker",90)
player2 = Player("Cole Palmer",22,"Centre Attack Midfield",86)
player3 = Player("Erling Haaland",23,"Striker",87)
player4 = Player("Sandro Tonali",23,"Centre Midfield",85)

print(player1)

print()

# Example4
class Ontario:
    def __init__(self,city,population):
        self.city = city
        self.population = population
    def __str__(self):
        return self.city
    def meth14(self):
        return self.population
city1 = Ontario("Ottawa",1.8)
city2 = Ontario("Toronto",3.2)
city3 = Ontario("Hamilton",0.75)
city4 = Ontario("Kitchener",0.50)

print("The Canadian Cities with their respective populations(millions): ")
print(f"{city1}, {city1.meth14()}")
print(f"{city2}, {city2.meth14()}")
print(f"{city3}, {city3.meth14()}")
print(f"{city4}, {city4.meth14()}")

print()

# INHERITANCE
# Defined as acquiring all variables(attributes) and methods(behavior) from once class to another class.
# Inheritance ensures code reusability and avoids duplication.
# Sub-Class/Derived Class inherits all the properties from the Base/Super Class.
#
# TYPES OF INHERITANCE
# Single Level, Multi Level, Heirarchy, Multiple Level.

# Example5 - Single Level Inheritance
# Create the Base Class
class Manufacturer:
    def __init__(self,make,model,year,color):
        self.make = make
        self.model = model
        self.year = year
        self.color = color
    # Create a method in the Base Class
    def display_manufacturer(self):
        return f"""Vehicle Details:
Make: {self.make}\nModel: {self.model}\nYear: {self.year}\nColor: {self.color}"""

# Create the Derived Class - Inheritance
class Vehicle(Manufacturer):
    def __init__(self,make,model,year,color,cost):
        super().__init__(make,model,year,color)
        self.cost = cost
    # Create a method in the Sub Class
    def display_vehicle(self):
        # Store the method from parent class in the variable
        manufacturer_details = self.display_manufacturer()
        return f"""{manufacturer_details}\nCost:{self.cost}"""

# Create an Object of the Derived/Sub Class
vehicle1 = Vehicle("Mercedes","SLS AMG",2022,"Silver", 165000)
vehicle2 = Vehicle("BMW", "M5", 2020, "Blue", 110000)
vehicle3 = Vehicle("Audi", "R8", 2021, "Orange", 200000)
vehicle4 = Vehicle("Chevrolet", "Corvette", 2019, "Yellow", 120000)

print(vehicle1.display_vehicle())
print()
print(vehicle2.display_vehicle())
print()
print(vehicle3.display_vehicle())
print()
print(vehicle4.display_vehicle())

print()

# Example6 - Single Level Inheritance
# In this example we will ask the User to input the details and then print the values almost similar to Example5
# Create the Base Class
class Basketball:
    def __init__(self,input_name,input_team,input_position):
        self.input_name = input_name
        self.input_team = input_team
        self.input_position = input_position
    def player_info(self):
        return f"""The NBA info for the Player in the 2024/2025 season:
Name: {self.input_name}\nTeam: {self.input_team}\nPosition: {self.input_position}"""
# Create the Sub Class and inheriting the properties from the Base Class
class Player(Basketball):
    def __init__(self,input_name,input_team,input_position,input_age,input_height,input_weight):
        super().__init__(input_name,input_team,input_position)
        self.input_age = input_age
        self.input_height = input_height
        self.input_weight = input_weight
    def physical_info(self):
        player_details = self.player_info()
        return f"""{player_details}\nAge: {self.input_age}\nHeight: {self.input_height}\nWeight: {self.input_weight}"""
input_name = input("Please enter the Player Name: ")
input_team = input("Please enter the NBA Team Name: ")
input_position = input("Please enter the Player Position: ")
input_age = input("Please enter the Age: ")
input_height = input("Please enter the Height: ")
input_weight = input("Please enter the Weight: ")
print()
player1 = Player(input_name,input_team,input_position,input_age,input_height,input_weight)
print(player1.physical_info())

# Example7 - SINGLE LEVEL INHERITANCE
# In this example we will ask the User to input the details and then print the values similar to Example6 - RE-PRACTICE

# Create the Base Class
class Soccer:
    # Create the Constructor with the required instance variables
    def __init__(self,input_name,input_nationality,input_club,input_position):
        self.input_name = input_name
        self.input_nationality = input_nationality
        self.input_club = input_club
        self.input_position = input_position
    # Create a method to display the Player Details
    def player_info(self):
        return f"""The Player details for the 24/25 season are:
Player Name: {self.input_name}\nNationality: {self.input_nationality}\nClub: {self.input_club}\nPosition: {self.input_position}"""

# Create a Sub-Class that will inherit the properties of the Base Class
class Player(Soccer):
    # Create the constructor
    def __init__(self,input_name,input_nationality,input_club,input_position,input_height,input_age,input_skill):
        super().__init__(input_name,input_nationality,input_club,input_position)
        self.input_height = input_height
        self.input_age = input_age
        self.input_skill = input_skill
    def display_playerdetails(self):
        player_stats = self.player_info()
        return f"""{player_stats}\nHeight: {self.input_height}\nAge: {self.input_age}\nSkill: {self.input_skill}"""

# Ask the User to input the values and store in the variable
input_name = input("Please enter the Player Name: ")
input_nationality = input("Please enter the Player Nationality: ")
input_club = input("Please enter the Player Club: ")
input_position = input("Please enter the Player Position: ")
input_height = input("Please enter the Player Height: ")
input_age = input("Please enter the Player Age: ")
input_skill = input("Please enter the Player Skill: ")

print()

# Create an object and store in the variable
player1 = Player(input_name,input_nationality,input_club,input_position,input_height,input_age,input_skill)

# Print the values entered by the User
print(player1.display_playerdetails())

print()

# Example8 - MULTI LEVEL INHERITANCE
# Create the Base/Parent Class
class Addition:
    def add(self,input_a,input_b):
        return f"""The Addition of the 2 numbers equals \"{input_a+input_b}\"."""
# Create a Sub Class of the Base Class
class Subtraction(Addition):
    def sub(self,input_c,input_d):
        while True:
            if input_c < input_d:
                print ("The number entered for \"C\" cannot be lesser than number entered for \"D\".")
                input_c = float(input("Please re-enter the number for \"C\": "))
                input_d = float(input("Please re-enter the number for \"D\": "))
            else:
                return f"""The Subtraction of the 2 numbers equals \"{input_c-input_d}\"."""
# Create a 2nd Sub Class of the 1st Sub Class
class Multiplication(Subtraction):
    def mul(self,input_e,input_f):
        return f"""The Multiplication of the 2 numbers equals \"{input_e*input_f}\"."""
# Create a 3rd Sub Class of the 2nd Sub Class
class Division(Multiplication):
    def div(self,input_g,input_h):
        while True:
            if input_g == 0 or input_h == 0:
                print ("Input value entered cannot be 0 to perform division.")
                input_g = float(input("Please re-enter the number for \"G\": "))
                input_h = float(input("Please re-enter the number for \"H\": "))
            else:
                return f"""The Division of the 2 numbers equals \"{input_g/input_h}\"."""

input_a = float(input("Enter the Number A: "))
input_b = float(input("Enter the Number B: "))
input_c = float(input("Enter the Number C: "))
input_d = float(input("Enter the Number D: "))
input_e = float(input("Enter the Number E: "))
input_f = float(input("Enter the Number F: "))
input_g = float(input("Enter the Number G: "))
input_h = float(input("Enter the Number H: "))

print()
# Create the Object using 3rd Sub Class and store in a variable
calc1 = Division()
# Using the Object call the methods from the preceding Classes
print(calc1.add(input_a,input_b))
print()
print(calc1.sub(input_c,input_d))
print()
print(calc1.mul(input_e,input_f))
print()
print(calc1.div(input_g,input_h))

print()

#EXAMPLE9 - HEIRARCHAL LEVEL INHERITANCE
#Create the Base/Parent Class
class University:
    # Create a Constructor
    def __init__(self,input_university,input_campus,input_degree):
        self.input_university = input_university
        self.input_campus = input_campus
        self.input_degree = input_degree
    # Create a method in the Base Class
    def display_University(self):
        return f"""Details of the Academic Program offered by the University: .
University: {self.input_university}
Campus: {self.input_campus}
Degree: {self.input_degree}"""

# Create the 1st Sub-Class - Student Information
class StudentInfo(University):
    def __init__(self,input_university,input_campus,input_degree,input_name,input_id,input_age,input_gender):
        super().__init__(input_university,input_campus,input_degree)
        self.input_name = input_name
        self.input_id = input_id
        self.input_age = input_age
        self.input_gender = input_gender
    def display_StudentInfo(self):
        return f"""Student Information:
Student Name: {self.input_name}
Student ID: {self.input_id}
Student Age: {self.input_age}
Student Gender: {self.input_gender}"""

#Create the 2nd Sub Class - Academic Grades
class StudentGrades(University):
    def __init__(self,input_university,input_campus,input_degree,input_sem,input_gpa):
        super().__init__(input_university,input_campus,input_degree)
        self.input_sem = input_sem
        self.input_gpa = input_gpa
    def display_StudentGrades(self):
        return f"""Student Academic Grades:
Semester: {self.input_sem}
GPA: {self.input_gpa}"""
    def calc_StudentGrades(self):
        if self.input_gpa == 0:
            print("The GPA entered cannot be 0")
            input_gpa = input("Please re-enter the GPA: ")
        elif self.input_gpa < 1.0:
            print(f"""The result obtained for GPA \"{self.input_gpa}\" is FAIL""")
        elif self.input_gpa >= 1.0 and self.input_gpa < 2.0:
            print(f"""The result obtained for GPA \"{self.input_gpa}\" is SATISFACTORY""")
        elif self.input_gpa >= 2.0 and self.input_gpa < 3.0:
            print(f"""The result obtained for GPA \"{self.input_gpa}\" is GOOD""")
        elif self.input_gpa >= 3.0 and self.input_gpa <= 4.0:
            print(f"""The result obtained for GPA \"{self.input_gpa}\" is DISTINCTION""")
        else:
            print("The GPA entered is not a valid value.")
            input_gpa = input("Please re-enter the GPA: ")

print("Enter the Course Information.")
input_university = input("Please enter the University: ")
input_degree = input("Please enter the Degree: ")
input_campus = input("Please enter the name of the Campus: ")

print()

print("Enter the Student Details.")
input_name = input("Please enter the Student Name: ")
input_id = input("Please enter the Student ID: ")
input_age = input("Please enter the Student Age: ")
input_gender = input("Please enter the Student Gender: ")

print()

print("Enter the Student Grades.")
input_sem = int(input("Please enter the Academic Semester: "))
input_gpa = float(input("Please enter the GPA earned in the semester : "))

print()

# Create an object of the 1st Child Class and assign it to a variable
student_info = StudentInfo(input_university,input_campus,input_degree,input_name,input_id,input_age,input_gender)
print(student_info.display_University())
print()
print(student_info.display_StudentInfo())

print()

# Create an object of the 2nd Child Cass and assign it to  variable
student_grades = StudentGrades(input_university,input_campus,input_degree,input_sem,input_gpa)
print(student_grades.display_StudentGrades())
print(student_grades.calc_StudentGrades())

print()

# EXAMPLE10 - MULTIPLE LEVEL INHERITANCE
# Create the 1st Base Class
class Force:
    def __init__(self,input_mass,input_accl):
        self.input_mass = input_mass
        self.input_accl = input_accl
    def calc_force(self,force):
        force = self.input_mass * self.input_accl
        return force
# Create the 2nd Base Class
class Speed:
    def __init__(self,input_distance,input_time):
        self.input_distance = input_distance
        self.input_time = input_time
    def calc_speed(self,speed):
        speed = self.input_distance/self.input_time
        return speed
# Create the 3rd Base Class
class Voltage:
    def __init__(self,input_current,input_resistance):
        self.input_current = input_current
        self.input_resistance = input_resistance
    def calc_voltage(self,voltage):
        voltage = self.input_current * self.input_resistance
        return voltage
# Create the Sub-Class depicting Multiple Inheritance
class Physics(Force,Speed,Voltage):
    def __init__(self,input_mass,input_accl,input_distance,input_time,input_current,input_resistance):
        Force.__init__(self,input_mass,input_accl)
        Speed.__init__(self,input_distance,input_time)
        Voltage.__init__(self,input_current,input_resistance)
    def display_physics(self):
        force_result = self.calc_force(Force)
        speed_result = self.calc_speed(Speed)
        voltage_result = self.calc_voltage(Voltage)
        return f"""The final results:
{force_result} N\n{speed_result} m/s\n{voltage_result} V"""

input_mass = float(input("Enter the Mass of the Vehicle: "))
input_accl = float(input("Enter the Acceleration of the Vehicle: "))
print()
input_distance = float(input("Enter the distance of the Race Track: "))
input_time = float(input("Enter the Time taken for vehicle to complete 1 lap of the Race Track: "))
print()
input_current = float(input("Enter the Current passed through the appliance: "))
input_resistance = float(input("Enter the Resistance of the appliance: "))

print()

# Create an Object of the Sub Class and the properties of 3 Parent classes will be inherited
physics = Physics(input_mass, input_accl, input_distance, input_time, input_current, input_resistance)
print(physics.display_physics())

print()

# OVERRIDING
#Redefining a method in the sub class that is already defined in the parent class.
# In Overriding, only the output of the latest method will be implemented.
# The "super()" keyword is used to invoke the overridden method in the Parent Class.
# It is used to call the "__init__" method in the parent class from within the child class.
# This ensures the initialization logic in the parent class is executed.
# Can also be used for variables.
# Requires inheritance as it occurs between the Parent and Child class.

#EXAMPLE11 - OVERRIDING
# Create the Parent Class
class Physics:
    def __init__(self,name):
        self.name = name
    def calculate(self):
        """Default method to calculate"""
        return f"No specific calculations implemented."
# Create the 1st child class and inherit properties from parent class
class Force(Physics):
    def __init__(self,name,mass,accl):
        super().__init__(name)
        self.mass = mass
        self.accl = accl
    def calculate(self):
        """Calculate Force using the formula, Force = m.a"""
        force = self.mass * self.accl
        return f"Force: {force}N"
# Create the 2nd child class and inherit properties from parent class
class Energy(Physics):
    def __init__(self,name,mass,velocity):
        super().__init__(name)
        self.mass = mass
        self.velocity = velocity
    def calculate(self):
        """Calculate Energy using the formula, Energy = 0.5.mv^2"""
        energy = 0.5 * self.mass * self.velocity**2
        return f"Kinetic Energy: {energy}J"
# Create the 3rd child class and inherit properties from the parent class
class Pressure(Physics):
    def __init__(self,name,force,area):
        self.force = force
        self.area = area
    def calculate(self):
        """Calculate the Pressure using formula, Pressure = F/A"""
        pressure = self.force/self.area
        return f"Pressure: {pressure}Pa"

# Create the Objects for each subclass
force_calculation = Force("Force",10,2.5)
energy_calculation = Energy("Energy",21,3)
pressure_calculation = Pressure("Pressure",77,11)

print(force_calculation.calculate())
print(energy_calculation.calculate())
print(pressure_calculation.calculate())

print()

# EXAMPLE12 - OVERRIDING
# Create the parent Cc
class Shape:
    def __init__(self,name):
        self.name = name
    def volume(self):
        """Default method to calculate the volume"""
        return f"This is the method to be overridden."
# Create the 1st child class to inherit the properties of the parent class
class Cylinder(Shape):
    def __init__(self,name,radius1,height1):
        super().__init__(name)
        self.radius1 = radius1
        self.height1 = height1
    def volume(self):
        """Calculate the volume of the Cylinder"""
        volume_cylinder = 3.14 * self.height1 * self.radius1**2
        return f"Volume of the Cylinder: {volume_cylinder}m^3"
# Create the 2nd child class to inherit the properties of the parent class
class Cone(Shape):
    def __init__(self,name,radius2,height2):
        self.radius2 = radius2
        self.height2 = height2
    def volume(self):
        """Calculate the volume of the Cone"""
        volume_cone = (1/3) * 3.14 * self.height2 * self.radius2**2
        return f"Volume of the Cone: {volume_cone}m^3"
# Create the 3rd child class to inherit the properties of the parent class
class Pyramid(Shape):
    def __init__(self,name,length,width,height3):
        super().__init__(name)
        self.length = length
        self.width = width
        self.height3 = height3
    def volume(self):
        """Calculate the volume of the Pyramid"""
        volume_pyramid = (1/3) * self.length * self.width * self.height3
        return f"Volume of the Pyramid: {volume_pyramid}m^3"

print()

print("Volume of Cylinder: ")
radius1 = float(input("Please enter the radius of the Cylinder: "))
height1 = float(input("Please enter the height of the Cylinder: "))

print()

print("Volume of Cone: ")
radius2 = float(input("Please enter the radius of the Cone: "))
height2 = float(input("Please enter the height of the Cone: "))

print()

print("Volume of Pyramid: ")
length = float(input("Please enter the length of the Pyramid: "))
width = float(input("Please enter the width of the Pyramid: "))
height3 = float(input("Please enter the height of the Pyramid: "))

# Create the Object for the respective classes.
cylinder_volume = Cylinder("Volume of Cylinder",radius1,height1)
cone_volume = Cone("Volume of Cone",radius2,height2)
pyramid_volume = Pyramid("Volume of Pyramid",length,width,height3)

print()

print(cylinder_volume.volume())
print()
print(cone_volume.volume())
print()
print(pyramid_volume.volume())

print()

# EXAMPLE13 - VARIABLE OVERRIDE
# 2 Variables with the same name belonging to 2 different classes
# Latest class with variable value will be obtained in result
class Parent:
    name1 = 'John'
class Child(Parent):
    name1 = 'Susan'
name = Child()
print(name.name1)

# EXAMPLE14 - VARIABLE OVERRIDE
# 2 Variables with the same name belonging to 2 different classes
# However we will print values of both variables using the super() function
class Father:
    name2 = 'Isak'
class Son(Father):
    name2 = 'Aleksandr'
    def meth1(self):
        print(super().name2)
# Create the Object and store in variable.
name = Son()
# Print the Name in the child class.
print(name.name2)  # This will print "Aleksandr".
# Print the Name in the parent class.
Son().meth1() # This will print "Isak".

print()

# EXAMPLE15 - METHOD OVERRIDE
# Parent Class.
class Bank:
    def __init__(self,name):
        self.name = name
    def calculate(self):
        """Default method to calculate the Simple Interest"""
        print("Simple Interest = (Principal x Years x Rate)/100")
# 1st Child Class inherit properties of the Parent Class
class RoyalBank(Bank):
    def __init__(self,name,principal1,years1,rate1):
        super().__init__(name)
        self.principal1 = principal1
        self.years1 = years1
        self.rate1 = rate1
    def calculate(self):
        """Calculate the Simple Interest offered at Royal Bank of Canada"""
        rbc_interest = (self.principal1*self.years1*self.rate1)/100
        return f"""Royal Bank Canada(RBC):
1. Principal = ${self.principal1}
2. Number of Years: {self.years1}
3. Rate of Interest: {self.rate1}
Calculated Simple Interest: ${rbc_interest}"""
# Create a 2nd Child Class inherit properties of the Parent Class.
class TorontoDominion(Bank):
    def __init__(self,name,principal2,years2,rate2):
        super().__init__(name)
        self.principal2 = principal2
        self.years2 = years2
        self.rate2 = rate2
    def calculate(self):
        """Calculate the Simple Interest offered at Toronto Dominion Bank of Canada"""
        td_interest = (self.principal2*self.years2*self.rate2)/100
        return f"""Toronto Dominion Bank(TD):
1. Principal = ${self.principal2}
2. Number of Years: {self.years2}
3. Rate of Interest: {self.rate2}
Calculated Simple Interest: ${td_interest}"""

print()
# Object creation
bank1 = RoyalBank("RBC",1200,3,3.2)
bank2 = TorontoDominion("TD",1200,3,3.5)
print(bank1.calculate())
print()
print(bank2.calculate())

print()

# POLYMORPHISM is basically OVERLOADING.
# Polymorphism allows objects of different classes to be treated as objects of a common Superclass.
# Basically, one thing can have many forms.

# OVERRIDING
# Redefining a method in the subclass that is already defined in the parent class.
# Requires inheritance as it occurs between the Parent and Child class.
# If there are 3 methods being overridden, then python considers the latest implemented method.
# To overcome this, the "super()" keyword is used to invoke the method.

# OVERLOADING.
# Overloading is a feature that allows the class to have multiple methods with the same name but different parameters.
# Does not require inheritance. Occurs within the same class.

# EXAMPLE16 - OVERLOADING
class Calculator:
    def add(self,a,b=0,c=0):
        return f"Addition of the numbers equals {a+b+c}."
# Object created
calculator = Calculator()
# Overloading - Different parameters used for the same method in the class
print(calculator.add(2))
print(calculator.add(3,8))
print(calculator.add(5,2,7))

print()

# EXAMPLE17 - OVERLOADING
class Thermodynamics1:
    def thermo(self,energy=0,work=0):
        """Heat added to system = Change in Internal Energy + Work done"""
        heat = float(energy) + float(work)
        return f"""\"Using the 1st Law of Thermodynamics:\"
Heat added to the system equals {heat}"""
class Thermodynamics2:
    def thermo(self,absheat=1,rejheat=1):
        """Efficiency of Heat Engines = 1 - (Heat Absorbed/Heat Rejected)"""
        efficiency = 1 - (float(absheat)/float(rejheat))
        return f"""\"Using the 2nd Law of Thermodynamics:\"
Efficiency of the Heat Engine equals {efficiency}%"""

print()

thermo1 = Thermodynamics1()
print(thermo1.thermo())
print()
print(thermo1.thermo(16,3))
print()
print(thermo1.thermo(7.5))
print()

thermo2 = Thermodynamics2()
print(thermo2.thermo())
print()
print(thermo2.thermo(0.11,0.24))
print()
print(thermo2.thermo(0.31))

print()

# Topics covered:
# Classes
# Objects
# Inheritance - Types, Static & Instance methods, Constructors, Overriding.
# Polymorphism - Overloading.
























































