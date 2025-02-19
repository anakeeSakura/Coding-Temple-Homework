# flavors = ["vanilla" , "chocolate" , "strawberry" , "lemon" , "orange"]
# for flavor in flavors:
#     print("Mmm... I just sampled " + flavor + "!")

# # range() function helps you to:
# # 1. Generate a sequence of numbers
# # 2. Iterate over a sequence of numbers
# # 3. Create a sequence of numbers in a specific range
# for i in range(3):
#     print("Trying out flavor number  " + str(i+1) + ":" + flavors[i])

# # Nested Loops is  a loop inside another loop. 
# # It is used to iterate over two or more lists in parallel.

# flavors = ["vanilla" , "chocolate" , "strawberry" , " lemon" , "orange"]
# toppings =  ["whipped cream" , "chocolate chips" , "sprinkles" , "chopped nuts" , "caramel sauce"]
# for flavor in flavors:
#     for topping in toppings:
#         print("Lets's try a scoop of " + flavor + " with some " + topping + " on top!")

# #Break

# # The break statement is used to exit a loop when a certain condition is met.
# # It is used to terminate the loop and move to the next statement after the loop.
# # The break statement can be used with for and while loops.

# ice_cream_flavors  = ["vanilla" , "chocolate" , "strawberry" , "lemon" , "orange"]

# for flavor in  ice_cream_flavors:
#     if flavor == 'lemon':
#         print("Lemon is my favorite flavor! No need to taste further.")
#         break
#     print("Trying " + flavor + " flavor.")

# #Excersises
# #Given List
# booth_type = ["Food", "Games"  , "Movies" , "Crafts"]
# schedule_timeschedule_times = ["10:00 AM", "1:00 PM", "3:00 PM", "5:00PM"]
# items_needed = ["Grill", "Tickets", "Instruments", "Paint"]

# #EX.1 For Loop Festival Planner
# # Use a for loop to iterate over the booth types. 
# #For each booth type, print the type of booth, the schedule time, and the item needed.
# #Ensure that each booth type is matched with the correct schedule time and item needed from the lists provided. 
# for i in range(len(booth_type)):
#     booth =  booth_type[i]
#     time  = schedule_timeschedule_times[i]
#     item = items_needed[i]
#     print(f"{booth} Booth - Schedule:  {time} - Item Needed: {item}")


# #EX.2 Classroom seat assignment
# # 30 students - 5 rows
# #Each row can seat an equal number of students.
# #Use a for loop with the range function to assign and print a seat number for each student.
# #Seat numbers should start at 1 and increase sequentially. 

# total_students = 30
# rows = 5

# students_per_row = total_students // rows
# for row in range (1,  rows + 1):
#     for seat in range(1, students_per_row  + 1):
#         seat_number = (row - 1) * students_per_row  + seat
#         print(f"Row {row} - Seat {seat}: Student  {seat_number}")
              

# # EX.3 Shopping Cart total Calculator
# # List of item  prices
# # Use a for loop to iterate through the list of prices
# # Calculate the total cost by adding up the prices of all the items. 
# # Print the total cost at the end. 

# item_prices = [10.99, 7.99, 5.99, 13.99, 4.75]
# total_cost = 0
# for price in item_prices:
#     total_cost += price
# print(f"the total cost of the shopping cart is: ${total_cost:.2f}")

# # EX.4 Mulitplication Table Generator
# # Ask the user for the size of the multiplicaiotn table they wish to generate.
# # Use nested for loops to calculate the product of each pair of numbers. 
# # Display the multiplication table in a formated manner. 

# table_size = int(input("Enter the size of the multiplication table: "))
# for row in range(1, table_size  + 1):
#     for column in range(1, table_size + 1):
#         product = row * column
#         print(f"{product} \t", end="")
#         print()


# #EX.5 Inventorty Management
# # Create a list of items in the inventory with their current quantitites.quit
# # Use a for loop to iterate over each item
# # Use an if  statement to check if the quantity of an item is below the reorder theshold. 
# # Print out the nams of the items that need to be reordered.


# inventory  = [
#     ["Apples", 5],
#     ["Bananas", 2],
#     ["Oranges", 0],
#     ["Grapes", 15],
#     ["Eggs", 3]
#     ]

# reorder_threshold =  3
# for item in inventory:
#     name, quantity = item
#     if quantity <= reorder_threshold:
#         print(f"{name} needs to be reordered.")
        
