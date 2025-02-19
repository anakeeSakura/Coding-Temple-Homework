# # # # # # # '''
# # # # # # # The Proactive Approach: The try Block '''

# # # # # # # try:
# # # # # # #     # Code that might cause an exception
# # # # # # #     user_input  = int(input("Enter a number: "))
# # # # # # # except  ValueError:
# # # # # # #     # Code to handle the exception
# # # # # # #     print("That's not a valid number!")


# # # # # # # '''
# # # # # # # Customizing the Response: The except Block
# # # # # # # '''
# # # # # # # try:
# # # # # # #     # Code that might cause multiple exceptions
# # # # # # #     number = int(input("Enter a number: "))
# # # # # # #     result = 100 / number 
# # # # # # # except ValueError:
# # # # # # #     # Code to handle in correct input type
# # # # # # #     print("Please enter a valid number!")
# # # # # # # except  ZeroDivisionError:
# # # # # # #     # Code to handle division by zero
# # # # # # #     print("Sorry, infinity is not on the menu today. Try a non-zero number. ")

# # # # # # # '''
# # # # # # # The Catch-All: The General except block'''

# # # # # # # def perform_complex_calculation(data):
# # # # # # #     # Simulatin a complex calculation that might result in various exceptions
# # # # # # #     result = 0
# # # # # # #     for item in data:
# # # # # # #         result += item ** 2
# # # # # # #     average  = result / len(data)
# # # # # # #     return average

# # # # # # # # Handling the eceptions
# # # # # # # try:
# # # # # # #     # Code that  might cause an unexpected exception
# # # # # # #     data =  [1, 2, 3, 'a', 5]
# # # # # # #     calculation_result = perform_complex_calculation(data)
# # # # # # # except (ValueError, ZeroDivisionError):
# # # # # # #     # Code to handle the known potential issues
# # # # # # #     print("Please provide a list of numbers and ensure it's not empty.")
# # # # # # # except Exception as e:
# # # # # # #     # Code to handle any other unexpected exceptions
# # # # # # #     print(f"An unexpected error occurred: {e}")


# # # # # # # '''
# # # # # # # How to Raise an Exception '''

# # # # # # # fuel_level = -1
# # # # # # # if fuel_level < 0:
# # # # # # #     raise ValueError("Fuel level cannot be negative")

# # # # # # # '''
# # # # # # # Custom Exceptions
# # # # # # # '''
# # # # # # # fuel_level = 10
# # # # # # # tank_capacity = 9

# # # # # # # class FuelTankOverFlowError(Exception):
# # # # # # #     '''Exception raised when the fuel tank is overfilled.'''
# # # # # # #     pass
# # # # # # # if fuel_level > tank_capacity:
# # # # # # #     raise FuelTankOverFlowError("Fuel has exceeded the tank capacity")

# # # # # # # '''
# # # # # # # Exercise 1: E-commerce Product Catalog

# # # # # # # Build a Python program to manage an e-commerce product catalog efficiently.
# # # # # # # The program should facilatate adding a new product categories, adding products, displaying all available catgegories, and conduction
# # # # # # # product searches within the catalog. 

# # # # # # # 1. Initializa a dictionary to represent your porduct acatalog.
# # # # # # # 2. Implement functions to:
# # # # # # #     -Add a new product category. 
# # # # # # #     -Add a product to an existing category.
# # # # # # #     -Display all product categories with their respective products.
# # # # # # #     -Search for a product across all categories.
# # # # # # # 3. Include error handling for situations such as adding a product to an unliste category.
# # # # # # # 4. Ensure that the p roduct search is case-insensitive.
# # # # # # # 5. Design the program to handle multiple additions and searches.

# # # # # # # hints
# # # # # # # Start by pre-population your catalog dictionary with some categoris and products. 
# # # # # # # Utilize the 'lower()' or 'upper()' methods on strings for case-insesitive comparison.
# # # # # # # In yhour search function, check for the product's presnec in every category.
# # # # # # # Leverage 'try' and 'except' block to gracefull handle any keyError instances.'''

