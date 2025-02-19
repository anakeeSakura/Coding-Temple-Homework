# # if 7 > 5 :
# #     print ("Seven is greater than five!")

# # # This is a comment
# # print('this is not a comment')

# # #This is my variable
# # a = "hi"

# # #This is a condition
# # if 9 > 5:
# #     print(a)

# #This is a Mulit line Statement in Python (code did not work but worked in video example slide 16)
# a = '''Python's 
# Multi-Line 
# Groove!'''

b = "Hello, Coding Templers \
    How are you today?"

# print(a)
print(b)
for i in range(3):
    print(i)


# # sakura = '''
# # cherryblossom blizzard
# # asdfasdf''' 

# # theString = "a string with \"hello\"  "
# # print(sakura)
# # print(theString)

# # Hello = """kjdfjaslkfj
# # dlkaf"jlsdjfla
# # dsalkfjsdlj"flaj"""
# # variavble2 = '''asdfasd'''

#Exercise 1: Dance to the Python Rhythm!

#1. Create a multi-line string using triple quotes. This string should be a small paragraph about your favourite hobby, passion, or a general thought.
#2. Write a Python statement to perform a simple calculation, suich as adding two numbers. Add a comment explaining the purpose of this statement. 

# favorite_qoute = """
# Python programming is more than just a skill;
# it's a journey into the world of problem-solving and creativity, 
# where each line of code is a step towards mastery.
# """

# print(favorite_qoute)

# sum = 5 + 3
# print ("The sum of 5 and 3 is:", sum)

# # this is called string formatting
# print(f"this is a string with the sum:{sum} inside")

# import math
# # some_number = ""
# # this_that = ""
# # kdkdkd= "kdasjflkdsajl"
# # iLovePizza = "peperoni"
# # # print(iLovePizza)


# # def fake_bin(x):
# #     digits = ""
# #     for num in x:
# #         # print(num)
# # #         print(num) comments are used to explain code and its color is green
# #         if int(num) < 5:
# #             digits = digits + "0"
# #             print(digits)
            
# # #             print(digits)
# #         else:
# #             digits = digits + "1"
# #             print(digits)
# #     return digits 


# the_list = ["1", "2", "3", "4",  56]

# # print(the_list[0] + "10")
# # print(the_list[2] + "10")
# # # new_string = fake_bin(the_list)

# # print(new_string)

# def donuts(donuts):
#     fattyFoods = "donuts"


# class Test:

#     donut =""
#     def __init__(self):
#         self.donut = "donut"



# the_class_instance = Test()

# print(the_class_instance.donut)



# theChar = 'C'

# print(theChar)

# theFloat = 2.5


# the_class_instance.the_method()
  
# theBolean = True
# secondBolean = False

# earth = "round"
# try:
#     x > 3 
# except: 
#     print("pirnting somehting")
# finally:
#     print("the finally")

# if (earth == "round"):
#     print("The Earth Is Round") 
# elif(earth == "potato"):
#     print("the earth is a potato")
# else: 
#     print("The Earth Is Flat")





# count = 1
# while(theBolean):
#     print("I am in the while loop iteration: " ,     count)
#     count += 1
#     if (count == 5):
#         theBolean = False

# addition_numbers = 5 + 5
# print(addition_numbers)

# multiply_number = 10023423423400 * 2342342342323434324
# print(multiply_number)
# print(math.pi)

# genre = input("enter the genre: ")
# runtime = float(input("enter the runtime: "))
# if (genre == "action") and (runtime < 2):
#     print("Let's Watch It")
# elif (genre == "action") and (runtime >=2):
#     print("Can't watch no time")
# elif ( genre == "BL Movie") and (runtime < 2):
#     print("Lets Watch it!!!")
# else:
#     print("No time to Watch!!!!")

# #why are Variables So important?

# user_name = input("What's your name? ")
# print("Hello, " + user_name + "! ")

# def order_coffee():
#     return "A cup of coffee for your thoughts!"

beach = "Sunny Shore"
print(beach)

X = 123
print(type(X))
y = str (X)
print(type( y))

x = "123.456"
print(type(x))

y = float(x)
print(type(y))


fruits=["apples", "kumqot", "lychee"]
def weight_loss(x):
    for healthy in x:
        print(healthy)