# #Ex.6 Treasure Hunt
# # Treasure Game
# caves  = [False,  False, True, False, False]
# for index, cave in enumerate(caves):
#     # Check if the cave has the treasure
#     if cave:
#         print(f"Treasure found in cave {index +1}!")
#         break
#     else:
#         print("No treasure in cave.")

# #Exercise 7. Email cleanup
# emails = ["user1@example.com", None, "user2@example.com", None]
# valid_emails  = []
# for email in emails:
#     print(f"Checking this emails: {email}")
#     if email is None:
#         print(f"email {email} is not valid")
#         continue
#     input()
#     print("Adding to valid_emails list...")
#     valid_emails.append(email)
#     print(valid_emails)

#     # While loop 

#     marshmallows  = 0
#     while marshmallows < 5:
#         marshmallows  += 1
#         print("Added a marshmallow! Now there are " + str(marshmallows) + " marshmallows.")
# # Where you place the increment(marshmallows  += 1) is important. 
# # At the beginning: It instantly updates, ensuring your loop mirrors the current state with each marshmallow addition.marshmallows
# # At the end: It delay updates, useful but can be tricky, possibly causing off-by-one errors.

# marshmallows =  0
# while  marshmallows < 5:
#     print("Planning to add a  marshmallow! Currently, there are " + str(marshmallows) + "marshmallow.")
#     marshmallows += 1


# # The Non-started Loop:If your while loop condition is never intially true, it's an unused path. 
# # This is a common pitfall in programming, especially when using while loops with conditions that depend on
# # external factors. To avoid this, ensure your loop condition is always true at the start, or
# # use a for loop instead.

# temperature  = 100
# # Set up a while loop with a condition that is never true
# while temperature  < 0:
#     #This block of code will not execute because the initial temperature is 100, which is not less than 0
#     temperature -= 1
#     print("The temperature is now:", temperature)

#     # Since the loop body never executes, the is print statemnt will run immediately
#     print("The temperature was never below 0 to begin with.")

# # The Infinite Loop:If your while loop condition is always true, your loop will run indefinitely.
# # This can be useful for tasks that require continuous execution, such as monitoring a system or
# # handling user input. However, it can also lead to performance issues and make your code harder to
# # debug. To avoid this, ensure your loop condition is always false at the start, or use
# # a for loop instead.
# # Initialize a variable

# while True:
#     user_input = input("Say 'stop' to end the refill:  ")
#     if user_input.lower() == 'stop':
#         break
#     else:
#         print("Here's more coffee!")


# # A while loop's exit strategy is vital as it specifies when an how the loop will end. 
# # If not handled  properly, it can lead to infinite loops or loops that never start.
# # potentially causing your program to freeze or use excessive resources. 

# # Key components
# # The break statement is used to exit a loop when a certain condition is met.
# # termination  condition is met, the loop will terminate.
# # State change : The break statement changes the state of the loop by terminating it.

# # The Decrementing  Loop:If you want to count down from a certain number, you can use a while loop with
# # a decrementing condition. This is useful for tasks that require a countdown, such as a timer
# # or a countdown to a specific event.

# steps = 10
# while steps > 0:
#     print("Descending the stairs, " +
# str(steps) + " steps remaining.")
#     steps -= 1 # Take a step down
#     print("You have reached the bottom of the stairs")


# # Exercise 1: The Countdown Timer
# # You are programming a countdown timer for a game that starts from a specified number and counts down to zero. You need
# # to display each number as the timer counts down.

# # Here are the task you need to perform:

# # 1. Initialize a variable with the starting number of the Countdown. 
# # 2. Use a 'while' loop to keep the countdown going as long as the timer is greater than zero. 
# # 3. Inside the loop, decreas the timer by one and then print the current value of the timer. 
# # 4. Once the countdown reaches zero,  print a message indicating that the countdown has ended.
# # Hint: Remember to decrement the timer variable inside the loop to avoid creating an  infinite loop.

# timer  = 10
# while timer > 0:
#     print(timer)
#     timer -= 1 # Decrement the timer by one 10 - 1 and so on 
#     print("Countdown has ended")


