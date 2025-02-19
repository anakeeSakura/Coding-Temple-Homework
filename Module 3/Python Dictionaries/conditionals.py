
# the_condition = "dfdasdf"
# power_on = False

# if (the_condition == True):
#     print("The condition is true")
#     x = 5
#     b = 10
#     if(power_on == True):
#         print("Power is on")
# elif (the_condition == False):
#     print("The condition is false")
#     if(power_on == True):
#         print("Power is on")
# elif (the_condition == "dfdasdf"):
#     print("The condition is a string")
#     if(power_on == True):
#         print("Power is on") 
# else: 
#     print("This will always run if the condition is not true or false")


''''Accept a grade between 51 and 100 and converted to a letter grade using if else statements'''

score = int(input("Enter your score: "))

if (score >= 90): 
    print("A")
elif (score >= 80):
    print("B")
elif (score >= 70):
    print("C")
elif (score >= 60):
    print("D")
else:
    print("F") 


number = int(input("Enter a number: "))
print(number % 2)
if (number % 2 == 0):
    print("The number is even ")
elif (number % 2 == 1):
    print("The number is odd ")

# Accept the number from user and check if its between 1 and 50

number_guess = int(input("Guess a number between 1 and 50: "))
if (number_guess >= 1 and number_guess <= 50):
    print("Your number is between 1 and 50")
    if (number_guess % 2 == 0):
        print("The number is even ")
    elif (number_guess % 2 == 1):
        print("The number is odd ")
else:
    print("Your number is not between 1 and 50")