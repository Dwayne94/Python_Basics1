# #Import the required Python keywords
# import keyword
# #Print the Python keywords
# print(keyword.kwlist)
#
# print()
#
# #String Functions
#
# #Create a method to print the maximum, minimum and length of the defined variables
# def meth2():
#     var1 = "Liverpool implement a gegenpressing style of play"
#     var2 = 97, 43, 9.5, 13
#     #len() - displays the length of the variable
#     print("The length of the variable: ", len(var1))
#     #max() - displays the max value from the displayed values
#     print("The maximum value: ", max(var2))
#     #min() - displays the min value from the displayed values
#     print("The minimum value:", min(var2))
# meth2()
#
# print()
#
# #Create a method to display other used String Functions
# def meth8():
#     var16 = "!@#$%^&*()"
#     var17 = "789"
#     var18 = "async continue"
#     var19 = "MISSISSIPPI"
#     var20 = " "
#     #isalnum() - returns True if the string contains alphanumeric characters
#     print("The string \"!@#$%^&*()\" is alphanumeric: ", var16.isalnum())
#     #isdigit() - returns True if the string contains all numbers
#     print("The string \"789\" contains numbers only: ", var17.isdigit())
#     #isidentifier() - returns True if the string contains Python keywords
#     print("The string \"async continue\" contains Python keywords: ", var18.isidentifier())
#     #isupper() - returns True if the string is in upper case
#     print("The string \"MISSISSIPPI\" is in upper case: ", var19.isupper())
#     #islower() - returns True if the string is in lower case
#     print("The string \"MISSISSIPPI\" is in lower case: ", var19.islower())
#     #istrue() - returns True if the string contains space
#     print("The string \" \" contains space: ", var20.isspace())
# meth8()
#
# print()
#
#
# #Create a method to display details in coded format to print
# def meth3():
#     var3 = "The covert operation on the enemy will begin at 06:00 hours"
#     var4 = 69
#     var5 = 'E'
#     #id() function - converts the string to number format
#     print("The ID of the provided string is: ", id(var3))
#     #ord() function - converts the character to number
#     print("The represented number of the character is: ", ord(var5))
#     #chr() function - converts the number to character
#     print("The represented character of the number is: ", chr(var4))
#     #encode().hex() - converts the string into encoded hexadecimal format
#     print("The encoded version of the string in hexa format is: ", var3.encode().hex())
# meth3()
#
# print()
#
# #Looping statements - for & while
#
# #Create a method to print Odd Numbers in Descending order from 0 to 100
# def meth1():
#     var6 = 99
#     var7 = 0
#     print("The Odd numbers in descending order from 0 to 100: ")
#     for i in range(var6, var7, -2):
#         print(i)
# meth1()
#
# print()
#
# #Create a method to print Even Numbers in ascending order from 0 to 100. Do not print numbers from 45 to 55
# def meth4():
#     var8 = 2
#     var9 = 101
#     print("The Even numbers in ascending order from 0 to 100 (excluding 45 to 55): ")
#     for i in range(var8, var9, +2):
#         if 45 < i < 55:
#             continue
#         print(i)
# meth4()
#
# print()
#
# # Create a method to print the Odd Numbers in ascending order from 100 to 200. Do not print numbers from 110 to 120.
# def meth5():
#     var10 = 101
#     var11 = 201
#     print("The Odd numbers in ascending order from 100 to 200 (excluding 100 to 120): ")
#     for i in range(var10, var11, 2):
#         if 110 < i < 120:
#             continue
#         print(i)
# meth5()
#
# print()
#
# #Create a method to print the Even Numbers from 400 to 500 using the while loop
# def meth6():
#     var12 = 400
#     var13 = 501
#     print("The Even numbers from 400 to 501: ")
#     while var12 <= var13:
#         print(var12)
#         var12 += 2
# meth6()
#
# print()
#
# #Create a method to print the Odd Numbers 1 to 100 in descending order
# def meth7():
#     var14 = 99
#     var15 = 1
#     print("The Odd numbers from 1 to 100 in descending order: ")
#     while var14 >= var15:
#         print(var14)
#         var14 -= 2
# meth7()
#
# print()