weight_loss(fruits)
print("\n")

fatty_foods= ["chips", "donuts", "cookies"] 
def weight_gain(x):
    for unhealthy in x:
        print(unhealthy)
weight_gain(fatty_foods)

numbers=["1","2","3"]
def num(x):
    for integers in x:
        print(integers)
        int(integers)
        print(type(int(integers)))
num(numbers)

mood = "happy"
print(type(mood))







# import random

# word_bank = [ 'seahawks', 'resident evil', 'halo', 'alpha', 'final fantasy']
# word = random.choice(word_bank)

# name = input('What is your name? '). title()
# print(f'Hello {name}, lets play some Hangman!')

# guesses =  ' '

# turns = 6

# while turns > 0:

#     failed = False
    
#     for char in word:

#         if char in guesses:
#             print(char, end='')
#         else:

#             print('_', end='')
#             failed = True


# if not failed:
#     print(f'Congrats, you guessed the word: "{word}"!')
#     break

# guess = input('Guess a letter: ')

# guesses += guess

# if guess not in word:

#     turns -= 1

#     if (turns > 0):

#         print(f'Wrong guess, try agian! You turns left')


#     print(f'Wrong guess, try again! You have {turns} turns left!')

#     if (turns == 0):


# #Exersise 1: **Naming Convention Challenge**
# - Create a variable that holds your full name. Make sure the variable name follows the naming convention rules. Print the variable. 
# ... 

full_name = "Sirivanh"

print(full_name)


#Arithmetic Operators Excersises
 #Excercise 1: The Baker's Dilemma 

#If one cake requires 250 grams of flour and you have 2.5 kilograms of flour, how manyu cakes can you make using the arithmetic operators?

flour_per_cake = 250
total_flour = 2.5 * 1000  # =2.5 kilograms
number_of_cakes = total_flour // flour_per_cake #floor devision rounds down //
print(number_of_cakes)

#Excersise 2: Claiming Territories Assignment Operator

#Use the assignment operator to claim a variable kingdom with a value of "Pythonland"

kingdom = "Pythonland"
print(kingdom)

#Exercise 3: Fashon Contest comparison operator

#Given two shirt with prices shirt1 = 45 and shirt2 = 50. Use a comparison operator to check if shirt1 is cheaper thean shirt2. 

shirt1 = 45
shirt2 = 50
result = shirt1 < shirt2
print(result)

# ''' 
# Excercise 4: Rainy Day Dilemma Logical operation
# It will rain today, but your're not sure if it will be heavy.
# Write a logical operation to determine if you should take an umbrella if it's either going to rain or going to rain heavily. 

#  '''

rain = True
rain_heavily = False 
take_umbrella = rain or rain_heavily
print(take_umbrella)

# ''' Exercse 5: Royal Order

# Evaluate the expression 3 + 5 * 2 - 8. What would be the order of operations? 
# '''


results = 3 + 5 * 2 - 8 
print(results) #output should be 5 PEMDAS Prantheses, Exponent, Mulitplication, Division, Addition, Subtraction

# ''' 
# Exercise 6: The Pastry Fraction 
# you have 10 pastries and you want to divide them equally among 3 friends How many pastries does each friend get an dhow many are left?
# '''

pastries = 10
friends = 3

each_get = 10 // 3 
left_over = 10 % 3 
print(each_get, left_over)


# ''' Exercise 7: Kingdom Expansion Assignment operator

# You already have a kingdom named "Pythonland". Use the assignment operator to add " is wonderful!" to it. 
# '''
kingdom = "Pythonland"
kingdom += " is wonderful"
print(kingdom)

capital_of_mn = "St.Paul"
capital_of_mn += " is ghetto"
print(capital_of_mn)


# ''' Exercise 8: Royal Duel Comparison Operator 
# Two Knights have strength values of knight1 = 45 and knight2 = 50. Use a comparison operator to determine if knight1 has the same strenght as knight2. 
# '''

knight1 = 45
knight2 = 50
# 45 = 50 ==> False
result = (knight1 == knight2)
print(result)

divante = 32
sakura = 38

older = (divante == sakura)
print(older)

# ''' Exercise 9: Chef's Special
# A chef has two ingredients: eggs = True and flour = False. He can only make pancakes if he has both. Determine if the chef can make pancakes. 
#  '''

