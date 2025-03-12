# Basic Calculator Program
def get_valid_number(prompt):
    """Helper function to repeatedly ask for a valid number input to ensure we reduce the error that a reader cannot understand."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a valid number.")
def simple_calculator():
    stop_calculator = False

    while not stop_calculator:
        first_value = get_valid_number("What is the first value? ")
        second_value = get_valid_number("What is the second value? ")
        symbol_operation = input("Do you want to add, subtract, multiply, or divide?, please type it. ").lower()
        if symbol_operation == "add":
            answer = first_value + second_value
            print (answer)
        elif symbol_operation == "subtract":
            answer = first_value - second_value
            print(f'The answer is {answer}')

        elif symbol_operation == "multiply":
            answer = first_value * second_value
            print(f'The answer is {answer}')

        elif symbol_operation == "divide":
            if first_value == 0 or second_value == 0:
                print("Cannot divide by a number by zero")
            else:
                answer = first_value / second_value
                print(f'The answer is {answer}')
        else:
            print("Please input the correct symbol")
        while True:  # we want to keep asking until the user enters "yes" or "no"
            answer = input("Do you want to continue? yes or no? ").lower()
            if answer == "yes":
                break  # Break out of this loop and restart the calculator loop to start asking the same question
            elif answer == "no":
                stop_calculator = True
                break  # Exit both loops
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")


simple_calculator()