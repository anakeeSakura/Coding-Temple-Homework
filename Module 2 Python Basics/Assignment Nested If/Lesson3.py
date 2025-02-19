'''Lesson 3: Assignments: Python Lists'''

# Task 1: Given the list of grades:

grades = [85, 90, 78, 88, 76, 95, 89, 80, 72, 93]
grades.sort()    
grades.reverse()
print(grades)

# '''Task 2: Calculate the average grade and print it.''' 
average_grade = sum(grades) / len(grades)
print(average_grade)

# 2. Advanced List Methods and Identity Operators

# Task 1: Given the two lists:

submitted = ["Alice", "Bob", "Charlie", "David"]
attended = ["Charlie", "Eve", "Alice", "Frank"]

if "Alice" in submitted and "Alice" in attended:
    print("Alice is both submitted and attended")

# 3. Advanced slicing Techniques

# Task 1: Given the list of temperatures:
temperatures = [72, 75, 78, 79, 80, 81, 82, 83, 85, 86, 87, 88, 89, 90, 91, 92,  93, 94, 95, 96, 97, 98, 99, 100, 101, 102, 103, 104, 105, 106]

# Extract Extract the temperatures for the second week (7 days) of the month (index 7 to index 14).
second_week_temps = temperatures[7:14]
print(second_week_temps)

#Task 2: Extract all the temperatures above 100. HINT: add the temperatures over 100 to a new list, or use list slicing to get the temperatures.
temperatures_over_100 = temperatures[-1:-7:-1]
print(temperatures_over_100) 