eggs = True
flour = False
make_pancakes = eggs and flour
print(make_pancakes)

# ''' 
# Exercise 10: Medieval Architecture 
# A castle's height is 100 units and its moat's width is 50 units. If you double the castle's height and halve the moats's width, what would be the new dimensions?
# '''

castle_height = 100
moat_width = 50

castle_height *= 2
moat_width /= 2
print(castle_height, moat_width)

# My script 
castle_height = 100
moat = 50

new_castle = castle_height * 2, moat // 2
print(new_castle)


# Python Syntax topic Logic Errors: 

# Exercises: 

# ''' 1. The Forgotten Quote: Correct the syntax error '''

print("Hello, World!")

# ''' 2. The Mismatched Socks: Identify the logic error in the code. It's meant to check if a number is odd '''

num = 7
# 7 % 2 ==> 1
# 1 != 0 ==> True
if num % 2 != 0:
    print("The number is odd!")    
else:
    print("The number is even!")

# ''' 3. The Overeager Greeter: Find the logic error in the ocde which is meant to greet only the color red. '''

color = "pink" 
if color == "red":
    print("Hello, red!")
else:
    print("You're not red!")

color = "red"
if color == "red":
    print("Hello, red!")
else:
    print("You're not red!")

print(type ("Hello world"))

a,b,c = "apple", "banana", "cherry"
print(a,b,c)


floating = 3.14
print(type(floating))

pie = 5
freinds = 3

results = 5 // 3 
left_over = 5 % 3

print(results, left_over)


fruit = ["apples", "banana", "cherry"]
if fruit == "apples":
    print("Apple is a fruit!")
else:
    print("Apple is not a fruit!")

# result= 10/0

# def is_odd(num): if num % 2 == 0: return True else: return False


print("Hello, World!")


# Topic1: The Mighty if: The First Path

# The Magic of conditional statements

# Defining a variable and setting it to True

# Example 1. Simple conditions: Clear Skies Ahead

weather = "sunny"

if weather == "sunny":
    print("Time for a picnic!")

# Example 2. Combining Conditions: Two Paths Converging

gold_coins = 10
silver_coins = 50

if gold_coins > 5 and silver_coins > 30:
    print ("Enought to buy the magic potion!")

# Example 2. Not Conditions:
# Beware of Trap!

enemy = "goblin"
if enemy != "dragon":
    print("Charge foward, brave adventure")

# Example 4. Greater or Lesser Conditions: The Weighing Scales of Fate

player_health = 75

if player_health <= 100:
    print("Drink a health potion for full strength")

# Example 5. Checking Ranges: The guarded Treasure Chest

magic_stones = 12
if 10 <= magic_stones <= 20:
    print("You've unlocked the Eleven chest!")

# Example 6. combining Negative Checks The Double Guardian

is_daytime = False
dragon_asleep = True
if not is_daytime and dragon_asleep:
    print("Sneak into the dragon's lair to retrieve the colden chalice!")







torch_lit = True

# We are writing an if statement. If torch_lit is True, we want the print statement to run
# long hand
if torch_lit == True:
    print("venture forth into the cave!")

# short hand 
if torch_lit:
    print("venture forth into the cave! ")
# Another way it operates as long if statement is true
if 10 > 9: 
    print("venture forth into the caven!")


# Topic:2 The Elusive Elif The Alternate Route

# The crucial Part of the "if-elif-else" Structure
# Example 1. Potion Strength check

potion_strength = 15
if potion_strength > 20:
    print("Its's a super potent poition!")
elif potion_strength > 10:
    print("It's a moderately potent poition!")

# Example 2. Weather Advisory
weather = "rainy"
if weather == "sunny":
    print("Its's a bright and beautiful day!")
elif weather == "rainy":
    print("Carry an umbrella!")
elif weather == "snowy":
    print("Time to build a snowman!")

#    Example 3. Magic Sword quality
# 
sword_material = "silver"

if sword_material == "gold":
    print("The sword shines brightly!")
elif sword_material == "silver":
    print("The sword has mystical glimmer!")
elif sword_material == "bronze":
    print("The wsord looks ancient and valuable!")