# # # # # # # def add_category(catalog,  category):
# # # # # # #     if category not in catalog:
# # # # # # #         catalog[category] = []
# # # # # # #         print(f"Category '{category}' added.")
# # # # # # #     else:
# # # # # # #         print(f"Category '{category}' already exist.")
        

# # # # # # # def add_product(catalog,  category, product):
# # # # # # #     try:
# # # # # # #         if product not in catalog[category]:
# # # # # # #             catalog[category].append(product)
# # # # # # #             print(f"Product '{product}' added to '{category}'.")
# # # # # # #         else:
# # # # # # #             print(f"Product '{product}' already exist in '{category}'.")
# # # # # # #     except KeyError:
# # # # # # #         print(f"Category '{category}' does not exist.")
        

# # # # # # # def display_categories(catalog):
# # # # # # #     for category, products in catalog.items():
# # # # # # #         print(f"{category}: {', ' .join(products)}")

# # # # # # # def search_product(catalog,  product):
# # # # # # #     found  = False
# # # # # # #     for category, products in catalog.items():
# # # # # # #         if product.lower() in [p.lower() for p in products]:
# # # # # # #             found = True
# # # # # # #             print(f"Product '{product}' was found.")
# # # # # # #             break
# # # # # # #         if not found:
# # # # # # #             print(f"Product  '{product}' not found.")


# # # # # # # catalog = {
# # # # # # #     "Electronics": ["Laptop", "Smartphone",],
# # # # # # #     "Books":  ["Fiction", "Non-Fiction"],

# # # # # # # }
# # # # # # # add_category(catalog, "Clothing")
# # # # # # # add_product(catalog,  "Electronics", "Camera")
# # # # # # # display_categories(catalog)
# # # # # # # search_product(catalog, "laptop")


# # # # # # # '''Exercise 2: The Simple Order Validator
# # # # # # # An online bookstore is processing orders 

# # # # # # # 1. Prompt the user to enter the quantity of books the wish ot order. 
# # # # # # # 2. Validate the input to ensure it is a postive integer.
# # # # # # # 3. If the in put is vailid, confirm the orrder by printing a message.
# # # # # # # 4. If the in put is invalid (not an integer or a negative number), Display an error message and prompt th eagain. 
# # # # # # # 5. Use a try/ except block to catch non-numeric inputs.

# # # # # # # Hints: 
# # # # # # # Use a while loop to keep asking for input until a valid quantity is entered. 
# # # # # # # Utilize the 'int()' function to convert the input to an integer and catch 'ValueError' for non-numeric inputs.'''

# # # # # # # def validate_order():
# # # # # # #     while True:
# # # # # # #         try:
# # # # # # #             quantity = int(input("Enter the quantity of books you want to order: "))
# # # # # # #             if quantity > 0:
# # # # # # #                 print(f"Thank you! You have ordered {quantity} books")
# # # # # # #                 break
# # # # # # #             else:
# # # # # # #                 print("Invalid quantity. Please enter a positve  integer.")
# # # # # # #         except ValueError:
# # # # # # #                 print("Invalid input. Please enter a number.")

# # # # # # # validate_order()

# # # # # # # '''Exercise 3: The Safe Calculator
# # # # # # # In a terminal based calculator app, its' crucial to ensure the at the user inputs are valid numbers before any arithmetic operation is performed. 
# # # # # # # Your task is to enhance th eapp's rebustness by implementing input valiadation that prevents the program form crashing when a user enters non-numeric data.

# # # # # # # 1. Write a function'safe_addition' that prompts the user for two nubmer and returns their sum. Its should handle any 'ValueError' exceptions that arise from non-numberic input. 
# # # # # # # 2. Use a loop to allow the user to try entering the nubmers again if theyu mae an input  error. 
# # # # # # # 3. Print the result of the additon if the i nputs are valid numbers.
# # # # # # # 4. Provide the user with the Option to perform another addition or exit the program. 

# # # # # # # Hints
# # # # # # # use the 'try' block to attempt to conevert the user input to floats.
# # # # # # # use the 'except' block to catch ValueError' and prompt the user to enter the numbers again. 

# # # # # # # '''
# # # # # # # def safe_addition():
# # # # # # #     while True:
# # # # # # #         try:
# # # # # # #             num1 = float(input("Enter the first number: "))
# # # # # # #             num2 = float(input("Enter the second number: "))
# # # # # # #             return num1 + num2
# # # # # # #         except ValueError:
# # # # # # #             print("Please  enter a valid number. Try again!")

