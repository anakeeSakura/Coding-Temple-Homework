# '''Special Characters'''

# print("Hello,\nWorld!")
# print("Hello,\tWorld!")
# print("This is a backslash:  \\")
# print('She said, \'Hello!\'')
# print("He replied, \"Hi there!\"")

# ''' String Concatenation: Crafting Messages with Care'''

# greeting = "Hello"
# name  = "John"
# print(greeting + ", " + name + "!")  

# age = 30
# print(name + " is " + str(age) + " years old.")  

# '''Customizing messages'''

# print("apple",  "banana", "cherry", sep="---")

# print("This is just the beginning...",  end="")
# print(" and here's the continuation.")
# print("apple",  "banana", "cherry", sep="-", end="...yum!\n")


# '''String Formatting: A More Elegant Approach'''

# name = "Sakura"
# print("Her name is %s." % name) # %s is a  placeholder for a string

# age  = 39
# print("she is {} years old.".format(age)) #.format is acting  as a placeholder for a value

# hobby = "Playing LOL"
# print(f"Sakura loves {hobby}.") # f string allows a variable to  be embedded inside a string


# pi = 3.14
# print(f"The value of PI to 3 decimal places is {pi:.3f}.")  
# # taking the variable pi and .3f allows us to use the first 3 decimal places after it.

# # Tips for message Mastery
# '''Commas for space: Separate items with commas in print(), and Python will add spaces. 
# New lines with\\n: Use\\n for new lines. 
# Dynamic Messages: Mix variables and strings
# in print() for messages that adapt and resonate. '''

# '''
# How Does input () work'''
# # input() is a function that allows users to input data into a program.
# # It returns a string value of what the user entered.
# # Always returns a  string, even if the user enters a number.You'll need to  convert it to the correct type if needed.



# name  = input("What is your name? ")
# print(f"Hello, {name}!")  # prints out the user's name

# age = input("How old are you?") #alway returns a  string

# age = int(age)
# print(f"Next year, you'll be  {age + 1} years old.") 

# answer =  input("Do you like Python? (yes/no) ")
# if answer ==  "yes":
#     print("That's awesome!")
# else:
#     print("oh, why  not?")


# '''Recapp on integer,  float, and string'''
# # Integers: whole numbers, no decimal points
# # Floats: numbers with decimal points
# # Strings: text, enclosed in quotes
# # Strings can be enclosed in single quotes or double quotes. Both are acceptable.
# # Strings can be enclosed in triple quotes for multi-line strings. ''' '''
# # Strings can be concatenated (combined) using the + operator.
# # Strings can be repeated using the * operator.
# # Strings can be formatted using the format() method or f-strings. '''
# # Integers and floats can be converted to strings using the str() function.

# # The Number Wizard
# number_string = "123"
# number = int(number_string)

# # The Floating Enchanter
# decimal_string  = "3.14"
# pi = float(decimal_string)

# # The workd weaver
# age = 25
# age_string = str(age)

# # The Truth Seeker
# is_empty = bool("")

# # Casting the spells 
# print(number + 1)
# print(pi  * 2)
# print("I am"  + age_string + "years old")  # prints out "I am 25 years old"
# print(is_empty)

# # The cast of characters
# mystery_variable = "Sherlock"
# clue_list = ["candlestick," "footprint", "handerkercheir"]
# alleged_title  = "I am a duke"
# # The detective
# print("Type of mystery_variable:" , type(mystery_variable))
# print("Number of clues found:", len(clue_list))
# print("Is the title genuine?", isinstance(alleged_title, str)) 

# '''Python's Number Types
# abs(): The Beacon of positivity: Go-to for finding the absolute value, 
# round(): The numberical Shepherd: Guiding numbers to their neares whole value
# sub(): The Generous Collector: Gives us the total
# min() and max (): The judges of Extremes: Bring the smallest and largest numbers. 
# pow(): The Muscle Builder: When numbers need to buld up
# divmod(): The Fair Divider: A fair division and what's left over 

# Math Module:

