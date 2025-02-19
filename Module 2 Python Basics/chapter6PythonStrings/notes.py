# '''
# Strings: The unalterable 
# '''
# #Original score, a string that says "Python":
# original_score = "Python"

# #Now, suppone we want to change the second letter to 'i' to spell  "Pithon"
# #If we try to change it directly like this:
# #original_score[1] = 'i' #This  will raise an error:TypeError

# # Instead, we start a new "game" by creating a new string:
# new_score = original_score[0]  + 'i' + original_score[2:] 
# #This will create a new string "Pithon"  that is a modified version of the original string "Python"
# # Now, new_score holds the value "Pithon" , but original_score is still  "Python".
# print(original_score) #This will print "Python"
# print(new_score) #This will print "Pithon"

# '''
# Indexing an Accessing Characters'''
# # Let's say we have a string that represents our team name:
# team =  "Coders"

# #The game of indexing starts with 0, so to acces the first character 'C'
# first_letter =[0]

# # To get the letter 'd', which is the third character,  we use index 2:
# third_letter = team[2]
# print(third_letter) #This will print 'd'
# print(first_letter) #This  will print 'c'

# '''Indexing and Acessing Characters: 
# '''
# # Let's say we have a string that represents  our teams name:
# team = "Coder"

# # The game of indexing starts with 0, so to acces teh firest character 'C':
# first_letter = team[0]
# # To get the letter 'd', which is the third character, we use index 2:
# third_letter = team[2]
# print(first_letter)  #This will print 'C'
# print(third_letter)  #This will print d

# #to get the last character 's' using negative indexing:
# last_letter = team[-1]
# #And if we want the second last character 'r':
# second_last_letter =  team[-2]
# print(last_letter) #This will print 's'
# print(second_last_letter) #This will print 'r'

# '''
# Iterating:
# '''
# # Our string is the track we're going to run on:
# track = "Marathon"

# #Let's runt the drill, interating  over each character in the track:
# for char in track:
#     print(char) # We'll print each character followed by a space
#     # Output: M a r a t h o n

# '''
# Iterating: Slicing:
# The Precision Play Video
# '''

# # Our string is the field, and we're going to make some precise plays:
# field = "Touchdown"
# #Let's execute a play where we only want "Touch":
# play_one = field[0:5]

# #Now, let's make a play for "down", starting form the 5th index to the end:
# play_two = field[5:]

# #What if we want to start from the third character and get every second character?
# play_three = field[2::2]

# print(play_one) # Output: Touch
# print(play_two) # Output: down
# #print(play_three)# Output:udon

# '''
# Combining Drills: Iteratin with Slicing 
# '''
# # Our string is the game plan:
# game_plan = "Execute play number"

# #Let's focus on the "play number 9" and iterate over just that part:
# for word in game_plan[8:]:
#     print(word, end=' ') #We'll print each character in the slice

#     #Output: p l a y  n u m b e r 9

# '''
# String Concatenation: The Passing Game Video
# '''

# #Our Strings are the players:
# quarterback =  "Tom Brady"
# receiver  = "Rob Gronkowski"
# play = " runs a route to catch the pass from "

# #Let's connect the play:
# complete_play = quarterback + play + receiver

# print(complete_play) # Output: Tom Brady runs a route to catch the pass from Rob Gron  

# '''
# String Formatting: The Chroeographed Celebration
# '''
# # Our string is the celebration plan:
# celebration = "{} scores a touchdown and does the {} dance!"

# #Let's fill in teh details:
# touchdown_celebration = celebration. format("Tom", "moonwalk")

# print(touchdown_celebration)
# #Out:Tom scores a touchdoen and does the moonwalk dance!

# #Our sting is the play call:
# player = "Tom"
# action = "touchdown"
# celebration_move = "moonwalk"

# # Let's execute the play with an f-string:
# play_call = f"{player} scores a {action} and does the {celebration_move}!"

# print(play_call)

# '''
# len() The Measuring tape
# '''
# # Our string is the playing field:
# field_length = "Football Field"

# #Let's measure it:
# field_size  = len(field_length)

# print(f"The length of the string is: {field_size}")
# # Output: The length of the string is: 14

# '''
# uppper() and lower(): The Unifkorm Adjusters 
# '''
# # Our string is a team chant:
# chant = "Let's go Sakura!"