# #COLLECTIONS - LIST, TUPLE, SET, DICTIONARY
#
# #LIST
# #Lists are represented with [] brackets
# #List are mutable
# #List is ordered and changeable
#
# #Create a method to represent a list containing different data types
# def meth9():
#     list1 = [1, 2, 3, 4, 5, 6.6, 7.7, 8.8, 9.9]
#     list2 = ['Rooney', 'Tevez', 'Ronaldo', 'Berbatov', 'Giggs']
#     list3 = [9, 8, 7, 6, 5, 'Four', 'Three', 'Two', 'One', 'Zero']
#     list4 = []
#     #Print the Lists
#     print(list1), print(list2), print(list3), print(list4)
#     print()
#
#     # Print the range of indexes of the Items in the List
#     print("Item 5, Item 6 and Item 7 in List 1 are", list1[4:7])
#     print("Item 3, Item 4 and Item 5 in List 2 are", list2[2::])
#     print("Item 4, Item 5, Item 6 and Item 7 in List 3 are", list3[-7:-3])
#     print()
#
#     #Accessing items in the list
#     print("The 1st item in List 1 is", list1[0])
#     print("The 4th item in List 2 is", list2[3])
#     print("The 10th item in List 3 is", list3[9])
#     print()
#
#     #Accessing items in the list using negative values will begin the count from reverse order
#     print("The 1st item in List 1 is", list1[-9])
#     print("The 10th item in List 2 is", list2[-1])
#     print("The 3rd item in List 3 is", list3[-8])
# meth9()
#
# print()

# #Create a method to prove that a LIST IS MUTABLE
# def meth10():
#     list5 = ['Newcastle United', 'Aston Villa', 'Tottenham Hotspur', 'Brentford', 'Westham United']
#     print("The original list is:", list5)
#     #Set new values to the list
#     list5[0] = 'Manchester United'
#     list5[1] = 'Chelsea'
#     list5[2] = 'Arsenal'
#     list5[3] = 'Liverpool'
#     list5[4] = 'Manchester City'
#     #Print the new values of the list
#     print("The new list is:", list5)
# meth10()
#
# print()

# #Print a list using the For loop. Print certain items in the list using the if-else condition
# def meth11():
#     list6 = ['Mercedes', 'BMW', 'Audi', 'Porsche', 'Volkswagen']
#     print('The original German Automobile Manufacturer list: ', list6)
#     print()
#     print('The selected German Automobile Manufacturers are: ')
#     for i in list6:
#         if i == list6[-2] or i == list6[4]:
#             continue
#         print(i)
# meth11()

# #Print the required items in the list
# #Determine if the values are displayed in the list or not
# def meth12():
#     list7 = ['Mississauga', 'Toronto', 'Vaughan', 'Brampton', 'Oshawa', 'Ajax', 'Pickering', 'Scarborough', 'Hamilton',
#              'Kitchener', 'Waterloo', 'Sarnia']
#     print("Toronto GTA:")
#     for i in list7:
#         print(i)
#     print()
#     user_input = input("Please enter an Ontario City from the above list: ")
#     if user_input in list7[0:4]:
#         print("The city is part of the Toronto GTA.")
#     elif user_input in list7[4:8]:
#         print("The city is Not a part of the Toronto GTA but is a close suburb of Toronto.")
#     elif user_input in list7[8::]:
#         print("This city is NOT part of Toronto but a major city in Ontario")
#     else:
#         print("Invalid String entered. Try again.")
# meth12()
#
# print()

# #Determine the length of the list
# def meth13():
#     list8 = ['Kobe Bryant', 'Lebron James', 'Jimmy Butler', 'Steph Curry', 'Luka Doncic', 'Kevin Durant',
#              9.5, 4.25, 7.88, 6.69, 2, 1.00, 13.42]
#     print(list8)
#     print()
#     print("Representing the items in the list individually: ")
#     for i in list8:
#         print(i)
#     print()
#     print("The length of the above list is: ",len(list8))
# meth13()
#
# print()

# #Adding items to the list - append() and insert()
# # append() will insert items into the last index position in the list
# # insert() will insert items into the desired index position in the list
# def meth14():
#     list9 = ['Mitsubishi', 'Mazda']
#     list10 = ['Porsche', 'Volkswagen']
#     print("The original Japanese Manufacturer list:", list9)
#     list9.append('Honda')
#     list9.append('Toyota')
#     print("The updated Japanese Manufacturer list: ", list9)
#     print()
#     print("The original German Manufacturer list:", list10)
#     list10.insert(1, 'BMW')
#     list10.insert(2, 'Mercedes')
#     print('The updated German Manufacturer list:', list10)
# meth14()
#
# print()

# #Create a method to Remove, Delete items in a list or Clear all items in a list
# # pop(), del, clear()
# def meth15():
#     list11 = ['New York City', 'Los Angeles', 'Seattle', 'Houston', 'Washington DC', 'Miami', 'Chicago',
#               'Toronto', 'Vancouver', 'Montreal', 'Ottawa']
#     print("The City list is:", list11)
#     print()
#     #Using the pop() function to remove an item from the list. Index position needs to be provided
#     list11.pop(9)
#     print("The 1st updated City list is:", list11)
#     print()
#     #Using the del keyword to delete an item from the list. Index  position needs to be provided
#     del list11[9]
#     print("The 2nd updated City list is:", list11)
#     print()
#     #Using the clear() function to empty the entire list
#     list11.clear()
#     print("The 3rd updated City list is:", list11)
# meth15()
#
# print()