# # Exercise 2: The Patient Queue
# # 1.  Initialize a variable with the number of patients in the queue. 
# # 2. Use a 'while' loop to simulate calling each patient untill the queue is empty. 
# # 3. Inside the loop, decrement the number of ptients as eacch one is called. 
# # 4. Print a message each time a patient is called and when the queue is empty.
# #Hint:
# # Make sure to decrease the number of patients in the queue to reflect that  a patient has been called.
# patients = 5
# while patients > 0:
#     print(f"Patients number {patients} please come in.")
#     patients -= 1 # Decrement the number of patients by one patient = 5 - 1 short hand
#     print("The queue is empty")

# #Exercise 3: The battery charger with efficiency check
# #Hint you will need to adjust the increment value within the 'while' loop based on the charge level.
# '''
# Initialize a variable to represent the battery charge level. 
# Use a 'while' loop to charge the batter  in increments. 
# Inside the loop, use 'if' statements to check the charge level. 
# If the charge level is 50% in crease the charging increments.
# If the charge level reaches 80%, decrease the charging increments to prevent damage. 
# Print the battery level at each increment and a message when the battery is fully charged.
# Hint: You will need to adjust the increment vaule within the 'while' loop based on the charge level.'''
# battery = 0
# increment = 10
# while battery < 100:
#     battery += increment # batter = 0 + 10 => battery = 10
#     print(f"Battery level: {battery}%")
    
#     if battery == 50:
#         print("Efficiency check: Increasing charge rate.")
#         increment = 15 # Increase the increment value to 15 when battery level reaches 50%
#     elif battery == 80:
#         print("Efficiency check: Decreasing charge rate to prevent overcharging.")
#         increment = 5 # Decrease the increment value to 5 when battery level reaches 80
        
# print("Battery fully charged")

# #Exercise 4: The Smart Coffee Machine
# #Hint: You will need to use list methods to remove coffee types once they are dispensed. 
# ''' 
# Initialize a variable to represent the coffee reservoir level. 
# Create a list of coffee that the machine can dispense. 
# Use a 'whle' loop to dispense coffee untill the reservoir is empty. 
# Inside the loop, use an 'if' statement to check if there are stil coffee types available. 
# Dispense each type of coffee and the remove it from the list. 
# Print the type of coffee dispensed and the remaining coffee types in the list. 
# Print a mesaage when the coffee reservoir is empty. '''

# coffee_reservoir = 10
# coffee_types = ["Espresso", "Cappuccino", "Latte", "Americano", "Mocha"]

# while  coffee_reservoir > 0:
#     if  coffee_types:
#         current_coffee  = coffee_types.pop(0) # Remove the first coffee type from the list
#         print(f"Dispensing {current_coffee}.")

#         coffee_reservoir -= 1
#         print(f"Dispensing {current_coffee}.")
#     else:
#         print("No more coffee types available")
#         break
#     print("The coffee resevoir is empty")

# # Exercise 5: The Intelligent Elevator System
# # Hint: You will need to use list methods to remove floors from the list once they are  visited.
# '''
# Initialize a variable for the starting floor.
# Create a list of floors where passengers have requested stops. 
# use a 'while' loop to move the elevator down floor by floor.
# Inside the loop , use the membership operator to check if the current floor is in the list of requested stops. 
# If the current floor is a requested stop, print a message and remove that floor from the list. 
# Continue moving down untill the gournd floor is reached.
# Print a message each time the elevator moves down a floor and when it reach the gournd floor.
# Hint
# You will need to use list methods to remove floors from the lis once they visited. 

# '''
# current_floor = 5
# requested_stops  = [1, 3, 4]
# while current_floor > 0:
#     if current_floor in requested_stops:
#         print(f"Stopping at floor {current_floor}.")
#         requested_stops.remove(current_floor) # Remove the current floor from the list of requested stops
    
#     current_floor -= 1 # Decrement the current floor by one
#     print(f"Descending to floor {current_floor}.")  

# #Exercise 6. The Smart Traffic Light System

# ''' 
# Create a list of colors representing the traffic light sequence. 
# initialize a counter for the green light.
# Use an infinite while loop to cycle thorugh the traffic light colors.
# Inside the loop, use the count method to track the number of times 'green' appears
# Breath the loop when the green light thas appeared a specific number of times.
# Print a messagfe each time the light changes and when the loop breaks for maintenance. '''

# traffic_lights =  ['Red', 'Yellow', 'Green', 'Yellow']
# green_count  = 0

