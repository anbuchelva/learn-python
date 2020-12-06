from art import logo
print(logo)
# Calculator

#Add
def add(n1,n2):
    result = n1 + n2
    return result

#Subtraction
def sutbtract(n1,n2):
    result = n1 - n2
    return result

#Multiply
def multiply(n1,n2):
    result = n1 * n2
    return result

#Division
def divide(n1,n2):
    result = n1 / n2
    return result

operations = {
    "+" : add,
    "-" : sutbtract,
    "*" : multiply,
    "/" : divide,
}

def calculator():
    should_continue = True
    num1 = float(input("Input the first number: "))
    while should_continue:
        for sign in operations:
            print(sign)
        operation_input = input("What operation do you like to do from the above list?: ")
        num2 = float(input("Input the second number: "))
        calc = operations[operation_input]
        output = calc(n1=num1,n2=num2)

        print(f"{num1} {operation_input} {num2} = {output}")
        should_continue_input = input(f"\nType 'y' to continue calculating with {output} or \ntype 'n' to start a new calculation or \ntype 'x' to exit.\n")
        if should_continue_input == "n":
            should_continue = False
            calculator()
        elif should_continue_input == "y":
            num1 = output
        elif should_continue_input == "x":
            should_continue = False

calculator()