# #Lists can also be duplicated and copied
# #Duplicating a list will use the list(nameofyourlist) and assign it a variable.
# #Copying of a list involves the use of copy() function
#
# #Create a method to duplicate and copy a list
# def meth16():
#     list12 = ['Stamford', 'Bridgeport', 'New Haven', 'Greenwich', 'Hartford']
#     print("Original Connecticut City List:", list12)
#     #Duplicate the list using the list(nameOfList) function.
#     list13 = list(list12)
#     print("Duplicated Connecticut City List:", list13)
#     print()
#     list14 = ['Tehran', 'Baghdad', 'Riyadh', 'Abu Dhabi', 'Doha', 'Dubai', 'Kuwait City', 'Muscat']
#     print("Original Gulf City List:", list14)
#     #Copy the List using the copy() function
#     list15 = list14.copy()
#     print("Copied Gulf City List:", list15)
# meth16()
#
# print()

# #Lists can be combined/joined/concatenated by using + operator OR For loop OR extend() function

# def meth17():
#     list16 = ["Ferrari", "Lamborghini", "Maserati", "Alfa Romeo"]
#     print("Italian Automobile Manufacturers:", list16)
#     list17 = ["Mclaren", "Volvo", "Koenigsegg", "Pagani"]
#     print("European Automobile Manufacturers:", list17)
#     print()
#     #Concatenation of 2 lists
#     print("European Automobile Manufacturers (Concatenation):", list16+list17)
#     print()
#     #Using the For loop to join 2 lists
#     for i in list16:
#         list17.append(i)
#     print("European Automobile Manufacturers (For loop):", list17)
#     print()
#     print("European Automobile Manufacturers (individual display):", list17)
#     #Displaying all the Manufacturers on separate lines
#     for i in list17:
#         print(i)
# meth17()
#
# print()

# #Concatenation of 2 lists using For loop and + operator - PRACTICE 1
# def meth18():
#     list18 = ["Bale", "Benzema", "Ronaldo"]
#     list19 = ["Neymar", "Suarez", "Messi"]
#     print('Real Madrid Attack:', list18)
#     print('Barcelona Attack:', list19)
#     print()
#     #Concatenation of the 2 lists using the + operator
#     print("La Liga Attack (+operator):", list18+list19)
#     print()
#     #Concatenation of the 2 lists using the For loop
#     for i in list18:
#         list19.append(i)
#     print("La Liga Attack (For loop):", list19)
#     print()
#     print("La Liga Attack (individual):")
#     #Print each name on individual lines using the For loop
#     for i in list19:
#         print(i)
# meth18()
#
# print()

# #Concatenation of 2 lists using For loop and + operator - PRACTICE 2
# def meth19():
#     list20 = ['Haaland', 'Foden', 'De Bruyne']
#     print("Manchester City Attack:", list20)
#     list21 = ['Salah', 'Nunez', 'Diaz']
#     print("Liverpool Attack:", list21)
#     print()
#     #Concatenation of the 2 lists using the + operator
#     print("English Premier League Attack (+ operator):", list20+list21)
#     print()
#     #Concatenation of the 2 lists using the For loop
#     for i in list20:
#         list21.append(i)
#     print("English Premier League Attack (For loop):", list21)
#     print()
#     print("English Premier League Attack (individual):")
#     #Display the list of attackers on individual lines
#     for i in list21:
#         print(i)
# meth19()
#
# print()

# #Create a method to concatenate 2 lists using the extend() function
# def meth20():
#     list22 = ['Samsung', 'Acer', 'Huawei', 'Sony']
#     print("Asian Electronic Companies:", list22)
#     list23 = ['Apple', 'Microsoft', 'Blackberry']
#     print("American Electronic Companies:", list23)
#     print()
#     #Making use of the extend() function to combine 2 lists
#     list22.extend(list23)
#     print("Combined Electronic Companies:", list22)
#     print()
#     #Print the names of each company individually
#     print("Electronic Companies (individual):")
#     for i in list22:
#         print(i)
# meth20()
#
# print()