# # # # # # # while True:
# # # # # # #     result= safe_addition()
# # # # # # #     print(f"The result of the addition is: {result}")

# # # # # # #     continue_input  = input("Do you want to perform another addition? (yes/no): ").lower()
# # # # # # #     if continue_input != 'yes':
# # # # # # #         break


# # # # # # # '''
# # # # # # # Exercise 4: The REsilient Diveder

# # # # # # # In a data analysis context, dividing by zero can often occur and lead to program crashes.
# # # # # # # Your task is to create a function that performs division but returns a specific message instead of crashing when a division by 
# # # # # # # zero is attempted. 

# # # # # # # Instructions

# # # # # # # 1. Write a function 'safe_divide' that takes two parameters, 'a' and 'b', and returns the result of 'a/b'.
# # # # # # # 2. Implement error handling to catch 'ZeroDivisionError' exceptions within the function. 
# # # # # # # 3. If division by zero occurs, the function should return a message indicating that division by zero is not allowed. 
# # # # # # # 4. Test the function with user input an dprint the result or error message. 

# # # # # # # Hints
# # # # # # # Use the 'try' block to attempt the divisoin operatoin. 
# # # # # # # Use the except' block to catch 'ZeroDivisionError' and return the appropriate message. 
# # # # # # # '''
# # # # # # # def safe_divide(a, b):
# # # # # # #     try:
# # # # # # #         return a / b
# # # # # # #     except ZeroDivisionError:
# # # # # # #         return "Division by zero is not allowed"
    
# # # # # # # while True:
# # # # # # #     try:
# # # # # # #         numerator = float(input("Enter the numerator: "))
# # # # # # #         denominator = float(input("Enter the denominator: "))
# # # # # # #         result = safe_divide(numerator, denominator)
# # # # # # #         print(f"The result of the division is: {result}")
# # # # # # #     except ValueError:
# # # # # # #         print("Please enter only numbers.")

# # # # # # #     continue_input = input("Do you want to perform another division? (yes/no): ").lower()
# # # # # # #     if continue_input  != 'yes':
# # # # # # #         break



# # # # # # '''
# # # # # # Exercise 5: The Login Gatekeeper

# # # # # # In a software application, it's crucial to ensure that user credentials meet certain security standards. 
# # # # # # Your task is t create a function that checks whether a username meets the required criteria and raises a custom exception if it does not. 

# # # # # # Instructions:
# # # # # # 1. Define a custom exception class names "UsernameError' that inherits fro mthe base 'Exception' class. 
# # # # # # 2. Write a function ' check_username' that takes a singe parameter, 'username', and checks if its meets the criteria (e.g., at least 6 characters long).
# # # # # # 3. If the username does not meet the criteria raise a "usernameError' with an appropriate error message. 
# # # # # # 4. Prompt the user to input a username and use a 'try-except' block to catch the 'UsernameError' and display the error message.

# # # # # # Hints:
# # # # # # User the 'raise' keyword to raise the custom exception with a message when the username is too short. 
# # # # # # In the except' block, catch the 'UsernameError' and print the message to inform the user.
# # # # # # '''

# # # # # # class UsernameError(Exception):
# # # # # #     def __init__(self, message):
# # # # # #         self.message = message

# # # # # # def check_username(username):
# # # # # #     if len(username) < 6:
# # # # # #         raise UsernameError("Username must be at least 6 characters long")

# # # # # # while True:
# # # # # #     username_input = input("Please enter your username: ")
# # # # # #     try:
# # # # # #         check_username(username_input)
# # # # # #         print("Username is valid!")
# # # # # #         break
# # # # # #     except UsernameError :

# # # # # #         print(f"Error: {UsernameError.message}")

# # # # # #     try_again_input = input("Would you like to try a different username? (yes/no): ").lower()
# # # # # #     if try_again_input != 'yes':
# # # # # #         break


# # # # # ''' 
# # # # # Exercise 6: The Data Sanitizer