# # Let's make it all uppercase for emphasis:
# loud_chant = chant.upper()

# # Or all lowercase if we're being stategic and quiet:
# quiet_chant = chant.lower()

# print(loud_chant) # Output: GO TEAM!
# print(quiet_chant) # Output: let's go sakura!

# '''
# replace(): The 
# Strategy Tweaker'''

# # Our string is the initial game plan:
# game_plan = "Attack from the left flank"

# print(game_plan)
# # Output: Attack from the left flank
# # The couch decides to change the plan:
# new_game_plan = game_plan.replace("left" , "right")
# print(new_game_plan)
# # Output: Attack from the right flank

# '''
# strip(): The Gear Cleaner
# '''
# # Our string has some unnescessary whitespace:
# player_name = "   Sakura   "
# # Let's clean it up:
# clean_name = player_name.strip()
# print(f"'{clean_name}' is ready to play!")
# # Output: 'Sakura' is ready to play!

# '''
# join() and split(): The Team Builders
# '''
# # Our string is a chant that we want to break into individual words:
# chant = "Here we go, team, here we go!"

# # Let's split the team:
# words = chant.split()

# #Now, let's bring it back together with a different rythm:
# new_chant  = "-".join(words)

# print(words)
# # Output: ['Here', 'we', 'go,', 'team,', 'here', 'we ', 'go!']
# print(new_chant)
# # Output: Here-we-go,-team,-here-we-go!

# '''
# The Seperator in split(): The couach's Whistle'''
# # Our string is a list of plays separated by commas:
# plays = "pass,run,block,kick"

# #The coach blows the whistle at each comma:
# individual_plays = plays.split(',')

# print(individual_plays)
# # Output: ['pass', 'run', 'block', 'kick']

# '''
# Exercise 1: The Book  Index Finder

# Instructions
# 1. Write a function 'find_character_index' that takes a 'text' string and a 'character' as parameters and returns teh index of the character in 
# the text. 
# 2. If the character is not found, the function should return a message stating that the character is not present.
# 3. Implement a loop that prompts the user to enter a string (representing a paragraph or line form a book) and a character to search for. 
# 4. Use the function to find the index of the character and  print the result using an f-string.
# 5. Ensure the program handles cases where the user may enter multiple characters instread of a single one.'''

# def find_character_index(text, character):
#     if len(character) == 1:
#         index = text.find(character)
#         if index == -1:
#             return f"The character  '{character}' is not present in the text."
#         else:
#             return f"The index of the character '{character}' is {index}"
#     else:
#         return f"Please enter a single character."   

# while True:
#     text_input = input("Enter a line of text from the book: ")  
#     char_input = input("Enter the character to find: ")

#     result = find_character_index(text_input, char_input)
#     print(result)  # Output: The index of the character 'a' is 2

#     continue_search  = input("Do you want to search again? (yes/no): ").lower()
#     if continue_search != 'yes':
#         break

# '''
# Exercise 2: The Echo Generator

# Develop a feature for a social media that allow user to create a fun echo effect with their text posts. 
# This reature repeats each character in the text to create an echo-like pattern, making the posts more engaging and visually
# appealing. 

# 1. Write a function 'generate_echo_text' that takes a 'text' string as a parameter and returns a new string with each character repeated twice.
# 2. Implement a loop that prompts the user to enter a string (representing a social media post or message)>
# 3. Use the function to generate the echo tect and print the result using an f-string.
# 4. Ensure the program handles empty strings and informs the user accordingly. 
# '''
# def generate_echo_text(text):
#     if text:
#         my_echo = [char*2 for char in text]
#         return "".join(my_echo)
#         print(my_echo)
#         # return ''.join([char * 2 for char in text])   # Alternative way to write the above line

#     else:
#         return "The input text cannot be empty. Please enter some to"
# while True:
#     user_input = input("Enter a message to create an echo effect: ")

#     echo_text = generate_echo_text(user_input)
#     print(f"Your echoed text is: {echo_text}")

#     continue_echo = input("Do you want ot create another echo text? (yes/no):").lower()
#     if continue_echo != 'yes':
#         break


# '''
# Exercise 3: The Game Highlight Reel
# You are developoing a feature for a sports app that allows users to input a series of game highlights and then displays each wevent sperately for eas reading and anylysis. 