# #Combination of 3 Lists using the extend() function
# def meth21():
#     list24 = ['Saka', 'Havertz', 'Martinelli']
#     list25 = ['Rashford', 'Fernandes', 'Garnacho']
#     list26 = ['Palmer', 'Jackson', 'Mudryk']
#     print("Arsenal Attack:", list24)
#     print("Manchester United Attack:", list25)
#     print("Chelsea Attack:", list26)
#     print()
#     #Making use of the extend() function to combine list25 and list26
#     list25.extend(list24)
#     print("The combination of List24 and List25:", list25)
#     print()
#     #Making use of the extend() function to combine (List24+List25) and List 26
#     list26.extend(list25)
#     print("The combination of (List24 + List25) and List26:", list26)
# meth21()
#
# print()

# #TUPLE
# #Tuple is represented with ().
# #Tuples are immutable
# #Tuple is ordered and unchangeable

# #Create a method to print a Tuple, access the items in a tuple and display the index ranges
# def meth22():
#     tuple1 = ('Dawson', 'Derrick', 'Dwayne', 'Dexter', 'Dominic', 'Dianne', 'Distin', 'Dickson', 'Doyle', 'Derina')
#     print("Tuple with 1st Name \"D\":", tuple1)
#     print()
#     print("Individual Names (starting D):")
#     for i in tuple1:
#         print(i)
#     print()
#     #Accessing the items in the Tuple
#     print("The 5th item in the Tuple is", tuple1[4])
#     print("The 3rd item in the Tuple is", tuple1[-8])
#     print()
#     #Display the index range of the Tuple using positive integers
#     print("Items 4 to 8 in the Tuple1 collection include:", tuple1[3:7])
#     print()
#     #Display the index range of the Tuple using negative integers
#     print("Items 2 to 5 in the Tuple1 collection include:", tuple1[-9:-5])
#     print()
#     #Display the index range of the Tuple from 6th item to the last item
#     print("Items 7 to 10 in the Tuple1 collection include:", tuple1[6::])
#     print()
#     print("Items 4 to 10 in the Tuple1 collection include:", tuple1[-7::])
# meth22()
#
# print()

# #To change the items in a Tuple is not possible. To achieve this we need to convert Tuple to a List.
# #We can then use append() or insert() functions to add items to the List.
# #We then change the List back to the Tuple
#
# #Create a method to add items to the Tuple
# def meth23():
#     tuple2 = ("Gordon", "Isak", "Almiron", "Joelinton", "Guimaraes", "Tonali")
#     print("Newcastle United Squad:", tuple2)
#     print()
#     print("Newcastle United Squad \"individual\":")
#     for i in tuple2:
#         print(i)
#     print()
#     #Convert the Tuple to a List
#     list27 = list(tuple2)
#     #Now the Tuple has been converted to a list. We can now append/insert into the List
#     list27.append("Burn")
#     list27.insert(3, "Schar")
#     list27.insert(4, "Trippier")
#     #Convert the List back to Tuple
#     tuple2 = tuple(list27)
#     print("Newcastle United Squad \"updated\":", tuple2)
#     print()
#     print("Newcastle United Squad \"individual-updated\":")
#     for i in tuple2:
#         print(i)
# meth23()
#
# print()

# #Create a method wherein only 5 items of the Tuple are printed
# def meth24():
#     tuple3 = ('Oslo', 'Stockholm', 'Helsinki', 'Copenhagen', 'Berlin', 'London', 'Dublin', 'Moscow')
#     print("Northern European Cities:", tuple3)
#     print()
#     print("Northern European Cities (individual):")
#     for i in tuple3:
#         print(i)
#     print()
#     print("Northern European Cities (5 names only - individual):")
#     #User does not want Berlin, London and Dublin to be printed
#     for i in tuple3:
#         if i == 'Berlin':
#             continue
#         elif i == 'London':
#             continue
#         elif i == tuple3[6]:
#             continue
#         print(i)
# meth24()
#
# print()

# #Create a method to check if item is present in the Tuple or not
# def meth25():
#     tuple4 = ("Argentina", "Brazil", "Colombia")
#     print("South American Country List:", tuple4)
#     print()
#     print("South American Country list:")
#     for i in tuple4:
#         print(i)
#     print()
#     #Prompt the User to enter a string
#     user_input1 = input("Enter the Country Name: ")
#     if user_input1 in tuple4:
#         print("Entered value", user_input1, "is a South American Country")
#     else:
#         print("Entered value", user_input1, "is NOT a South American Country")
#     # if user_input1 == "Argentina":
#     #     print("South American Country is present in the Tuple")
#     # elif user_input1 == "Brazil":
#     #     print("South American Country is present in the Tuple")
#     # elif user_input1 == tuple4[2]:
#     #     print("South American Country is present in the Tuple")
#     # else:
#     #     print("Country entered is invalid. Please retry!")
#     print()
#     #Print the length of the Tuple
#     print("The length of the Tuple is", len(tuple4))
# meth25()
#
# print()