# # # # # In data processing applications, it's common to encounter a mix of valid and invalid data entries.
# # # # # your task is to write a program that attempts to convert a list of string values to integers, gracefully handling any valuess that cannot be converted.

# # # # # instructions

# # # # # 1. Create a list of string where a some  represent integer values and others are non-numeric.
# # # # # 2. Iterate over the list and attempt to convert each string to an integer.
# # # # # 3. If a string cannot be converted to an integer, catch the 'ValueError' and print a warning message.
# # # # # 4. Store the successfully converted integers in a new list called 'parsed_data'.

# # # # # hints

# # # # # use a 'try-except' block within your loop to catch conversion errors. 
# # # # # print a warning message in teh 'except' block for each non-convertible string. '''

# # # # # data_entries = ["100", "200", "three", "400", "5ive"]
# # # # # parsed_data = []
# # # # # for entry in data_entries:
# # # # #     try:
# # # # #         parsed_data.append(int(entry))
# # # # #     except ValueError:
# # # # #         print(f"Warning: '{entry}' is not a valid integer and will be skipped.")
# # # # # print(f"Parsed Data:  {parsed_data}")

# # # # '''
# # # # Exercise 7: The Server's Graceful Exit

# # # # In server applications, unexpected exceptions can occur, an dit's crucial to handle these gracefully to prevent data loss and ensure necessary cleanup is performed.
# # # # Your task is to simulate a server's main operation loop and implement a mechanism that guarantees a graceful shutdown, even if an error occurs.

# # # # Instructions
# # # # 1. Simulate a server's main loop with a placeholder comment. 
# # # # 2. Use a 'try-except-finally' block to handle any potential exceptions during the server's runtime.
# # # # 3. In teh 'except' block, catch a general exception and print an error message.

# # # # Hints
# # # # The 'finally' block is executed after 'try' and 'except' blocks, regardless of whether an exception was raised or not.
# # # # Use the 'finally' block to include anyu code that you want to execute regarldess of exceptions, such as closing files or releasing resources.
# # # # '''
# # # # try:
# # # #     print("server is running...")
# # # #     # simulate an error
# # # #     raise Exception("Unexpected error!")
# # # # except Exception as e:
# # # #     print(f"An error occurred:  {e}")
# # # # finally:
# # # #     print("Server is shutting down...")
# # # #     print("Shutting down server gracefully")

# # # '''Exercise 8:User in put validation with fallback

# # # In user-driven applications, it's common to require in put that matches specific criteria.
# # # Your task is to write a program tha tprompts the user for their favorite fruit from a predefined list.
# # # if the input is not in th elist, the program should handle the situation gracefully and ask for input again.

# # # instructions
# # # 1. Create a list of fruits that are allowed inputs.
# # # 2. Prompt the user to enter their favorite fruit.
# # # 3. Use a 'try-except-else' block to validate the input. 
# # # 4. if the inppput is not in the list, raise a 'ValueError' and handle it by asking for input again. 
# # # 5. If the input is valid, print a confirmation message.

# # # Hints
# # # The 'else' block can be used to execute code when the 'try' block doesn't raise an exceptoin.
# # # use a loop to keep asking for input untill a valid fruit is entered.
# # # '''
# # # allowed_fruits  = ["apple", "banana", "cherry", "date", "elderberry"]
# # # while True:
# # #     try:
# # #         fruit = input("Enter your favorite fruit: ")
# # #         if fruit not in allowed_fruits:
# # #             raise ValueError("Invalid fruit. Please try again.")
# # #     except  ValueError as ve:
# # #         print(ve)
# # #         print("Please choose a fruit from the list.")
# # #     else:
# # #         print(f"Your favorite fruit is: {fruit}")
# # #         break
        

# # '''
# # Exercise 9. Multi-Scenario Input Handling

# # In a software application that processes user data, it's essential to anticipate and handle a different kinds of erroneous input. 
# # Your task is to write a program that asks users for their age and ensure that the input is both a number and within a reasonable range.

# # Instructions
# # 1. Prompt the user to enter their age.
# # 2. Use a 'try-except' block to handle the following scenarios:
# # The input is not a number ('ValueError').
# # the number is not within the range of 0 to 120 ('ValueError').
# # 3. If an exception is raised, provide a specific error message for the type of exeception and ask for the input again.
# # 4. If the input is valid, print a confirmation message.

