'''
1. Exceptional Weather Forecast
Objective: The aim of this assignment is to enhance your understanding of exception handling by creating a weather forecast application that gracefully handles unexpected user input and provides user-friendly error messages.

Task 1: Start Begin by asking the user to enter the temperature in Fahrenheit.

Task 2: Temperature Conversion Write a function that converts the Fahrenheit temperature to Celsius. Remember that the formula is (Fahrenheit - 32) * 5/9.

Use a try block to catch any potential errors during the conversion process. What happens if they type out "thirty" instead of doing 30?

'''

def  convert_to_celsius(fahrenheit):
    return  (fahrenheit - 32) * 5/9

def main():
        try:
            fahrenheit = float(input("Please enter the temperature in Fahrenheit: "))
            celsius = convert_to_celsius(fahrenheit)
        except:
            print("Invalid input. Please enter a valid number.")
        else:
            print(f"The temperature {fahrenheit} degrees Fahrenheit is: {round(celsius, 2)} degrees Celsius")
        finally:
            print("Thank you for using our weather forecast application!")
main()


    
    