# #Since a Tuple is immutable they cannot be copied.
# #Step 1 - We need to covert Tuple to List first by making use of list(nameoflist) function.
# #Step 2 - Once tuple is converted to list, we will copy the list and assign to a variable.
#
# #Create a method to showcase how a tuple can be copied
# def meth26():
#     tuple5 = ('Egypt', 'Morocco', 'Nigeria', 'Ivory Coast', 'Cameroon')
#     print("African Football Countries (1):", tuple5)
#     #Convert the Tuple to list
#     list27 = list(tuple5)
#     print("African Football Countries (2):", list27)
#     test = list27.copy()
#     print("African Football Countries (3):", test)
# meth26()
#
# print()

# #Create another method to showcase how a tuple can be copied
# def meth27():
#     tuple6 = ('Japan', 'Qatar', 'Saudi Arabia', 'Oman', 'India')
#     print('Asian Football Countries (1):', tuple6)
#     print()
#     #Copy the Tuple
#     tuple7 = tuple6
#     print("Asian Football Countries (2):", tuple7)
# meth27()
#
# print()

#Tuples can be deleted

# #Create a method to delete a Tuple
# def meth28():
#     tuple8 = ('Squirtle', 'Polywag', 'Staryu', 'Psyduck', 'Magikarp')
#     print("The Pokemon tuple list:", tuple8)
#     print()
#     for i in tuple8:
#         print(i)
#     print()
#     #Delete the tuple using the del keyword
#     del tuple8
# meth28()
#
# print()

# #We cannot use the append(), insert() and extend() functions on a Tuple
# #However, concatenation of Tuples can be done
# def meth29():
#     tuple9 = ('Amazon', 'Nile', 'Indus', 'Ganga', 'Hudson')
#     print(tuple9)
#     tuple10 = (1, 2, 3, 4, 5)
#     print(tuple10)
#     tuple11 = tuple10 + tuple9
#     print(tuple11)
# meth29()
#
# print()

# #Create a method to combine 2 tuples using the For loop
# def meth30():
#     tuple12 = (1.1, 1.2, 1.3, 1.4, 1.5)
#     tuple13 = ('Alkane', 'Alkene', 'Alkyne', 'Hydrocarbons', 'Acids')
#     print(tuple12)
#     print(tuple13)
#     print()
#     list28 = list(tuple12)
#     list29 = list(tuple13)
#     print(list28)
#     print(list29)
#     print()
#     for i in list28:
#         list29.append(i)
#     tuple14 = tuple(list29)
#     print(tuple14)
# meth30()
#
# print()

# #SET
# #Sets are represented by {}.
# #A Set is mutable.
# #A Set is unordered and unindexed (values displayed in set will be printed in random order)
#
# #Create a method to print a Set and access the items in the Set
# def meth31():
#     set1 = {'Undertaker', 'Kane', 'Big Show'}
#     print("WWE Superstars:", set1)
#     print()
#     for i in set1:
#         print(i)
# meth31()
#
# print()

#Create a method to check if the item exists in the Set or not
# def meth32():
#     set2 = {'Spyder', 'Huracan', 'SLS AMG', 'GTR', 'Enzo', 'Agera'}
#     print("Supercar models:", set2)
#     print()
#     for i in set2:
#         print(i)
#     print()
#     if 'Spyder' or 'Huracan' or 'SLS AMG' or 'GTR' or 'Enzo' or 'Agera' in set2:
#         print("Supercar model type exists")
#     else:
#         print("Supercar model DOES NOT exist!")
# meth32()
#
# print()

# #Create a method asking the User to enter an input and check if entered input is in the Set or not
# def meth33():
#     set3 = {7.31, 6.46, 3.19, 2.81, 1.06, 4.96, 5.77}
#     print(set3)
#     print()
#     for i in set3:
#         print(i)
#     print()
#     user_input3 = input("Enter a decimal value (upto 2 places):")
#     print()
#     if user_input3 in set3:
#         print("The decimal value entered is in the Set.")
#     elif user_input3 == 0.0:
#         print("Please enter a value greater than 0.")
#     elif user_input3 not in set3:
#         print("The decimal value entered is NOT in the Set.")
# meth33()
#
# print()

#Adding items to the Set - add(), update([])
# add() function will add single items to the set
# update([]) function will add multiple items to the set
#update() can also be used to combine 2 sets
# union() function is used to combine 2 sets
#For Lists, we have made use of append() and insert()

