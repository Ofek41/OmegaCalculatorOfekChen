# Importing my modules:
from operators import *
from custom_exceptions import *
from implementing_custom_exceptions import *
from parsing_expression import *
from process_expression import *
from operators_config import OPERATORS

def main():
    print("Hello! Welcome to the calculator!")
    print("Please enter a math expression and you will get the result within seconds!")
    print("If you would like to quit, just type exit!")
    while True:
        expression = input("Your expression: ")
        if expression.strip().lower() == "exit": # Checking if the user inserted "exit"
            print("Goodbye, thank you for using!")
            break
        try:
            # Converting the exp from infix to postfix:
            postfix_expression = infix_to_postfix(expression)
            # Calculating the result based on postfix exp:
            result = postfix_calculation(postfix_expression)
            # Checking if the result is int or float:
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print("The result is:", result)
        except Exception as e: # If an error was raised, present it.
            print("Error: ", e)

if __name__ == "__main__":
    main()