# Instructions
# 1. Write  a function 'format_highlights' that takes a string of highlights spereated by commas and returns a list of individual plays.
# 2. Impl.ement a loop that promts the user to enter the stgring of highligts. 
# 3. Us the funtion to format the hightlights and print each play on a new line using an f-string. 
# 4. Ensure the program handles empty strings by informing trhe user an dasking for input again. 
# '''
# def format_highlights(highlight_string):
#     if highlight_string.strip():
#         return [play.strip() for play in highlight_string.split(',')]
#     else:
#         return []
    
# while True:
#         user_input = input("Enter the game highlights, separated by commas: ")
#         formatted_highlights = format_highlights(user_input)
        
#         if formatted_highlights:
#             print("Game highlights:")
#             for play in formatted_highlights:
#                 print(f"- {play}")
#         else:
#             print("No highlights entered. Please provide the highlights of the game.")
#         continue_input = input("Do you want to enter more highlights? (yes/no):").lower()
#         if continue_input != 'yes':
#              break

# '''
# Exercise 4: The Announcement Speaker
# Create a feature for public address system app that allows users to input a message  adn then displayus the message in uppercase,
# which represts the announcement mode.
# 1. Write a function 'announce_message' that takes a string and returns the same string in uppercase.
# 2. Implement a loop that prompts the user to enter their message. 
# 3. Use the function to convert the message and print it using an f-string.
# 4. Ensure the program handles empty string by informing the use and asking for input again.
# '''
# def announce_message(message):
#     return message.upper()

# while True:
#     user_input = input("Enter your message for the announcement: ")
#     if user_input.strip():
#           announcement = announce_message(user_input)
#           print(f"Announcemnet: {announcement}")
    
#     continue_input = input("Do you want to make another announcment? (yes/no): ").lower()
#     if continue_input != 'yes':
#          break

# '''
# Exercisse 5: The Personlized Welcome Mat

# You are developing a feature for a hospitality app tath personlizes the welcom experience for guests.
# The appt takes the guest's name as input and prints a welcome message, with the name beautifully cientered within a desing made of asterisks.

# Instructions:
# 1. Write a function 'create_welcome_message' that takes a string (the user's name) and returns a welcome message.
# 2. The welcom e message should have the user's name centere within a line of asteriks.
# 3. Use the function to generatge the welcome message and print it using an f-string. 
# 5. Ensure the program handle sempty or invalid name sby infomring the user and aksing for input again. 
# '''

# def create_welcome_message(name):
#      line_length = 100
#      centered_name = name.center(line_length, '*')
#      return f"Welcome {centered_name}) Welcome"

# while True:
#     user_name = input("Please enter your name for a personlized welcome message: ")
#     if user_name.isalpha():
#         welcome_message = create_welcome_message(user_name)
#         print(welcome_message)
#     else:
#         print("Invalid name. Please enter alphabetic  characters only.")
#     continue_input = input("Would you like to create another welcome message?  (yes/no): ").lower()
#     if continue_input != 'yes':
#          break


# '''
# Exercise 6: The stats Breakdown

# Create a feature for sports analytic app that catergorizes and displays players statistics.
# the app take a sing string input of varous stats separed by semicolons, where each stat is a category-value pair joned by a colon.
# The program should print each stat on a new line iwth its category and value clearly lableld.

# Intructions
# 1. Write a function 'print_stat' that takes a string of stats and prints each one on a new line. 
# 2. each stat should be presented in the format: " Category: [CATEGORY], Value: [Value]".
# 3. Implement a loop that prompts th euser to enter their stats string. 
# 4. Ensure the program handles invalid formats by informing the user and asking for input again. 
# '''
# def print_stats(stats_string):
#     stats_list = stats_string.split(';')
#     for stat in stats_list:
#         category_value = stat.split(':')
#         if len(category_value) == 2:
#             category, value = category_value
#             print(f"Category: {category}, Value: {value}")
#         else:
#             print(f"Invalid format for stat: {stat}")
#             break
# while True:
#     stats_input = input("Enter your stats separated by semicolons (e.g., 'Goals:4;Assists:2;Fouls:1'):")
#     print_stats(stats_input)

#     continue_input =  input("Would you like to enter another set of stats? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break


# '''Exercise 7:The Name Tag Switcheroo

# Develop a playful featuere for a social networking app that allows user to swap the firts and last character of their usernames. 
# The app takes a username as input and displays the modified version.