# sqrt(): The square Root sage: Numbers roots
# ceil() and floor(): The Precision Twins: handle decimals. Ensure numbers fall just where we want them. 
# exp() and log(): The exponential Elevator and Logarithmic Lens: For exponential growth or to peer into logarithmic patterns.
# sin(), cos(), tan(): The trigonomety trio: Trigonometryu operations related. 
# radians() and degress(): The Angle Translators:Converting degrees and radians to keep code consistency. '''



# import math

# scores = [1, 5, 10, 8, 4, 2]

# print(abs(-2023), round(3.14159, 2), sum([1, 2, 3, 4, 5]))
# print(min(scores), max(scores), pow(2, 3), divmod(10, 30))

# # Math module is only accesible by  importing math
# print(math.sqrt(16), math.ceil(2.1), math.floor(2.9))
# print(math.exp(1), math.log(10))

# angle = 10
# print(math.sin(angle), math.cos(angle), math.tan(angle))
# print(math.radians(180), math.degrees(math.pi))


# ''' 
# Exercise 1. 
# The username Validator wirte a program that checks if a username is neither too short nor too long, adhering to specific
# length criteria. 

# 1. Prompt the user to enter a username. 
# 2. check if the username is between 5 and 15 characters long. 
# 3. If the username meets the criteria,  print a confirmation message. 
# 4. If it does not meet the criteria, print a message indicating the username length requirements.
# 5. Provide the user with the opetion to try a different username or exit the program.
# '''
# while True:
#     username  = input("Please enter a username: ")
#     if 5 <= len(username) <= 15:
#         print("Username is valid")
#     else:
#         print("Username is too short or too long. It should be between 5 and 15")   
#     continue_input = input("Do you want to try another username? (yes/no)").lower()
#     if continue_input !=  'yes':
#         break

# '''
# Exercise 2. The Precise Price Tagger
# Task is to write a program that takes a price as input and rounds it to two decimal places, making it more user-friendly. 

# 1. Prompt the user to enter a price.
# 2. Use the 'round()' function to round the price to two decimal places. 
# 3. Display the round price in a format that is easy for customers to understand.
# 4. Provide the user with the option to enter a new price or exit the program. 
# '''

# while True:
#     price_input  = float(input("Please enter a price: "))
#     rounded_price = round(price_input, 2)
#     print(f"Your price is: ${rounded_price}")

#     new_price  = input("Do you want to enter a new price? (yes/no) ").lower() # .lower() allows user to enter a lower case  or upper case. 
#     if new_price !=  'yes':
#         break


# ''' 
# Task create a feature for a travel app that allows users to view the temperature in both Celsious and  Fahrenheit. 
# 1. Create a list of temperatures in Celsius that you want to convert. 
# 2. Loop through the list, and fo reach temperature in Celsius, convert int to fahrenheit. 
# 3. Print out both the celsius and fahrenheit temperature using f-strings for formated output. 
# '''

# celsius_temperatures  = [10, 20, 30, 40, 50,]

# for celsius in celsius_temperatures:
#     fahrenheit = (celsius * 9/5) + 32
#     print(f"{celsius}°C is equal to {fahrenheit}°F")

# '''
# Exercise 3 
# Goldilocks wants to find the warmest and coolest rooms in her house based on teh current  temperature readings.
# She has a list of temperature for each room and needs a quick way to determine which rooms are the warmest and coolest. 

# 1.  Create a list of temperatures for each room in the house. 
# 2. Detremine the warmest and coolest temperatures using the the  max() and min() functions. 
# 3. Identify the rooms with these temperature and print out the  results using string formatting. 
# '''
# room_temperatures =  [22, 18, 25, 12]
# room_names = ['living room', 'kitchen', 'bedroom', 'bathroom']

# warmest_temp = max(room_temperatures)
# coolest_temp = min(room_temperatures)

# warmest_room_index = room_temperatures.index(warmest_temp)
# coolest_room_index = room_temperatures.index(coolest_temp)

# warmest_room = room_names[warmest_room_index]
# coolest_room = room_names[coolest_room_index]

# print(f"The {warmest_room} is the warmest with {warmest_temp}c")
# print(f"The {coolest_room} is the coolest with {coolest_temp}c")

