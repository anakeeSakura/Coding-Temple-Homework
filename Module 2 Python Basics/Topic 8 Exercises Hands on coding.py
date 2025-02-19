# Excercise 1. The Movie night decesion

''' you are developing a feature for a movie steraming that suggest a movie genre to user based on their current mood and the 
the days's weather. The platform has th efollwing a recommentdation criteria:

- If the user is feeling "happy" and the weather is "sunny, recommend a "comedy.
- If the user is feeling "happy" but the weather is not "sunny, recommend a "romantic" movie.
- If the user is feeling "sad",  recommend a "Drama".
- For any other mood, recommend an "Adventure" movie.

Write a Python program that:

1. Ask the user about their current mood (happy/sad/adventurous).
2. Ask the user about the day's weathe (sunny/rainy).
3. Determines the movie genre based on the above criteria. 
4. Displays the reccommended movie genre to the user. 

**Hint**:
Use nested 'if' statements to determine the movie genre based on teh user's mood and the day's weather. 

'''
mood = input("How are you feeling  today?) (happy/sad/adventurous):")
weather = input("What's the weather like? (sunny/rainy):")

if mood == "happy":
    if weather == "sunny":
        print("comedy")
    else:
        print("Romantic")
elif mood == "sad":
    print("Drama")
else:
    print("adventure")


# Excercise 2 Quick Temperature Check

'''
You are programing a smarth wardrobe assistant that suggests outfits to users based on the day's temperature and the type of event they 
are attending. The wardrobe has the following recommendation criteria:

-If the temperature is below 15c or 59F and the event is "formal", suggest a "Warm formal suit".
-If the temperature is below 15c or 59F but the event is "casual", suggest a "Cozy sweater and jeans".
-If the temperature is below 15c or 59F and the event is "formal", suggest a "Light formal suit".
-For any other combination, suggest a "T-shirt and shorts". 

Write a python program that:
1. Asks the user about the day's temperature in Celsius or Fahrenheit.
2. Ask the user about the type of event they are attending (formal/casual).
3. Determines the outfit based on the above criteria. 
4. Displays the recommened outfit to the user. 

'''

temperature = float(input("What's the temperature today in Fahrenheit?"))
event_type = input("What type of event are you attending? (formal/casual):")

if temperature < 59:
    if event_type == "formal":
        print("warm formal suit")
    else: 
        print("Cozy sweater and jeans")
elif temperature >= 59:
    if event_type == "formal":
        print("light formal suit")
    else:
        print("T-shirt and shorts!")

# Exercise 3. Student Discount Eligibilty 
'''A school offers various discounts to its students based on their academic performance and participation in extracrrucular
activities. The discount criteria are a s follow:
- Students with a grade of 'A' and who are also part of the schools's sports team get a 20% discount.
- Students with a grade of 'A' but not in a  sports team get a 10% discount. 
- Students with a grade of 'B' and who are  part of the schools's drama club get a 15% discount. 

Write a Python program that:

1. Asks the user for their grade (A/B/C). 
2. Asks if they are part of the sports team (yes/no)
3. Asks if they are part of the drama club (yes/no).
4. Determines the discount percentage based on teh above criteria. 
5. Displays the discount percentage to the user. 

**Hint**:
Use nested 'if' statements to determine the discount percentage based on the student's greade and extracurricular 
activities.'''

grade = input("Enter your Grade (A,B,C): ")
sports_team = input("Are you part of the sports team? (Yes/No): ")
drama_club = input("Are you part of the drama club? (yes/no): ")

discount = 0

if grade == 'A':
    if sports_team == 'yes':
        discount = 20
    else:
        discount = 10
elif grade == 'B':
    if drama_club == "yes":
        discount = 15
    print(f"you are elgible for a {discount}%")

# Exercise 4 Quick Age Check
''' If the player's age is 18 or above, display "you can drive!"
    If the player's age is below 18, display "not yet!" 
Write a Python program that:

1. Asks the user for their age. 
2. Determines if the user is old enough to access the games based on the above criteria. 
3. Displays the appropriate message to the user. 
**Hint**
Use the shorthand 'if' statement to determine the message based on the user's age. 
'''
age = int(input("How old are you?"))
#if age >= 18:
    # print("You can drive!")
# else:
#     print("Not yet!")

print("You can drive!") if age >= 18 else print("Not yet!")


# Exercise 5. Nested Food Choice 

''' - If the customer prefers a vegetarian meal and wants it sugar-free, suggest a "Fruit salad".
    - If the customer prefers a vegetarian meal but doesn't want it sugar-free, suggest a "veg cake".
    - If the customer prefers a non-vegetarian meal and wants it sugar-free, suggest a "Sugar-free ice cream".
    - For any other combination, sugget a "Chocalate brownie". 

    Write a Python program that:
    1. Asks the user about their meal type preference (ven/non-veg).
    2. Ask the user about their dietary preference (sugar-free/regular).
    3. Determines the dish based on teh above criteria. 
    4. Displays the recommneded dish to the user. 

    **Hint**
    Use nested 'if' statements to determine the dish based on teh user's meal type and dietary preference. 
    '''

meal_type = input("Do you prefer veg or non-veg?")
dietary_preference = input("Do you want sugar-free or regular? ")

if meal_type == "veg":
    if dietary_preference == "sugar-free":
        print("Fruit Salad")
    else: 
        print("Veg cake")
else:
    if dietary_preference == "sugar-free":
        print("Sugar-free ice cream!")
    else:
        print("Chocolate Brownie")