# 1. Write a function 'swap_characters' that takes a string and reaturns a new string with the first and last characters swapped.
# 2. Ensure the function handles usernames of any length, including sing-character names. 
# 3. Implement a loop that prompts the user to enther their username. 
# 4. Use the funtion to swap the characters and print the resut in a fun and engaging way. 
# 5. Provide the user with the option to try another username or exit the program. 
# '''

# def swap_characeter(username):
#     if len(username) > 1:
#         #coding ==> godinc
#         return username[-1] + username[0]
#     return username
# while True:
#     username_input = input("Enter your username to see the magic swap: ")
#     swapped_username = swap_characeter(username_input)

#     print(f"Ta-da! Your magical username is: {swapped_username}")
#     continue_input = input("Want to try another username? (yes/no):  ").lower()
#     if continue_input != 'yes':
#         break


# '''
# Exercise 8: The Meeting Agenda Reverser
# Develop a feature for a meeting managemnt app that allows users to reverse the order of items in their meeting agenda.
# The app accepts a string representing the angenda items in order an doupts them in reverse order. 

# 1. Write a function 'reverse_agenda' that takes a string of agnenda items and returns a string with the items in reversed order
# 2.  Implement a loop that prompts the user to enter their meeting agenda itmes separated by commas.
# 3.  Use the function to reverse the agenda items and print the result in a fun and engaging way.
# 4. Provide the user with the option ot enter a new agenda or exit the program. 
# '''

# def reverse_agenda(agenda_string):
#     #'gym, breakfast, work'
#     agenda_items = agenda_string.split(',')
#     # ['gym', 'breakfast', 'work']
#     #  ['work', 'breakfast', 'gym']

#     reversed_agenda = agenda_items[::-1]
#     # 'work,  breakfast, gym'

#     return ','.join(reversed_agenda)

# while True:
#     user_agenda = input("Enter your meeting agenda items separated by commas: ")
#     reversed_order  = reverse_agenda(user_agenda)

#     print(F"Reversed agenda order: {reversed_order}")
#     continue_input = input("Would you like to reverse another agenda? (yes/no): ").lower()
#     if continue_input != 'yes':
#         break
    

# '''
# Exercise 9: The Social Media Post Formatter

# In the world of social media, users often like to sytlize their posts with unique character replacements. 
# Task is to develop a feature for a social media app that allows users to replace every instance of the letter 'a' with '@' and 'e' with '3'

# 1. Write a function a Stylize_post' that takes a string and returns a stylized version of it according to the specified replacements.
# 2. Implement a loop tha tp rompts the user to enter their post.
# 3. Use the function to apply the stylization and print the result. 
# 4. Provide the user with the option to stylize a new post or exit the program. 

# '''

# def  stylize_post(post_string):
#     stylized_chars = []
#     for char in post_string:
#         if char == 'a':
#             stylized_chars.append('@')
#         elif char == 'e':
#             stylized_chars.append('3')
#         else:
#             stylized_chars.append(char)
#     return  ''.join(stylized_chars)

# while True:
#     #Hello all => H3llo @ll
#     user_post = input("Enter your social media post: ")
#     stylized_post = stylize_post(user_post)
    
#     print(f"Stylized post: {stylized_post}")
#     continue_input = input("Would you like to styl9ize another post?  (yes/no): ").lower()
#     if continue_input != 'yes':
#         break

'''Exercise 10: The Custom Repetion Message Generator
Task is to develop a feature for a user interface toolkit that allows users to repeat a string a specified number of times,
with each repetition separeated by a dash ('-'). 

1. Write a function 'repeat_message' that takes a string and number as argumetns and returns the repeated string pattern.
2. Implement a loop that prompts the user to enter their message and teh number of repetions.
3. Use the function to generate the repeated string pattern and print the result. 
4. Provide the user the option to create a new repeated string patern or exit the program. 

''' 
def repeat_message(message, times):
    return '-'.join([message] * times)

while True:
    user_message = input("Enter the message you want to repeat: ")
    repeat_count = int(input("How many times would like to repeat it? "))

    repeated_message = repeat_message(user_message, repeat_count)

    print(f"Repeated message: {repeated_message}")

    continue_input = input("Would you like to create another repeated message? (yes/no): ").lower()
    if continue_input != 'yes':
        break
