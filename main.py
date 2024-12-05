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
    expression = input()
    postfix_expression = infix_to_postfix(expression)
    result = postfix_calculation(postfix_expression)
    print("The result is:", result)

if __name__ == "__main__":
    main()