# #Create a method to add items to the Set and determine the length of the Set
# def meth34():
#     set4 = {'Bale', 'Parker', 'Berbatov', 'Son', 'Lamela', 'Dembele'}
#     print("Tottenham Hotspur:", set4)
#     print()
#     for i in set4:
#         print(i)
#     print()
#     #Add single item to the set
#     set4.add('Assou-Ekotto')
#     print("Tottenham Hotspur (updated-1):", set4)
#     print()
#     #Add multiple items to the set using update() function
#     set4.update(['Lennon', 'Walker'])
#     print("Tottenham Hotspur: (updated-2):", set4)
#     print()
#     for i in set4:
#         print(i)
#     print()
#     print("The length of \"Set4\" is", len(set4))
# meth34()
#
# print()

# def meth37():
#     set10 = {'Auckland', 'Wellington', 'Christchurch', 'Hamilton', 'Invercargill'}
#     set11 = {'Perth', 'Sydney', 'Melbourne', 'Hobart', 'Brisbane'}
#     print("New Zealand:", set10)
#     print()
#     for i in set10:
#         print(i)
#     print()
#     print("Australia:", set11)
#     print()
#     for i in set11:
#         print(i)
#     print()
#     #Combine both sets using update()
#     set11.update(set10)
#     print("Australia & New Zealand:", set11)
#     print()
#     for i in set11:
#         print(i)
#     print()
#     print("The length of the Set is", len(set11))
# meth37()
#
# print()

# #Create a method to combine 2 Sets using the union() function
# def meth36():
#     set7 = {'Dollar','Euro', 'Ruble', 'Pesos'}
#     set8 = {'Yuan', 'Yen', 'Rupee', 'Dirham', 'Dinhar'}
#     print("World Currencies (America & Europe):", set7)
#     print()
#     for i in set7:
#         print(i)
#     print()
#     print("World Currencies (Asia):", set8)
#     for i in set8:
#         print(i)
#     print()
#     #Combining the 2 Sets using union() function.
#     set9 = set7.union(set8)
#     print("World Currencies (World):", set9)
#     print()
#     for i in set9:
#         print(i)
# meth36()

#Items can be removed from the set using the following: remove(), discard()
#For Lists, we can make use of also: pop(), del, clear()

#clear() removes all the items from the list and set. Tuple is immutable
#del keyword deletes the set permanently
#pop() removes the required item in the List or Set
#remove() and discard() both remove the required items in the List or Set
#remove() throws an error to remove a non-existing item. However discard() does not throw any error

# #Create a method to remove and discard items from the Set
# def meth35():
#     set5 = {'Belial', 'Judus', 'Lucifer', 'Kane'}
#     print("Devils Set:", set5)
#     print()
#     for i in set5:
#         print(i)
#     print()
#     #Remove an item from the Set using the remove() function
#     set5.remove('Kane')
#     print("Devils Set (updated-I):", set5)
#     print()
#     #Using the remove() function for the same item throws an error in the console
#     # set5.remove('Kane')
#     #Remove an item from the Set using the discard() function
#     set5.discard('Judus')
#     print("Devils Set (updated-II):", set5)
# meth35()
#
# print()

# #DICTIONARY
# #Dictionary is also represented by {}
# #Dictionary is mutable/changeable
# #Dictionary is unordered and indexed
# #Items in the Dictionary can be accessed using the key
# #To access the items in Dictionary, we use the key and NOT the index number. get() function can also be used
#
# #Create a method to display a dictionary, length and access the items in the dictionary
# def meth38():
#     dict1 = {1001:'London', 1002:'Liverpool', 1003:'Newcastle', 1004:'Brighton', 1005:'Manchester'}
#     print("England:", dict1)
#     print()
#     #Accessing the items in the dictionary
#     for key,value in dict1.items():
#         print("ID:", key, "City:", value)
#     print()
#     print("The length of the Dictionary \"dict1\" is", len(dict1))
#     print()
#     print("City situated on the southern coast of England is", dict1[1004])
#     print()
#     print("The capital of England is", dict1.get(1001))
# meth38()
#
# print()

# #Create a method to display a dictionary, length and access the items in the dictionary - PRACTICE 2
# def meth39():
#     dict2 = {1011: 'Alpha', 1012: 'Zulu', 1013: 'Beta', 1014: 'Gamma', 1015: 'Omega', 1016: 'Phi'}
#     print("Codes:", dict2)
#     print()
#     for key,value in dict2.items():
#         print("ID:", key, "Code:", value)
#     print()
#     #Accessing a particular item in the dictionary using get()
#     print("The launch code initiation is:", dict2.get(1011))
#     print()
#     #We can access the items by just using the key value
#     print("The launch code confirmation is:", dict2[1016])
#     print()
#     #Determine the length of the Dictionary
#     print("The length of the Dictionary \"dict2\":", len(dict2))
# meth39()