# '''
# Exercise 5. 
# The E-commerce cart task write a Python script that uses a string concatenation to create a summary of the items in a shopping
# cart, including product names, 
# prices, and stock availability. 

# 1. Define variable sfor a few products, their prices, and their stock availability. 
# 2 Use string concatenation to build a summary of the cart. 
# 3. Include product names, prices, and stock status (In stock or Out of Stock) in the summary.
# 4. Display the car cummary to the user. 
# '''
# #products
# product_1  = "Apple Watch"
# product_2 = "Samsung TV"
# product_3 = "Sony Headphones"

# #prices
# price_1 = "300"  
# price_2 = "1000"
# price_3 = "200"

# #stock availability
# stock_1 = True
# stock_2 = False
# stock_3 = True

# cart_summary = "Your Cart Items:\n"
# cart_summary  += "- " +  product_1 + ":" + price_1 + ("(In Stock)" if stock_1 else  " (Out of Stock)") + "\n"
# cart_summary  += "- " +  product_2 + ":" + price_2 + ("(In Stock)" if stock_2 else  " (Out of Stock)") + "\n"
# cart_summary  += "- " +  product_3 + ":" + price_3 + ("(In Stock)" if stock_3 else  " (Out of Stock)") + "\n"

# '''
# Exercise 6.
# The Interactive Story
# Task is to write a Python script that guides the reader throught the first decision point of the story.

# 1. Present the reader with a brief introductio to the story and a choice to make. 
# 2. Capture the reader's choice using the 'input()' function. 
# 3. Depending on the choice, displayu the outcojme their decision. 
# 4. Us a list to store possible choices and outcomes.
# '''
# print("You wake up in a  mysterious forest. Two paths lie before you.")

# choices  = ['left', 'right']
# outcomes  = ["You encounter a friendly elf who offer you a map.", "You stumble upon a sleeping dragon" ]

# print(f"Do you go left or right? (Type 'left' or 'right')")
# decision = input().lower()
                                                     
# if decision not in choices:
#     print("Confused, you decide to wait for a clearer sign of which path to take.")
# elif decision == 'left':
#     outcome_index = choices.index('left')
#     print(outcome_index)
#     print(outcomes[outcome_index])
# else:
#     outcome_index = choices.index('right')
#     print(outcomes[outcome_index])


# '''
# Exercise 7 The Customized list Printer
# Task is to create a program that prints out a shopping list. 
# However, the user wants the list to be printed in a specific format, with custom seperatgors between items and a custom ending 
# to signify the end of the  list.

# 1. Create a list of shopping items.
# 2. Ask the user for their preferred separator (e.g., comma, slash, dash).
# 3. Ask the user preferred ending phrase (e.g., "End of list", "That's all!").
# 4. Use a loop to print each item with the user's preferred separator and end the list with their chosen ending phrase.

# '''

# shopping_list =  ["Milk", "Bread", "Eggs", "Chicken", "apples"]
# seperator = input("Please enter your preferred item separator (e.g., ',', '/', '-'): ")
# ending = input("please enter your preferred ending phrase (e.g., 'End of list', 'That's all!'):")

# print("Your shopping list: ", end="\\n\n")
# for item in shopping_list:
#     print(item, end=seperator +  " ")
# print("\n\n" + ending)

# '''
# Exercise 8:
# The Dynamic Type quiz game
# 1. Create separate lists for questions, correct answers, and the required answer types.
# 2. Use a loop to iterate over the questions and present them to the user one by one. 
# 3. For each question, prompt the user fo rtheir answer and convert it to the required type using th ecorresponding type conversion function. 
# 4. Compare the user's converteed answer to the correc answer and provide immediate feedback.
# 5. keep a count fo the number of correct answers and display the user's score at the enf of the game. 
# '''
# questions = ["What is 10 plus 4?",
#              "Enter a decimal number between 1 and 2",
#              "What is the string representation of the number 20?",
#              "Is Python a programing Language? (True/False)"]
# correct_answers = [14, 1.5, "20", True]
# answer_types = [int, float, str, bool]