# Example 4. Dungeon Level Access

player_level = 12

if player_level < 5:
    print("Access the beginner dungeon!")
elif 5 <= player_level < 10:
    print("Enter the intermediate dungeon!")
elif player_level >= 10:
    print("Challenge the advanced dungeon!")

# Example 5. Dragon's Lair Alert System

is_dragon_present = True
has_treasure = False

if is_dragon_present and not has_treasure:
    print("Enter with caution! Dragon ahead, but no treasure in sight.")
elif not is_dragon_present and has_treasure:
    print("No dragon around! Quick, grab the treasure.")
elif is_dragon_present and has_treasure:
    print("A mighty dragon guards the treasure! Tread carefully.")
else:
    print("Empty Lair. Safe to explore, but no treasures here.")

# Example 6. Potion Mixing Consequences

red_potion = True
blue_potion = False

if red_potion and not blue_potion:
    print("You get a potion of strength!")
elif not red_potion and blue_potion:
    print("You get a potion of Speed!")
elif red_potion and blue_potion:
    print("Oops! Mixing red and blue makes it explode!")
else:
    print("No potion was mixed.")

# More conditionals Examples

moon_phase = "full moon."

if moon_phase == "full moon":
    print("Beware of werewolves!")
elif moon_phase == "new moon":
    print("Witches' night out!")

potion_strength = 15

if potion_strength > 20:
    print("It's a super potent potion!")
elif potion_strength > 10:
    print("It's a moderatly potent potion!")


# Topic:3 The Trusty Else: When All Else Fails

# When No Path is Accessible The Fundammental Rules of the "else" Statement

is_daytime = False
is_raining = False

if is_daytime:
    print("Take the sunny path through the meadow!")
elif is_raining:
    print("take the rainy path through the marsh!")

# Think of else as a default statement if false for all
else:
    print("Neither paith is suitable right now. Use your and head back home!")

# Example 1. Weather Wardrobe Guide

is_raining = True
is_cold = False

if is_raining and is_cold:
    print("Wear a waterproof jacker and a Scarf!")
elif is_raining:
    print("Dont't forget your umbrella!")
else:
    print("Looks like a clear day, dress as you wish!")

# Example 2. Monthly Savings Calculator using calculations *****
income = 5000
expenses = 4500

savings = income - expenses
#500

if savings > 1000:
    print("Great job! You saved a lot this month.")
elif savings <= 0:
    print("Looks like you've spent all or more than you earned!")
else:
    print("Every little bit counts! Keep saving.")

#Example 3. Museum Entry Discounts

is_student = False
is_senior = False 

if is_student:
    print("You get a 50% student discount!")
elif is_senior:
    print("Seniors enjoy a 40% discount!")
else:
    print("regular entry fee applies")


#Example 4. Weekend Activity Planner
is_sunny = True
have_money = True

if is_sunny and not have_money:
    print("Great day for a walk in the park!")
else:
    print("Maybe consider indoor activities or saving for a sunny day outing.")

#Example 5. Game Character interaction
is_friendly = True
has_quest = False

if not is_friendly:
    print("Be caution! This character might not be helpful.")
elif has_quest:
    print("this character has quest for you!")
else:
    print("Just a regular villager passing by.")

#Example 6. Drive-Thru Order Suggestion
wants_veggie = True
like_spice = False

if wants_veggie and like_spice:
    print("How about a spicy veggie wrap?")
elif wants_veggie:
    print("Try our classic veggie burger!")
else:
    print("Check out our grill menu!")

#Topic:4 Exercises Hands-on coding!

# Exercise 1: Traffic Light Simulator
'''Write a program that prompts the user to input the color of a traffic light (red, yellow, green) and output the 
action a driver should take'''

light_color = input("Enter the traffic light color (red, yellow, green):")

if light_color == 'red':
    print("stop!")
elif light_color == 'yellow':
    print("Slow down and prepare to stop!")
else:
    print("Go!")

#Example Acceptable alternate
# elif light_color == 'green':
#     print("Go!")
# else:
#     print("Please enter in red, yellow, or green")


#My Answers

red = False
yellow = False
green = False

if red:
    print("Stop immediatly for traffic!")
elif yellow:
    print("Slow down for a stop!")
elif green:
    print("Look both ways and begin to drive!")
