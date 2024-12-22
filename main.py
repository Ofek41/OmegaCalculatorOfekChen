from process_expression import *

def main():
    # Instructions for the user:
    print("Hello! Welcome to the calculator!")
    print("Please enter a math expression and you will get the result within seconds!")
    print("If you would like to quit, just type quit!")
    while True:
        try:
            expression = input("Your expression: ")
            if expression.strip().lower() == "quit":
                print("Goodbye, thank you for using!")
                break
            tokens = check_full_validation_of_expression(expression)
            postfix_expression = infix_to_postfix(tokens)
            result = postfix_calculation(postfix_expression)
            if isinstance(result, float) and result.is_integer():
                result = int(result)
            print("The result is:", result)
        except Exception as e:
            if isinstance(e, EOFError):
                print("Ctrl + Z is not supported")
            else:
                print("Error:", e)
        except KeyboardInterrupt:
            print("\nProgram has been closed")
            break

if __name__ == "__main__":
    main()