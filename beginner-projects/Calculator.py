
def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    if n2 == 0:
        return "Error: Division by zero is not allowed."
    return n1 / n2

operations = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}

def calculator():
    should_continue = True
    num1 = float(input("Enter the first number: "))
    while should_continue:
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation from the line above: ")
        num2 = float(input("Enter the second number: "))
        
        calculation_function = operations[operation_symbol]
        answer = calculation_function(num1, num2)
        
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        
        if input("Type 'y' to continue calculating with the current answer, or 'n' to start a new calculation: ").lower() == 'y':
            num1 = answer
        else:
            should_continue = False
            calculator()

calculator()