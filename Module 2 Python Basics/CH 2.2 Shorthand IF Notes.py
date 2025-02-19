# Explaining the shorthand If's code Shorthand If's code

''' Shorthand if is best used when the conditions and outcomes are simple and can be expressed in a single line. 
For more complex conditions, traditional if statments are recommended '''

x, y = 5, 10
print("x is greater") if x > y else print ("y is greater")   

# Example 1. Quick Weather 
weather = "sunny"
activity = "beach" if weather == "sunny" else "indoor games"
print(activity)

# Example 2. Quick Beverage Choice

hour_of_day = 7 #Using an integer to represent the hour in 24- hour format
energy_level = 3 # Using an integer on a scale of 1 to 5, where 5 is very energetic

beverage = "coffee" if (6 <= hour_of_day < 12) and energy_level < 4 else "tea"
print(beverage) #Outputs: coffee

# Example 3. Quick Workout Routine
energy_level = 4.5 # Using a float on a scale of 1.0 to 5.0, where 5.0 is very energetic
time_available = 30.5 # Using a float to represent munutes available for workout
short_on_time = time_available < 45.0

workout = "intense cardio" if energy_level > 4.0 and not short_on_time else "light yoga"
print(workout) # Outputs: light yoga

# Example 4. Quick Meal Choice
current_hour = 15 # Using an integer to represent the hour in 24-hour format 
hunger_level = 7 # Using an integer on a scale of 1 to 10 is extremly hungry

meal = "snack" if current_hour < 17 and hunger_level < 5 else "full meal"
print(meal) # Outputs: full meal

#Example 5. Quick Vacation spot

Loves_beach = True
budget = 1500 # Intial budget in dollars
high_budget = budget >= 2000

destination = "beach resort" if Loves_beach and not high_budget else "luxury mountain " 
budget -= 500 if destination == "beach resort" else 1000 # Compound assignment

print(destination) # Outputs: beach resort
print ("Remaing budget:", budget) # Outputs: Remaining budget: 1000

#Example 6. Quick Study method

topic_diffuculty = "hard"
available_hours = 3.5 # Using a float to represent hours available for study
understanding_level = 6 # Using an int on a scale of 1 to 10, where 10 is full understanding

study_method = "deep dive" if topic_diffuculty == "hard" and available_hours > 2.5 else " quick review"
bonus_hours = 1.5 if understanding_level < 5 else 0.5 
# Compound assignment
available_hours += bonus_hours # Add monus hours to avaialbe hours

print(study_method) # Outputs: deep dive
print("Total study hours:", available_hours)
#Outputs : Total study hours: 4.0