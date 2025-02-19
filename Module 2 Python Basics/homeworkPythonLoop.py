

'''
1. The Range Riddle

Task 1: Your Mood Today Write a program that prints off different moods for 
each day of the week. Create a list of moods such as "Happy", "Sad", "Energetic", 
and "Calm". Using the range() function, loop through every day of the week and 
for each day, randomly select a mood from the list and print it. 
Ensure that your program includes the use of the random module to select the mood.
'''
import random
moods =  ["Happy", "Sad", "Energetic", "bored"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
for day in days_of_week:
    mood = random.choice(moods)
    print(f"Today is {day} and I'm feeling {mood}.")

'''
2. Double Scoop with Nested Loops '''

import random
moods = ["Happy", "Sad", "Energetic", "bored"]
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
times_of_day = ["Morning", "Afternoon", "Evening"]

for day in days_of_week:
    print(f"Mood Diary for {day}:")
    for time in times_of_day:
        mood = random.choice(moods)
        print(f"{time}: Feeling {mood}")





