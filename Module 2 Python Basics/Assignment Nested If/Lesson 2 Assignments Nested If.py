
'''1. Nested Decisions: The Adventure Game 
Task 1: Code Correction You are provided with a Python script that is supposed to guide a 
user through an adventure game, but it has some errors. Identify and fix them. 

Buggy Code:''' 


place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
elif place == "cave":
    print("You find a hidden treasure!")


# the_input = input("ENTER SOME TEXT")
# if(the_input.upper()== "PANDAS"):
#     print("you entered", the_input.upper())


'''Task 2: Setting the Scene 
Based on your corrected code from Task 1, expand the game. 
If the user chooses "cave", ask them if they want to "light a torch" 
or "proceed in the dark", and provide outcomes for each decision.
Task 3: Default Path

If the user makes an invalid choice at any point, 
incorporate a pass statement to handle it. HINT: How can an else statement be of use here?'''

# action = input("Do you want to light a torch or proceed in the dark? ")
# elif place == "cave": 

place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        print("Choose from the choices!")
elif place == "cave":
    print("You find a hidden treasure!")
    action = input("Light a torch or proceed in the dark?")
    if action == "Light a torch":
        print("You found a hidden treasure!")
    elif action == "proceed in the dark":
        print("You fell in to a trap!")
    else:
        print("Error, please choose from the choices!")
else:
    print("Game Over")

'''2. Quick Decisions: The Event Planner 
Task 1: Code Correction You are provided with a Python script that is 
supposed to help in event planning, but it has errors. Identify and fix them.'''

attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

'''Task 2: Venue Selection

Based on the corrected code from Task 1, further enhance your code to recommend 
additional things like "audio system" or "projector" based on the number of attendees.'''

attendees = int(input("Enter number of attendees: "))
venue = "large hall and audio sytem" if attendees > 100 else "conference room and projector"
print(venue)
if attendees > 100:
        print("an audio system and projector is reccomended for presentations and better sound")
elif attendees < 100:
    print("Please consider an audio system for better projected sound")

'''Task 3: Catering Choices

Ask the user if they want "vegetarian" food. 
Recommend "Veggie Delight Caterers" if yes, otherwise recommend "Gourmet Meals Caterers".'''

customer_order = input("Would like a vegetarian dish?:Yes/No ? ")
if customer_order == "Yes":
    print("I recommend a Veggie Delight")
else:
    print("I would reccomend a savory Gourment Meals Caterers")  