# score = 0
# for i in range(len(questions)):
#     user_answer = input(questions[i] + ": ")
#     try:
#         if answer_types[i] == bool:
#             converted_answer = user_answer.lower() in ['true', 't', '1', 'yes',  'y']
#         else:
#             converted_answer = answer_types[i](user_answer)
#         if converted_answer  == correct_answers[i]:
#             print("Correct!")
#             score += 1
#         else:
#             print("Wrong answer.")
#     except ValueError:
#         print("Invalid input type.")
# print(f"Your final score is {score}/{len(questions)}.")

# '''
# Exercise 9
# They Type Inspection Challange

# Create a program that categorizes elements in a list based on their data type.
# The Program should iterate over a mixed-type list, identify the data type of each element, and sort the elements into
# separate lists according to their type.

# 1. Create a mixed-typ list with various data types (e.g., integers, floats, strings, booleans).
# 2. Initialize separate lists to hold elements of each data types.
# 3. Use a loop to interate over the mixed-type list. 
# 4. For each element, use 'isinstance()' or 'type()' to determine the elemnt's type. 
# 5. Append the elemtn to the corresponding list based on its type.
# 6. Use shorthand 'if' statemetn to stremline the type-checking logic.
# 7. Print out the catergoraized lists after processing the entire mixed-type list.

# '''

# mixed_list = [10, 3.14, 'Python', False, 42, 'Code', 2.718, True]

# integers = []
# floats = []
# strings = []
# booleans = []

# for element in mixed_list:
#     if isinstance(element, int) and not isinstance(element, bool):
#         integers.append(element)
#     elif isinstance(element, float):
#         floats.append(element)
#     elif isinstance(element, str):
#         strings.append(element)
#     elif isinstance(element, bool):
#         booleans.append(element)
#     else:
#         print(f"Unknown type: {type(element)}")

# print(f"Integers: {integers}")
# print(f"Floats: {floats}")
# print(f"Strings: {strings}")
# print(f"booleans: {booleans}")

# '''
# Exercise 10. The Math Function Marathon
# A data analysis project that requires you to process a list of floating-point numbers.
# Task is to calculat the sum of all number, find the square root of each number, and then round them up or down to the nearest
# integer.
# Addtionallyu, you need to identify which nuymbers are above the average after rounding.

# 1. Create a list of floating-point numbers.
# 2.  Calculate the sum of the numbers using trhe 'sum()' function and print the result.
# 3. Use a loop to iterate over each number in the list. 
# 4. Inside the loop, calculate the square root of each number using the 'sqrt()

# '''

# import math

# numbers  = [2.5, 3.6, 4.7, 5.8, 6.9]

# total_sum = sum(numbers)
# print(f"The sum of the numbers is:  {total_sum}")

# average = total_sum / len(numbers)
# print(f"The average is:  {average}")


# for number in  numbers:
#     sqrt_number = math.sqrt(number)
#     rounded_number = round(sqrt_number)
#     if  rounded_number < sqrt_number:
#         rounded_number = math.ceil(sqrt_number)
#     else:
#         rounded_number = math.floor(sqrt_number)
#     if rounded_number > average:
#         print(f"{rounded_number} is above the average")
#     else:
#         print(f"{rounded_number} is below the average")


# '''
# Defining your First function
# '''
# def greet_user():
#     print("Hello, user!")

# greet_user()

# '''
# adding Parameters to a  function


# '''
# def cook_pasta(sauce_type):
#     print(f"Adding {sauce_type} to the pasta...")

# cook_pasta("marinara")
# cook_pasta("pesto")
# cook_pasta("Alfredo")
# cook_pasta("BaDek")


# '''
# Multiple Parameters
# '''
# def cook_pasta(sauce_type, second_parameter="none"):
#     print(f"Adding {sauce_type} to the pasta...")
#     print(f"Adding {second_parameter} to the pasta...")
# cook_pasta("marinara")
# cook_pasta("pesto")
# cook_pasta("Alfredo")
# cook_pasta("BaDek")

# cook_pasta("firstParmeter", "secondParameter")


