
from process_expression import *

def main():
    # Instructions for the user:
    print("Hello! Welcome to the calculator!")
    print("Please enter a math expression and you will get the result within seconds!")
    print("If you would like to quit, just type quit!")
    while True:
        expression = input("Your expression: ")
        if expression.strip().lower() == "quit":  # Checking if the user inserted "quit"
            print("Goodbye, thank you for using!")
            break
        try:
            tokens = check_full_validation_of_expression(expression)
            postfix_expression = infix_to_postfix(tokens)
            result = postfix_calculation(postfix_expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print("The result is:", result)
        except Exception as e:
            print("Error:", e)
            print("Traceback:")

if __name__ == "__main__":
    main()