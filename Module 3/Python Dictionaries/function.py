

# # def say_hello():
# #     print("Hello!")
# #     x = 30
# #     y = 44

# # say_hello()

# def hello_sakura():
#     return 'a'

# hello_return_value = hello_sakura()
   
# print(hello_return_value) 

# def add_two_numbers():
#     return 5 + 7
# print(add_two_numbers())   # Outputs: 12

# def mulitply_two_numbers():
#     return 5 * 7
# print(mulitply_two_numbers())  # Outputs: 35

# def divide_two_numbers():
#     return 10 / 2
# print(divide_two_numbers())  # Outputs: 5.0


def divide_two_numbers():
    print(10 / 2)  # Outputs: 5.0
    # Outputs: 5.0
divide_two_numbers() 
  


# def add_by_three(num1):
#     return num1 + 3


# results= add_by_three(1) # Outputs: 8
# print(results)

# def add_by_four(num1):
#     return num1 + 4

# the_number = int(input("Enter number: "))
# return_value = add_by_four(the_number) # Calling the metod and storing the result in return_value 
# print(return_value)

# def multiply_by_three(num1):
#     return num1 * 3

# input_number = int(input("Enter number: "))
# multiplication_answer_return_value = multiply_by_three(input_number)
# print(multiplication_answer_return_value) # Calling the method and storing the result in multiplication_answer_return_value

# def adding_two_numbers(num1, num2, num3):
#     return num1 + num2 * num3

# input_sum = int(input("Enter first number: "))
# addition_return_value = adding_two_numbers(input_sum, 10, 10000)
# print(addition_return_value) # Outputs: 20

"""create a dictionary
ask user which key they want
print the value of that key"""

pokemon = {"fire": "charizard", "water": "squirtle", "grass": "bulbasaur ", "electric": "pikachu", "ice": "articuno"}
# key = input("Enter a key: ")
# print(pokemon[key]) # Outputs: charizard

def get_pokemon(element, pokemon):#Accessing the value the user wants to input
    return pokemon[element]

user_pokemon = input("Enter the element type of your pokemon: ")
who_that_pokemon_return_value = get_pokemon(user_pokemon, pokemon)
print(who_that_pokemon_return_value)


