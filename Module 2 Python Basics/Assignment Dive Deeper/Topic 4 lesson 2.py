# '''1. Decisions at the Crossroad
# Task 1: Code Correction You are provided with a Python script that uses conditional statements 
# to tell if a number is positive, negative, or zero, but it has some errors. Identify and fix them.

# Buggy Code:
#  '''

number = int(input("Enter a number: "))

if number > 0:
    print("The number is positive.")
elif number == 0:
    print("The number is zero.")
else:
    print("The number is negative.")

'''2. The Greatest Showdown
Task 1: Identify the Greatest Write a Python program that asks the user 
to enter three numbers. Your code should then identify and print out the largest number among the three.



 
'''
num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
num3 = float(input("Enter third number :"))
largest = num1
if largest < num2:
    largest = num2
if largest < num3:
    largest = num3
print(largest)


'''Task 2: Identify the Smallest Improve upon your code from Task 1
 to also determine the smallest number among the three and print it out. '''


num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
num3 = float(input("Enter third number :"))
smallest = num1
if smallest > num2:
    smallest = num2
if smallest > num3:
    smallest = num3
print(smallest)

num1 = float(input("Enter first number :"))
num2 = float(input("Enter second number :"))
num3 = float(input("Enter third number :"))

'''Expected Outcome: If we provide the numbers 3, 3, and 4, it should print out that 
"The smallest number is 3. The largest number is 4. '''

smallest = num1
if smallest > num2:
    smallest = num2
if smallest > num3:
    smallest = num3
print(smallest,"smallest number")
largest = num1
if largest < num2:
    largest = num2
if largest < num3:
    largest = num3
print(largest,"largest number")


'''
3.Leap Year Explorer3
Task 1: Leap Year Checker'''

year = int(input("Enter A Year: "))

if year % 400 == 0:
    print("It is a leap year")
elif year % 100 == 0:
      print("It is not a leap year")
elif year % 4 == 0:
    print("Leap Year it is!")
else:
    print("Not a Leap year!")