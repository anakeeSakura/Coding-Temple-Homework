''' Index is the key to accessing, modifiying, or even removing any specific item from your collection
number start at 0 and up  in a "list" and inside is the "item" '''

potions = [ "Healing", "Invisibility", "Strength"]
print(potions[0]) 
#This will ouput "Healing" Healing is at index 0, invisibilty is at index 1, and "Strenght"? It's at index 2!

favorite_potion = potions[1]
print(favorite_potion) # Output "Invisibility"

last_potion = potions[-1] 
#indexing access items from the end of the list. However, it might IndexError if an index is too big or doesn't exist
print(last_potion) #Output "Strenght" negative

#Counting Dublicates: If you want to know how many time a particular 
# item appears in the list, you can use the count()method. 

flowers= ["rose", "lily", "rose", "daisy", "lily"]
print(flowers)

rose_count= flowers.count("rose") 
print(rose_count) 

# Removing Duplicates: Use hte remove() method to delete an item. It would only remove the first occurence

flowers.remove("lily")

print(flowers) 
# only the first lily vanishes. 

# Dynamic Additions

hobbies =["reading","painting","cycling"]
print(hobbies)

#Appending items adds it to last of the list not effecting the order. 
hobbies.append("singing")
print(hobbies)
#Inserting items into a specific index and updating the order. 
hobbies.insert(1, "dancing")
print(hobbies)

#Modifying Existing values. hobbies[0] accesses the first item in the hobbies list (which is "reading")

hobbies[0]= "writing"
print(hobbies)

# Taking items Out
hobbies.remove("cycling")
print(hobbies)

#Removes the last hobby in the list
last_hobby = hobbies.pop()
print(last_hobby)

#Removes the item at index 1, 
# e.g., "dancing"
second_hobby = hobbies.pop(1)
print(second_hobby)


# Exploring & Finding
count_reading = hobbies.count("writing")
print(count_reading)


position_painting = hobbies.index("painting")
print(position_painting)

# Clearing the list use the clear()method. The method empties the list, 
# leaving it blank but still available for future use.

hobbies.clear()
print(hobbies)


# Built in Methods The Wizard's Toolkit

# Sort your items 

fruits = ["banana", "apple", "cherry"]
fruits.sort()
#This arrange the fruits in alphabetical order. 
print(fruits)

# If you want to know how many items are in your list, Python provides a simple way to find out
# using the len()function.  Returns the total number of items in the list. 

count = len(fruits)
print(count)


# Reverse the order of your list

numbers = [1,2,3,4,5]
numbers.reverse() # This turns the list around.
print(numbers)


''' List Methods
append()  Adds an element at the end of the list
clear()	  Removes all the elements from the list
copy()	  Returns a copy of the list
count()	  Returns the number of elements with the specified value
extend()  Add the elements  a list (or any iterable), to the end of the current list
index()	  Returns the indexof of the first element with the specified value
insert()  Adds an element at the specified position
pop()	  Removes the element at the specified position
remove()  Removes the item with the specified value
reverse() Reverses the order of the list
sort()    Sorts the list'''


# The Role of len() returns the number of items in an object.

hobbies  = ["painting", "reading", "swimming"]
print(len(hobbies)) # output: 3

# The Magic of -1
last_index  = len(hobbies) - 1 
print(last_index) # output: 2

last_hobby= hobbies[last_index]
print(last_hobby) # output: swimming

# Variable elements like a map showing  the index of each element in the list.

hobbies  = ["painting", "reading", "swimming"]
print(hobbies)
# output: ['painting', 'reading', 'swimming']

# Variable Indexing 
# You can store this position in a variable  and use it to access the element at that position. 

position = 1 
mystery_hobby = hobbies[position]
print(mystery_hobby) # output: reading

# Dynamic Access with Variables by changing the value of the position variable, 
#  you can change the element that is accessed.

position = 0
mystery_hobby = hobbies[position]
print(mystery_hobby)
# output: painting

# Accessing Elements by a calculated Approach
# Index mathematical/logical expression://

middle_index = len(hobbies) //2
middle_hobby = hobbies[middle_index]
print(middle_index)
# output: 1


# Merging  lists using the + operator

fruits  = ["apple", "banana", "cherry"]
vegetables = ["broccoli", "carrot", "cucumber"]
print(fruits + vegetables)
# output: ['apple', 'banana', 'cherry', 'broccoli', 'carrot,  'cucumber']

# The copy method  is used to create a copy of a list.

fruits_clone = fruits.copy()
print(fruits_clone)
# output: ['apple', 'banana', 'cherry']

# Joining lists with the extend method
# The extend method is used to add all the elements of a list to another list.
# It does not return a new list, but instead modifies the original list.
fruits.extend(vegetables)
print(fruits)
# output: ['apple', 'banana', 'cherry', 'broccoli', 'carrot',  'cucumber']

# The join method
# The join method is used to join all the elements of a list into a string. It takes an
# iterable as an argument and returns a string in which the elements of the iterable
# are joined by the string on which the join method is called.
story_elements =  ["Once upon a time", "in a land far, far away", "there was a beautiful princess"]
story =  " ".join(story_elements)
print(story)
# output: Once upon a time in a land far, far away there was a beautiful princess

# Slicing 
# Slicing is a way to extract a subset of elements from a list. It is done by
# specifying the start and end indices of the subset, separated by a colon.
# The start index is inclusive, while the end index is exclusive.
# If the start index is omitted, it defaults to 0. If the end index is omitted
# it defaults to the length of the list.

# The colon: acts as a separator between the start and end indices.
# The start index is inclusive, while the end index is exclusive.
# If the start index is omitted, it defaults to 0. If the end index is omitted
# it defaults to the length of the list.

# Second and  third elements of the list
hobbies =  ["reading", "swimming", "cycling", "dancing"]
segment =  hobbies[1:3]
print(segment)
# output: ['swimming cycling']

# From the beginning
beginning_to_third = hobbies[:3]
print(beginning_to_third)
# output: ['reading', 'swimming', 'cycling'] Unveils 0-2


# till the end
third_to_end = hobbies[2:]
print(third_to_end)
# output: ['cycling', 'dancing']

destination = "Paris"
duration =  7
budget  =  5000
place_to_visit = ["Eiffel tower", "Louvre museum, Arc de Triomphe", "Notre Dame cathedral", "Montmartre"]
food_to_try = ["Crossant",  "Croque Monsieur", "Escargot"]

itinerary  = [destination, duration, budget,place_to_visit,  food_to_try]

itinerary[3].append("Champs-Elysees")
itinerary[4].append("Ratatouille")

print(f"destination:  {itinerary[0]}")
print(f"duration:  {itinerary[1]} days")
print(f"budget:  ${itinerary[2]}")
print(f"place_to_visit: {', '.join(itinerary[3])}")
print(f"food_to_try:  {', '.join(itinerary[4])}")














# # Python Regex notes from workshop

# results = re.search (r'\d', 'The house number is 1234')
# print(result.group()) # prints 1


# results = re.findall(r'\d+, 'The kinda ka Rollercoaster is 456ft high and reaches up to 128mph')

# print(results) # prints ['4', '5', '6', '1', '2',


# email_string = 'my emal for coding temple is: csachs@ct.com'
# email_pattern = r'[a=z]+@\D+.\D+'
# result = re.search(email_pattern, email_string)
# print(result)