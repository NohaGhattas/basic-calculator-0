def basic_calculator(a, b, operation):
    if a.isnumeric() and b.isnumeric():
        a = float(a)
        b = float(b)
        
        if operation == "subtract":
            result = a - b
        elif operation == "divide":
            result = a / b
        elif operation == "add":
            result = a + b
        elif operation == "multiply":
            result = a * b
        else:
            result = "Operations supported: add, subtract , divide, multiply only"
    else:
        result = "Please enter a valid number for a and b"
    return result