# def make_sandwich(bread_type, filling):
#     print(f"Making a {filling} sandwich with {bread_type} bread...")
#     make_sandwich("white", "turkey")


# '''Default  Parameter Values'''

# def brew_coffee(size= "medium"):
#     print(f"Brewing a {size} cup of coffee...")
#     brew_coffee()   # This will print:Brewing a medium cup of coffee...
#     brew_coffee("large")  # This will print: Brewing a large cup of coffee


# ''' Passing a lists to Python Functions'''

# def prepare_snacks(snack_list):
#     for snack in snack_list:
#         print(f"Preparing {snack}...Done!")
    
# # List of snack for movie night
# movie_snacks =  ['popcorn', 'chips', 'candy',  'cookies']

# # Call the function with the list
# prepare_snacks(movie_snacks)
# # Output: Preparing popcorn...Done! Preparing chips...Done! Preparing candy...Done

# '''
# The Magic of *args 
# '''
# # *args allow  you to pass a variable number of arguments to a function

# def make_ice_cream(*flavors):
#     print(flavors)
#     for flavor in  flavors:
#         print(f"Scooping {flavor} ice cream!")
# make_ice_cream("vanilla",  "chocolate", "strawberry")

# '''The power of  **kwargs '''
# # **kwargs allow you to pass a variable number of keyword arguments to a function

# def make_sandwich(**ingredients):
#     for item, quantity in ingredients.items():
#         print(f"Adding{quantity} of {item} to the sandwich.")
# make_sandwich(tomatoes=" 3 slices", lettuce= " 2 leaves", mayo= " 1 spread")


# '''
# Return values  from functions. '''
# # Return values can be any data type, including strings, integers, floats, lists, dictionaries, 
# # and even other functions.

# def add_numbers(a,b):
#     test = a + b
#     return test 

# add_numbers(1,2)


# '''
# Catching the return value
# '''

# def add_number(a,b):
#     return  a + b
# # return 8
# # add_numbers(5,3) ==> return 8
# # result = 8
# # print (8)

# result = add_number(5,3)
# print(result) # Output: 8


# '''
# Multiple Returns

# '''
# def check_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False
    
#     result = check_even(5)
#     print(result) # Output: False

# '''
# Returning multiple values 
# in the form of a Tuple
# '''
# def get_details():
#     name  = "John"
#     age = 25
#     return name, age, "Male"


# person_name, person_age,  person_gender = get_details()

# print(person_name, person_age, person_gender)

# '''
# local scope is  the area where the variable is defined 
# global scope is the area where the variable is not defined
# '''
# def greet():
#     message =  "Hello, World!" # local scope
#     print(message)


# '''
# Global keyword
# '''
# counter = 0
# def  increment():
#     global counter # access the global variable
#     counter += 1 


# '''
# A single Python
# Using pass in Action video
# '''

# def calculate_interest():
#     pass # TODO: Implement interest calculatoin

# def upcoming_feature():
#     pass # Placeholder for a future  feature

# def unfinished_logic():
#     pass # Stub for incomplete logic

# # Using the functions
# calculate_interest()
# upcoming_feature()
# unfinished_logic()


# '''
# Hands on coding
# Ex. 1: The smart home morning routine
# task design a smart home system to perform a series of actions as part of a morning routine.
# The system should greet you, inform you of the weather, remind you of your first calendar event, and tell you if you have unread emails.

# Instructions
# 1. Define a function called 'morning_routine()' that take no arguments.
# 2. Inside the function, print "Good morning!" to simulate a greeting.
# 3. Create a list of weather conditions for the week. 
# 4. Use a loop to iterate over the weather list and use an 'if' statment to check if the current day's weather is "Rainy". If it is, 
# print a reminder to take an umbrella.
# 5. Create a list of calendar events fo the week.
# 6. Use a loop to find today's event and print it as a reminder.
# 7. Creatre a variable to store the number of unread emails.
# 8. Use an 'if' statement to check if tghere are any unread eamils and print the number if there are.
# 9. Call the 'morning_routine()' function texecute the morning routine.

# ***Hint***:
# You can use the 'datetime' module to get the current day of the week if you want to match the weather and events to the acutal day.
# '''