# while True:
#     for color in traffic_lights:
#         print(f"The traffic light is now  {color}.")
#         if color == 'Green':
#             green_count += 1
#             if  green_count == 3:
#                 print("Maintenance time! The cycle will stop.")
#                 break
#     if  green_count == 3:
#         break


# # Exercise 7. the skipping rope challenge. 
# '''
# Initialize a countdown variable with the starting number.
# Create an empty list to store the nubmers you land on. 
# write a while loop that counts down from the starting number. 
# use the continue statmment to skip every other number.
# Append the number yhou land on the list. 
# use list slicing ot display the final list of numbers. '''

# count  = 10
# landed_numbers  = []
# while count > 0:
#     count -=  1
#     if  count % 2 == 1:
#         continue
#     landed_numbers.append(count)
# print("Numbers Landed on:",landed_numbers[::-1])

# # PIP: your python package courier
# # "PIP stands for "Pip installs Packages" or "Pip installs Python."
# # It's a command-line tool that helps you install, 
# # update, and remove Python packages. 
# # Installing a package = pop install package-name 

# # The random package  is a built-in package in Python. 
# # You can use it to generate random numbers.
# import random
# # Let's roll the dice 10 times
# for _ in range(10):
#     dice_roll  = random.randint(1, 6)
#     print(f"You rolled a {dice_roll}")

# # Coding temple's example
# for  _ in range(10):
#     dice_roll = random.randint(1, 6)
#     print("You rolled a " + str(dice_roll) + "!")

#Shuffling a playlist
# import random
# playlist  = ['song1',  'song2', 'song3', 'song4', 'song5']
# random.shuffle(playlist)

# #Let's see the shuffled playlist 
# for song in playlist:
#     print(song)

# import random
# snacks  = ['chips', 'popcorn', 'candy', 'cookies', 'chocolate bar']
# picked_snack = ''

# while picked_snack != 'chocolate bar':
#     picked_snack = random.choice(snacks)
#     print("You got a  " + picked_snack + "!")
#     if picked_snack != 'chocolate bar':
#         print("Let's pick again!")
#     else:
#         print("Yay! You got the chocolate bar!")

# '''
# Import the random module to use its choice selection capabilites. 
# Create a list of participant names, including 'Alex'.
# Use a while loop to repeatedly draw a name randomly from the list of participants.
# The loop should only terminate when 'Alex' is drawn.
# Ensure that the loop does not produce any output until 'Alex' is drawn.
# '''
# import random
# participants = ['Alex', 'Bob', 'Charlie', 'David', 'Eve']
# while'Alex' not in random.choices(participants, k=1):
#     pass
# print("Alex has been drawn!")

# '''
# Exercise 2. Random Walk simulation
# Import the random module to tuilize its random selection feature. 
# Define a list of directions that the entity can take. 
# Use a for loop to simulate 10 steps.
# In each iteration, randomly select a direction and simulate taking a stoep in that direction. 
# print out the direction of each step.
# '''

# import random
# directions = ['north', 'south', 'east', 'west']
# for step in range(10):
#     step_direction  = random.choice(directions)
#     print(f"Step {step + 1}: The entity moves 10 steps to the {step_direction}.")


# '''
# Exercise 3

# Import the 'random' module to generate randome dice rolls. 
# Use a 'while' loop ot keep rolling the dice untill the same number appears on both. 
# In each iteration, simulate rolling tow dice.
# Check if the two dice have the same number. If theyuu do, exit the loop.
# Print out the result of each roll and a mesage when both dice match. '''

# import random
# while True:
#     dice1 = random.randint(1, 6)
#     dice2 = random.randint(1, 6)
#     print(f"Dice1: {dice1}, Dice 2: {dice2}")
#     if dice1 == dice2:
#         print(f"Both dice landed on {dice1}")
#         break

# '''
# Exercise 4
# Import the random module to shuffle the list of questions. 
# Use the random. shuffle() method to randomize the order of the quiz questions. 
# Use a for loop to iterate throught the shuffled list an dpresent each questions. 
# Print out each question to the user. 
# '''
# import random
# questions = ['What is the capital of France?', 'What language family does Lao belong too?', 'What is the largest planet in our solar system', 'What is the chemical symbol for gold?']
# random.shuffle(questions)
# for question in questions:
#     print(question)