# #Create a method to print only the keys and only the values and keys & values - PRACTICE-1
# def meth40():
#     dict3 = {2001:'Berlin', 2002:'Munich', 2003:'Dortmund', 2004:'Leverkusen', 2005:'Mainz'}
#     print("Germany:", dict3)
#     print()
#     #Display ony the key
#     for i in dict3:
#         print(i)
#     print()
#     #Display only the value
#     for i in dict3:
#         print(dict3[i])
#     print()
#     #Display the key and value
#     for key,value in dict3.items():
#         print(key, value)
# meth40()
#
# print()

#enumerate() is a built in python function that increments by 1 and needs a start value
#The syntax for enumerate() is "enumerate(iterable, start=0)" where iterable is the list, tuple, dictionary or string
#If the "start=1" is not provided then default value is 0
#Keeps track of both the index and the value of each element in the iterable. It adds a counter to the iteration process.

#The f"", formatted string literals
# Allows you to include variables, expressions, or function calls directly into your string without needing concatenation or additional formatting methods.


# #Create a method to access the keys, values, keys & values of a dictionary collection - PRACTICE-2
# def meth41():
#     dict4 = {'Ancilla': 378, 'Jaden': 291, 'Dwayne': 794}
#     print("Students:", dict4)
#     print()
#     #Display the keys from the dictionary collection
#     for i in dict4:
#         print(i)
#     print()
#     #Display the values from the dictionary collection
#     for i in dict4:
#         print(dict4[i])
#     print()
#     #Display the serial number with the keys and values using enumerate()
#     for index,(key,value) in enumerate(dict4.items(), start=1):
#         print(f"{index}. {key}: {value}")
# meth41()
#
# print()
#
# #Create a method to access the keys, values, keys & values of a dictionary collection - PRACTICE-3
# def meth42():
#     dict5 = {1110:'DesertStorm', 1111:'Blitzkrieg', 1112:'Geronimo'}
#     print("War Operations:", dict5)
#     print()
#     #Print the Keys
#     for i in dict5:
#         print(i)
#     print()
#     #Print the Values
#     for i in dict5:
#         print(dict5[i])
#     print()
#     #PDisplay the serial number with the keys and values
#     counter = 1
#     for key,value in dict5.items():
#         print(f"{counter}. {key}: {value}")
#         #Increment the serial number by 1 after printing every item
#         counter += 1
# meth42()

# #Create a method to access the keys, values, keys & values of a dictionary collection - PRACTICE-4
# def meth43():
#     dict6 = {2021:'Honda', 2022:'Civic', 2023:'Hatchback', 2024:'Compact Sedan', 2025:35000}
#     print("Automobile Details:")
#     print(dict6)
#     print()
#     print("Automobile Specs 1:")
#     #Display the Keys of the Dictionary collection
#     for i in dict6:
#         print(i)
#     print()
#     print("Automobile Specs 2:")
#     #Display the Values of the Dictionary collection
#     for i in dict6:
#         print(dict6[i])
#     print()
#     print("Automobile Specs 3:")
#     #Display the Keys and Values of the Dictionary collection
#     for x,y in dict6.items():
#         print(x,y)
#     print()
#     print("Automobile Specs 4:")
#     #Display the Keys and Values along with the Serial number incremented using enumerate() function
#     for serial,(x,y) in enumerate(dict6.items(), start=1):
#         print(f"{serial}. {x}: {y}")
#     print()
#     print("Automobile Specs 5:")
#     #Display the Keys and Values along with the Serial number incremented without using Python inbuilt functions
#     sr_no=1
#     for x,y in dict6.items():
#         print(f"{sr_no}. {x}: {y}")
#         sr_no+=1
# meth43()
#
# print()