# import datetime

# def morning_routine():
#     print("Good morning!")
    
#     weather_conditions  = ['Sunny', 'Cloudy', 'Rainy', 'Rainy', 'cloudy', 'Windy']
    
#     today_weather = weather_conditions[datetime.datetime.today().weekday()]
#     # print(datetime.datetime.today().weekday())
#     print(today_weather)
#     if today_weather  == 'Rainy':
#         print("Don't forget to take an umbrella! It's rainy today")



#     calendar_events =  ['Meeting at 10am', 'Lunch at 12pm', 'Dentist appointment', 'Lunch with  friends',  'Movie night']
#     today_event = calendar_events[datetime.datetime.today().weekday()]
    
#     print(f"Today's event:  {today_event}")


#     unread_emails = 5
#     if unread_emails > 0:
#         print(f"You have {unread_emails} unread emails.")

# morning_routine()

# '''
# Exercise 2: The Versatile Coffe Machine

# You have a coffee machine that make various types of coffee. You want to program it to prepare your coffee based on you selection.

# 1. Define a function called 'make_coffee()' that takes one parameter 'coffee_tyupe' with a default vaule of "espresso".
# 2. Inside the function, print the message indicating the type of coffee being made. 
# 3. Create a list of coffee types that the machine can make. 
# 4. Use a loop to interate over the list of coffee types. 
# 5. Inside the loop, use an 'if' statement to check if the coffee type is "cappuccino". If it is, print a special message indicating that it's a favorite. 
# 6. Call the 'make_coffee()' function with different arguments to simulate making different types of coffee.
# 7. Ensure that calling 'make_coffee()' without arguments defaults to  making an espresso.

# '''
# def make_coffee(coffee_type="espresso"):
#     print(f"Making a cup of  {coffee_type} coffee!")

# coffee_types = ['espresso', 'cappuccino', 'latte', 'americano', 'mocha']

# for type in coffee_types:
#     make_coffee(type)
#     if type == 'cappuccino':
#         print("Cappuccino is my favorite!")

# make_coffee()

# '''
# Ex 3: The Dynamic Playlist DJ
# Develop a feature for a music app that allow users to create a custom playlist and play the songs in sequence.

# 1. Define a funciton called 'play_song()' that takes one parameter 'song_list'.
# 2. Inside the function, use a loop to iterate over 'song_list'.
# 3. For each song in the list, print a message indicating that the song is now playing.
# 4. Before calling the function, prompt the user to enther the number of songs they want to add to the playlist.
# 5. Use a loop and 'input()' to accept song names from the user, based on the number they provided, and store them in a list.
# 6. Call the 'play_song()' function with the user-crated list of song as an argument. 
# '''

# def play_songs(song_list):
#     for song in song_list:
#         print(f"Now playing: {song}")

# num_songs = int(input("How many songs would you like to add to the  playlist? "))

# user_playlist = []

# for i in range(num_songs):
#         song_name  = input(f"Enter song {i+1} name: ")
#         user_playlist.append(song_name)

# play_songs(user_playlist)


# '''Ex. 4: The Group Expense Tracker
# Create a program to track expenses for a group of friends on a trip. The program will calculate the total expenses and identify
# the highest spender.

# 1. Define a funciton called 'track_espenses()' that takes a variable number of numerical arguments representing individual expenses.
# 2. Insdie the function, calculate the sum of the expenses and print the total>
# 3.Also, determine the highest expense and print the person associated with it.
# 4. Outside the function, use a while loop to prompt each user to enter their expense untill they enter 'done'.
# 5. Use 'input()' to accept the expense amount from each user and store these in a list.
# 6. After collecting all expeses, call the 'track_expenses()' function with the list of expenses as arguments using the splat operator (*). 
# '''
# def track_expenses(*expenses): 
#     total_expenses = sum(expenses)
#     print(f"The total expenses are: {total_expenses}")
          
#     highest_expense = max(expenses)
#     spender = expenses.index(highest_expense)+1
#     print(f"Person {spender} is the highest spender with an expense of: {highest_expense}")

# group_expenses =  []