else:
    print("Traffic lights are down, proceed with caution!")

#Exercise 2: Movie Age Restriction
''' To ensure veiwer have an age - appropriate experience, movies come with specific ratings.
Given a movie's rating (G, PG, PG-13, R and the age of the person, inform the user if they can watch the movie 
based on their age)'''

age = int(input("Enter you age: "))
rating = input("Enter movie rating (G, PG, PG-13, R:")

if rating == "G":
    print("You can watch the movie!")
elif rating == "PG" and age >= 7:
    print("You can watch the movie!")
elif rating == "PG-13" and age >= 13:
    print("You can watch the movie!")
elif rating == "R" and age >= 17:
    print("You can watch the movie!")
else:
    print("You are not allowed to watch this movie")

# My Answers

age = int(input("What is your age?:"))
if 0 <= age < 13:
    print("Suitable only for G and PG movie!")
elif age < 17: 
    print("Suitable only for a PG-13, G and PG movie!")
elif age == 17:
    print("You can watch an R rated movie!")
else:
    print("Print you can watch R rated and NC movies!")
    


#Exercise 3: Weather Suggestion
''' Based on the temperature entered by the user, suggest an outfit to wear. Be creative!'''

temperature = float(input("Enter today's temperature in farenheit: "))

if temperature < 20:
    print("Wear a heavy coat and scarf!")
elif 20 <= temperature <= 50:
    print("It is a little chilly. Make sure to wear a light coat")
elif 51 <= temperature <= 70:
    print("It might good to wear a T-shirt and some long pants")
else:
    print("It feels great! This is T-shirt weather!")



#Exercise 4: Grading System
''' Convert number grades to letter grades. Asssume grades are between 0 to 100 
(Research academic grades values).'''

grade = float(input("Enter your grade (0-100):"))

if grade >= 90:
    print("Your letter grade is A.")
elif grade >= 80:
    print("Your letter grade is B.")
elif grade >= 70:
    print("You letter grade is C.")
elif grade >= 60:
    print("You letter grade is D.")
else:
    print("You letter grade is F.")

#Exercise 5: Fitness Advice
''' Ask the user how many minutes they exercise daily and provide health advice 
(be creative!).'''

exercise_minuties = int(input("How many minuties do you excercise daily?"))
if exercise_minuties < 30:
    print("You should consider exercising more for better health!")
elif 30 <= exercise_minuties <= 60:
    print("Great job staying active!")
else:
    print("You're an exercise superstar!")

#Exercise 6: Coffee Recommendation
'''Recommend a type of coffee based on user preferences about sweetness and milk'''
likes_sweet = input("Do you like your coffee sweet? (Yes/No): ")
likes_milk = input("Do you like Milk with your coffee? (Yes/No): ")

if likes_sweet == 'Yes' and likes_milk == 'Yes':
    print("How about a caramel latte?")
elif likes_sweet == 'No' and likes_milk == 'Yes':
    print("Try a black coffee with two sugar cubes.")
elif likes_sweet == 'Yes' and likes_milk == 'No':
    print("Try a black coffee with two sugar cubes.")
else:
    print("Black Coffee it is!") 


#Exercise 7: Library Book Return

''' 

Problem Statement:

you are tasked with creating a program for a libary to calculate fines for overdue books. 
The libary has the following fine structure:

* $1 per day for books that are up to 5 days overdue.
* $2 per day for books that are 6 to 10 days overdue. (7-5)2 + 5
* $5 per day  for books that are more than 10 days overdue. 12-5-10-10
((12-10)*5+15))

Write a Python program that:

1. Asks the user for the number of days a book is over. 
2. calculates the fine based on the above criteria.
3. Displays the fine amount to the user. 

Hint:
Use nested "if-elif-else" statements to determine the fine amount based on teh number of days the book is overdue.

'''

days_overdue = int(input("How many days is the book overdue? :"))
fine = 0


if days_overdue <= 5:
    fine = days_overdue * 1
elif days_overdue <= 10:
    fine = days_overdue * 2
else:
    fine = days_overdue *5

print(F"Your fine is ${fine}.")

#My Answer 
days_overdue = int(input("How many days is your book overdue? :"))