# #Create a method to access the keys, values, keys & values of a dictionary collection - PRACTICE-4
# #Ask the User to input a value and system to determine if the value entered is part of the dictionary or not
# def meth44():
#     dict7 = {1021:'Budweiser', 1022:'StellaArtois', 1023:'Guinness', 1024:'CoorsLight', 1025:'BudLight', 1026:'Corona'}
#     print("Beer Manufacturers-I:", dict7)
#     print()
#     print("Beer Manufacturers-II:")
#     # Display the Keys
#     for i in dict7:
#         print(i)
#     print()
#     print("Beer Manufacturers-III:")
#     #Display the Values
#     for i in dict7:
#         print(dict7[i])
#     print()
#     print("Beer Manufacturers-IV:")
#     #Display the Keys and Values
#     for x,y in dict7.items():
#         print(x,y)
#     print()
#     print("Beer Manufacturers-V:")
#     #Display the Keys and Values with incrementing serial numbers using enumerate()
#     for sr_no1,(x,y) in enumerate(dict7.items(), start=1):
#         print(f"{sr_no1}. {x}: {y}")
#     print()
#     print("Beer Manufacturers-VI:")
#     #Display the Keys and Values using a variable to counter increase the serial number by 1
#     sr_no2=1
#     for x,y in dict7.items():
#         print(f"{sr_no2}. {x}: {y}")
#         sr_no2+=1
#     print()
#     #The "while True" statement will ensure the statement is constantly prompted till a valid input is entered
#     while True:
#         user_input3 = input("Please enter the Name of the Beer Manufacturer:")
#         print()
#         #If the string entered is an alphabet
#         if user_input3.isalpha():
#             #If the string is present in the dictionary values
#             if user_input3 in dict7.values():
#                 print(f"The Beer Manufacturer \"{user_input3}\" is registered with the State of Ontario.")
#                 break
#             else:
#                 print(f"The Beer Manufacturer \"{user_input3}\" is NOT registered with the State of Ontario.")
#                 break
#         #If the string entered is an integer
#         elif user_input3.isdigit():
#             print(f"Entered input \"{user_input3}\" is an \"Integer\". Please enter name of the Beer Manufacturer again.")
#             continue
#         #If the string entered is a special character i.e. not an integer or alphabet
#         elif not user_input3.isalnum():
#             print(f"Entered input \"{user_input3}\" is a \"Special Character\". Please enter name of the Beer Manufacturer again.")
#         #If the string entered is blank
#         elif user_input3.isspace():
#             print(f"Entered input \"{user_input3}\" is \"blank\". Please enter name of the Beer Manufacturer again.")
#             continue
#         #If any other type of input is entered
#         else:
#             print(f"Entered input is Invalid. Please try again")
#             continue
# meth44()
#
# print()

# #Create a method to access the keys, values, keys & values of a dictionary collection - PRACTICE-5
# def meth45():
#     dict8 = {1501:'Javascript', 1502:'Java', 1503:'Python', 1504:'C', 1505:'PHP'}
#     print("Programming Languages Dictionary-I:", dict8)
#     print()
#     # Display only the Keys
#     print("Programming Languages-II:")
#     sr_no1 = 1
#     for i in dict8:
#         print(f"{sr_no1}. {i}")
#         sr_no1 += 1
#     print()
#     #Display only the Values
#     print("Programming Languages-III:")
#     sr_no2 = 1
#     for i in dict8:
#         print(f"{sr_no2}. {dict8[i]}")
#         sr_no2 += 1
#     print()
#     #Display the Keys and Values of the Dictionary with incrementing serial number
#     print("Programming Languages-IV:")
#     sr_no3 = 1
#     for x,y in dict8.items():
#         print(f"{sr_no3}. {x}: {y}")
#         sr_no3 += 1
#     print()
#     #Display the Keys and Values of the Dictionary using enumerate(iterable, start=0)
#     print("Programming Languages-V:")
#     for sr_no4,(x,y) in enumerate(dict8.items(), start=1):
#         print(f"{sr_no4}. {x}: {y}")
#     print()
#     #Determine whether the User entered Programming Language is offered as a course in University or not
#     #Using the while true to keep the loop running as long as a valid input is provided
#     while True:
#         user_input4 = input("Please enter the Programming Language: ")
#         print()
#         if user_input4.isalpha():
#             if user_input4 in dict8.values():
#                 print(f"The Programming Language \"{user_input4}\" is a course offered at this University.")
#                 break
#             else:
#                 print(f"The Programming Language \"{user_input4}\" is NOT a course offered at this University.")
#                 break
#         elif user_input4.isdigit():
#             print(f"The Programming Language \"{user_input4}\" is entered with integers. Please enter a valid input.")
#             continue
#         elif not user_input4.isalphanum():
#             print(f"The Programming Language \"{user_input4}\" is entered with special characters. Please enter a valid input.")
#             continue
#         else:
#             print("Please enter a Computer Programming Language to check if the course is being offered.")
#             continue
#     print()
#     #Access a record from the dictionary using index number & get() function
#     print("The 3rd item in the Dictionary is", dict8.get(1503))
#     print()
#     print("The 5th item in the Dictionary is", dict8[1505])
#     print()
#     #Delete an item from the dictionary - pop(), del, remove(), discard()
#     dict8.pop(1505)
#     print("The updated dictionary:", dict8)
# meth45()
#
# print()