# # Hints
# # Use 'int()' to convert the input string to an integer and catch any  'ValueError' exceptions.
# # Check the age range within the 'try' block and raise a 'ValueError' with a custom message if the age is out of range. 
# # '''
# # while True:
# #     try:
# #         user_age  = int(input("Enter your age: "))
# #         if user_age < 0 or user_age > 120:
# #             raise ValueError("Age must be between 0 and 120")
# #     except ValueError as ve:
# #         if "invalid literal" in str(ve):
# #             print("Invalid input. Please enter a whole number.")
# #         else:
# #             print(ve)
# #     else:
# #         print(f"Your age is: {user_age}")
# #         break
        

# '''
# Exercise 10: Robust Calculator Input Handling

# Your are developing a calculator app that can perform basic arithmetic operations. 
# The app should robustly handle user input, ensuring the only numerical values are accepted and operations are performed correctly.

# 1. Ask the user to enter two numbers.
# 2. Ask the user to choose an operation (addition, subtraction, multiplication, or division).
# 3. Peform the operation and display the result. 
# 4. Use a 'try-except' block to handle 'ValueError' and 'TypeError' exceptoins. 
# 5. No matter what happens, thank the user for using the calculator in a 'finally' block

# Hints
# Use float() to convert the input stgrings to numbers. 
# Use an 'if elif else' strctgure to perform the chosen operation. 
# In the 'except; blocks, handle 'ValueError' for non-numberic input and 'TypeError' for incorrect operations (like division by zero).
# Use the 'finally' block to print a than-you message.
# '''

# def get_number(prompt):
#     while True:
#         try:
#             return float(input(prompt))
#         except ValueError:
#             print("Invalid input. Please enter a number.")

# def get_operation():
#     operations = ['+', '-', '*', '/']   
#     while True:
#         op = input("Choose an operation  (+, -, *, /): ")
#         if op in operations:
#             return op
#         print("Invalid operation. Please chosse  one of the following: +, -, *, /")

# num1  = get_number("Enter the first number: ")
# num2  = get_number("Enter the second number: ")
# operation = get_operation()

# try:
#     if operation == '+':
#         result = num1 + num2
#     elif operation == '-':
#         result = num1 - num2
#     elif  operation == '*':
#         result = num1 * num2
#     elif operation == '/':
#         result  = num1 / num2
#     print(f"The result is: {result}")
# except TypeError:
#     print("Invalid operation. Please choose one of the following: +, -, *, /")
# finally:
#     print("Thank you for using the calculator!")  # This will always be printed, no matter


'''
Exercise 11: Nested Try blcoks in Data Entry

Create a data entry module for a software application where users can add numerical data to a list.
The module should validate the input and handle errors when users enter invalid data or attempt incorrect operations. 


1. Intialize an empty list to store numerical entries. 
2. Prompt the user to enter a number or 'done' to finish.
3. Use a nested 'try ' block to handle the following:
-Convert the input to a float and append it to the list. 
-If the userenter 'done', break out of the loop. 

4. Use an 'else' block to confirm the entry has been added. 
5. Handle 'ValueError' for non-numeric input and 'TypeError' for any type-related errors during conversion. 
6. Use a 'finally' block within the nested 'try' to inform the user that they can continue entering data. 
7. After the loop, print the list of entered numbers. 

Hints
Use a 'while' loop to continously prompt the user for input. 
Use 'float()' to attempt to convert th einput to a number. 
Use an 'else' blcok after the 'try' blcok to print a confirmation message. 
Use a 'finally' block to print a message that encourages the user to keep entering data '''

def data_entry():
    data_list =  []
    while  True:
        user_input = input("Enter a number or type 'done' to finish: ")
        if user_input.lower() == 'done':
            break
        try:
            try:
                number = float(user_input)

            except ValueError:
                print("That's not a number. Please enter a valid  number.")
                continue
            else:
                data_list.append(number)
        except TypeError:
            print("An unexpected error occurred. Please try again.")

        finally:
            print("You can enter another number or type 'done' to finish. ")

    print("Data entered:", data_list)    


data_entry()