if days_overdue <= 5:
    print("Total fine Amount","$" + str(days_overdue * 1) )
elif 6 <= days_overdue <= 10:
    print("Total fine Amount","$" + str((days_overdue -5)*2+5))
    # (7-5)2 + 5
else:
    print("Total fine Amount","$" + str((days_overdue-10)*5+15))
    
# ''' Nested Example''' REVIEW AGAIN !!!!!

temperature = 20
if temperature < 25:
    print("It's a bit chilly!")
    if temperature < 15:
        print("Actually, you might need a coat.")

age = 17
if age >= 18:
    if age >= 21:
        print("You can drive and vote")
    else:
        print("You can drive and vote.")
else:
    print("You're too young to drive or vote.")


day = "Saturday"
time = "Morning"

if day == "Saturday":
    if time == "Morning":
            print("Time for cartoons!")
    elif time == "Evening":
        print("Maybe a movie night?")
    else:
        print("Relax and enjoy your day!")

''' Example 3. The Library: Book Genre and author'''

genre = "Fantasy"
author = "J.K.Rowling"


if genre == "Fantasy":
        if author == "J.k. Rowling":
            print("Time to visit Middle Earth!")
        elif author == "J.R.R. Tolkien":
            print("Time to visit Middle-Earth!")
        else: 
            print("Fantasy is a journey to another world!")

        '''Example 4. The Kitchen: Fruit and Ripeness'''
fruit = "Apple"
is_ripe = True
has_spots = False

if fruit == "Apple":
    if is_ripe and not has_spots:
        print("Perfect for a juicy bite!")
    elif not is_ripe and not has_spots:
        print("Let it ripen a bit more.")
    else:
        print("Might be best for apple pie!")
elif fruit == "Banana":
    if is_ripe and not has_spots:
        print("Ready to eat!")
    elif not is_ripe:
        print("Still a bit green.")
    else:
        print("Perfect for banan bread!")
else:
    print("Not sure about this fruits's ripeness.")

#Example 5. The Cinema Room:Movie and Genre

Movie= "Inception"
release_year = 2010 # Using an integer to represent the year
duration_minutes = 148 # Using an integer for the movie's duration_minutes

if movie == "Inception":
    if 2000 <= release_year <= 2020 and duration_minutes > 120:
        print("A modern classic with a runtime over 2 hours!")
    elif release_year < 2000:
        print("A gem from the past!")
    else:
        print(" A recent masterpiece!")
elif movie == "Titanic":
    if release_year == 1997 and duration_minutes > 180:
        print("A timeless love story!")
else:
    print("Enjoy the movie!")


product = "Kindle Paperwhite"
average_rating = 4.7 # Using a float to represnt the average star rating
number_of_reviews = 25000 # Using an integer for the number of reviews

if product == "Kindle Paperwhite":
    if average_rating >= 4.5 and number_of_reviews > 10000:
        print("A highly recommend product with numerous postive reviews!")
    elif average_rating >= 4.0 and number_of_reviews > 5000:
        print("A well-received product with a good number of reviews.")
    elif average_rating < 4.0:
        print("The product has mixed reviews. Consider reading detailed reviews before purchasing.")
    else:
        print("The product has a high rating but lacks a significant number of reviews.")

elif product == "Amazon Echo":
    if average_rating >= 4.5 and number_of_reviews > 15000:
        print("A top-rated smart speaker with a vast number of positive reviews!")
    elif average_rating >= 4.0 and number_of_reviews > 7000:
        print("A popular smart device with many satisfied customers.")
    elif average_rating < 4.0:
        print("The smart speaker has varied reviews. It might be worth checking out new models")
    else:
        print("The Echo has a commendable rating, but more reviews would provide better clarity.")

elif product == "Amazon Fire Stick":
    if average_rating >= 4.5 and number_of_reviews > 20000:
        print("A must-have for streaming enthusiast with overwhelming positive feedback!")
    elif average_rating > 4.0:
        print("A favorite among many for streaming, with a good numb of reviews.")
    elif average_rating < 4.0:
        print("The fire Stick has mixed feedback. Consdier other streaming options or newer models.")
    else:
        print("The fire Stick seems promising, but more reviews could offer a clearer picture.")
else:
    print("Please check the products's detailed review and ratings on Amazon.")