'''Import the random module to use the sampling function.
Use the random.sample() method to randomly select 5 names from the list of students.
Print out the names of the selcted students as part of the attendance check. '''

#Exercise  5

import random
students = ['John', 'Mary', 'Jane', 'Bob', 'Alice', 'Eve']
selected_students = random.sample(students, 5)
for student in selected_students:
    print(f"Is {student} present?")

#Exercise 6
'''
Import the random and string modules.
Combine uppercase letters, lowercase  letters, digits, and punctuation to create a pool of characters.
use a loop to reandonly select 8 characters from the pools to form a password.
Print out the generated password.
'''
import random
import string

characters = string.ascii_letters +  string.digits + string.punctuation

password = ''.join(random.choice(characters) for _ in range(8) )
print(f"Generated password:  {password}")

#Exercise 7
'''
Import the random module.
Create a loop that will run a specified number of times to generate random color values.
In each iteration, generate three separate number ranging form 0 to 255, representing the Red, Green, and Blue (RGB) components of a color.
Print out the generated RGB color value in a readable format.
'''
import random
num_colors = 10
for _ in range(num_colors):
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    print(f"generated RGB color: ({red}, {green}, {blue})")


#For Loop
genres =  ['Rock', 'Pop', 'Jazz', 'Classical', 'Hip-Hop']
for genre in  genres:
    print("Now playing:  " + genre)
    
genres =  ['Rock', 'Pop', 'Jazz', 'Classical', 'Hip-Hop']

for index in range(len(genres)):
    print("Track "  + str(index + 1) + ":" + genres[index] + " - Light show is on!")


full_playlist = ['track1',  'track2', 'track3', 'track4', 'track5']

middle_tracks = full_playlist [1:4]

for track in middle_tracks:
    print("Playing " + track + " - The heart of our playlist!")


# Riff 
full_playlist =  ['track1',  'track2', 'track3', 'track4', 'track5']

for track in full_playlist [1::2]:
    print("Every other track:  " + track)

# [num for num in range [20] if num  % 2 == 0]

'''
Create a list of student names.
use slicing to select the top three students.
use a for loop to interate through the sliced list.
print each name with a congratulatory message. '''

student_names = ['John', 'Mary', 'David', 'Emily', 'Michael', 'Sarah']
top_students = student_names[:3]
for name in top_students:
    print("Congratulations, " + name + " you made it to the top three!")

'''
Loop through the inventory list using a while loop an dindex numbers.
Use if statemetns to check the data type of each item. 
print the item and its data type. '''

inventory = ['apple', 120, 'Oranges', 80, True, 'Bananas', 150, False]

index = 0

while index < len(inventory):
    item = inventory[index]

    if type(item) == str:
        print(f"item: {item}")
    elif type(item) == int:
        print(f"Quantity: {item}")
    elif type(item) == bool:
        status = "on sale" if item else "not on sale"
        print(f"Sale status:{status}")
    index += 1

'''
Use list comperehension to generate the squares of number from 1 to 10.
Each element in the new list should be the square of an integer from the original range.
'''
squares = [number**2 for number in range (1, 11)]                                           
print(squares)

'''
Start with a list of number from 1 to 20.
Use list comprehension to filter out the even numbers. 
Remember that an even number is divisible by 2 with no remainder.
'''
numbers = list(range(1,21))

even_numbers = [number for number in numbers if number % 2 == 0]
print(even_numbers)


'''
Begin with a  full list of ingredients.
Use slicing to select the first half of the list. 
The length of the list can be found using the 'len()' function, and you can divide it by
2 to find the midpoint. '''

ingredients = ['salt', 'pepper', 'paprika' , 'garlic' , 'onion' , 'beef', 'tomato', 'basil']

needed_ingredients =  ingredients[:len(ingredients)//2]

print(needed_ingredients)

'''
Start with the full list of article titles.
Use slicing with nagtive indices to selct the last three titles in revers order. 
Remember that in Python, negative indices count form the end of the list.
'''
articles = ['Article1',  'Article2', 'Article3', 'Article4', 'Article5']
recent_articles = articles[-1:-4:-1]
print(recent_articles)

'''
Use a list comprehension to iterate through numbers 1 to 30.
Include a condition within the list comprehension to select only the multiples of three. 
Store the resulting list in variable. 
'''
multiples_of_three  = [number for number in range(1,31) if number % 3 == 0]
print(multiples_of_three)







  
     