# while True:
#     expense_input = input("Enter your expense amount or 'done' to finish: ")

#     if expense_input.lower() == 'done':
#         break
#     else:
#         expense = float(expense_input)
#         group_expenses.append(expense)

# track_expenses(*group_expenses)

# '''
# Ex. 5
# The product Inventory
# Manager

# You are developing a feature for an e-commerce app that allows the store manager to view and update the inventory of products.

# 1. Define a list called 'products' that contains the initial inventory of product names.
# 2. Create a function called ' manage_inventory()' that will display the current inventory, allow the manager to add a new  product, and remove that are out of stock. 
# 3. Inside the function, use a loop to display optoins for the manager: view inventory, add prodcut, remove  product, or exit. and exit.
# 4. Use list slicing and the 'lent()' function to display the first 5 products  in the inventory when viewing. 
# 5. Allow the manager to add a product by entering it's name, which will be appended to the 'products' list. 
# 6. Allow the manager to remove a product by entering it's name. Ensure the product exist in the list before attempting to remove it.
# 7. Use the 'input()' function to collec the manager's choices and product names.
# '''
# products = ['T-Shirt', 'jeans',  'shoes', 'socks', 'hats',  'scarf', 'gloves']

# def manage_inventory():
#     while True:
#         print("\\nInventory Management System")
#         print("1. View Inventory")
#         print("2. Add Product")
#         print("3. Remove Product")
#         print("4. Exit")
#         choice = input("Enter your  choice: ")

#         if choice == "1":
#             print("\nCurrent Inventory:")
#             for product in products[:5]:
#                 print(product)
#             if len(products) > 5:
#                 print("..and more")
#         elif choice ==  '2':
#             new_product  = input("Enter the name of the product: ")
#             products.append(new_product)
#             print(f"{new_product} has been added to the inventory")
#         elif choice ==  '3':
#             product_to_remove = input("Enter the name of the product to remove: ")
#             if product_to_remove in products:
#                     products.remove(product_to_remove)
#                     print(f"{product_to_remove} has been removed from the inventory")
#             else:
#                  print(f"{product_to_remove} was not found in the inventory.")
#         elif choice == '4':
#             print("Exiting the inventory management system")
#             break
#         else:
#             print("Invalid choice. Please try again.")
# manage_inventory()



# '''
# Ex 6.: The Payment Splitter

# In a group of friends, expenses are often shared. Your task is to create a function that calculates how much each person must pay or be reimbursed after a shared expense.

# 1. Define a function a called 'split_payment' that takes a list of expenses and the number of friends as arguments.
# 2 The function should calculate the total expenses and the individual share. 
# 3. Return both the total and the individual share from the function.
# 4. Outside the function, use a loop to allow th euser to input the cost of each expense and add it to a list. 
# 5. After all expenses are entered, call the 'split_payment' funtion with the list of expenses and th enumber friends. 
# 6. Display the total expenses and how much each person must pay or be reimbursed.
# '''
# def split_payment(expenses, number_of_friends):
#     total_expenses = sum(expenses)
#     individual_share = total_expenses / number_of_friends
#     return total_expenses, individual_share

# expenses = []
# number_of_friends = int(input("Enter the number of friends: "))
# while True:
#     expense = input("Enter an expense or  'done' to finish: ")
#     if expense.lower() == 'done':
#         break
#     expenses.append(float(expense))

# total, share = split_payment(expenses, number_of_friends)
# print(f"Total expenses: ${total:.2f}")
# print(f"Each person must pay: ${share:.2f}")

# '''Exercise 7:
# The Phonebook Manager
# Task is to create functions that can add a new contact and display all contacts, ensuring that your crrectly handle variable scope.

# Instructions

# 1. Define a global list  called 'phonebook' to store contacts as separate lists for names and numbers.
# 2. Define a function called 'add_contact' that  takes a name and number as arguments and add them to the 'phonebook' list.
# 3. Define a function called 'display_contact' that prints all teh contact in the 'phonebook'.
# 4. Use a loop to allow the user to choose between adding a contact or display all contacts.
# 5. Ensure that the 'phonebook' list is not reintialized within the functions, preserving its global scope. 
# '''

