def calculator(number1, number2, operator):
    """this function computes a certain operation on two numbers based on
    input from user

    Parameter:
    number1: given as a string, the first input from second function
    and is first number to be operated on
    number2: given as a string,  the second input from second function
    and is second number to be operated on
    operator: string specified math operator given from user

    Return:
    float - result of specified computation from
    """

   
    "have to cast since arguments are strings right now"
    number1 = float(number1)
    number2 = float(number2)

    "series of elif statements to compute specified operator"
    if operator == "+":
        print(number1 + number2)
    elif operator == "-":
        print(number1 - number2)
    elif operator == "*":
        print(number1 * number2)
    elif operator == "/":
        print(number1 / number2)
    elif operator == "//":
        print(number1 // number2)
    elif operator == "**":
        print(number1 ** number2)
    else:
        quit()


'''this function takes input from the user in order to use those
parameters for the calculator function'''
def input_output():
    "to get data from user"
    num1 = input("Enter the first number: ")
    num2 = input("Enter the second number: ")
    op = input("Enter the operation: ")

    "give these inputs to the calculator function to compute"
    calculator(num1, num2, op)

    "hw example shows a line after result and asking to continue"
    print("")

    "determine if user wants to continue or not"
    response = input("Do you wish to exit? ")
    if response == 'n':
        input_output()
    else:
        quit()

"used for testing"
input_output()