# phonebook_names = []
# phonebook_numbers = []

# def add_contact(name, number):
#     global phonebook_names
#     global phonebook_numbers
#     phonebook_names.append(name)
#     phonebook_numbers.append(number)

# def display_contacts():
#     global phonebook_names
#     global phonebook_numbers
#     for i in range(len(phonebook_names)):
#         print(f"Name: {phonebook_names[i]}, Number: {phonebook_numbers[i]}")
# while True:
#     action = input("Choose an action: [A]dd contact,  [D]isplay contacts, [Q]uit: ")
#     if action == 'A':
#         name = input("Enter Contact's name: ")
#         number = input("Enter the Contact's number: ")
#         add_contact(name, number)
#     elif  action == 'D':
#         display_contacts()
#     elif action  == 'Q':
#         break
#     else:
#         print("Invalid choice. Please choose again.")

# '''
# Exercise 8 
# Task manage employee recored for a small company. Your job is to create functions that can add a new employee details,
# calculate average age, and display all employee information using lists instead of dictionaries.

# 1. Define a global list called 'employess' to store employee details, where each employee is representd as a list with elements 
# '[name, age, departmetn]'.
# 2. Define a function called 'add_employee' that takes name, age, and department as arguments and adds them as a list to the 'employees' list.
# 3. Define a function called 'calculate_average_age' that computes and returns the average age of all employees.
# 4. Define a function called 'display_employees' that prints all the employee details in a formated manner.
# 5. Usee a loop to allow th euser to choose between adding an employee, calculating the average age, or displaying all employees.
# 6. Ensure that the 'employees' list is not reinitialized within the functions, maintaining its globals scope.
# '''
# employees = []
# def add_employee(name, age, department):
#     global employees
#     employees.append([name, age, department])
# def calculate_average_age():
#     global employees
#     total_age = sum(employee(1) for employee in employees)
#     return total_age / len(employees) if employees else 0

# def display_employees():
#     global employees
#     for employee in employees:
#         print(f"Name: {employee[0]}, Age: {employee[1]}, Department:  {employee[2]}")

# while  True:
#     action = input("Choose an action: [A]dd employee, [C]alculate average  age, [D]isplay employees, [Q]uit: ").upper()
#     if action == 'A':
#         name  = input("Enter Employee's name: ")
#         age = int(input("Enter Employee's age: "))
#         department = input("Enter Employee's department: ")
#         add_employee(name, age, department)
#     elif action == 'C':
#         average_age = calculate_average_age()
#         print(f"Average age of employees is: {average_age:.2f}" )
#     elif action ==  'D':
#         display_employees()
#     elif action == 'Q':
#         break
#     else:
#         print ("Invalid choice. Please choose again.")

# The debugger
'''pdb = a GPS for your code helping you  navigate, pause, and inspect.
import pdb; pdb.set_trace() = use to starte debugging allowing you to inspect variables, test
conditions, and step through your code'''

'''
Example 1: The forgotten indentation

def greet(name):
print("Hello, " + name) # This will raise a SyntaxError because it's not indented correctly

Example 2: The Mismatche Data  Type
age  = input("Enter your age: ")
if age < 18:
print("You are a minor") # This will raise a TypeError because the input is a string,

Ex. 3: The Elusinve logical error 
def calculate_discount(price, discount):
    return price - discount # output is 99.8 instead of 80.0 (price * discount)

final_prince = calculate_discount(100, 0.2)
print(f"The discounted price is: ${final_price}")
# This will raise a NameError because final_price is not defined.


Example 4: Using the Debugger tool pdb

import pdb
def add_numbers(n):
    total = 0
    for i in range(n):
        pdb.set_trace() # Set a breakpoint here
        total += i
        return total
print(add_numbers(5))



Ex. 5. Debugging with print: The case of the Mysterious loop

def factorial(n):
    result = 1
    for i in range(n):
        print(r"Current value of result: {result}")
        result *= i
         print(f"Current value of result: {result}")
    return result
print(factorial{5}) #Expected: 120, Actual: 0

'''


