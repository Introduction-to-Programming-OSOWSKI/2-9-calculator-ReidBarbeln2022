def calculate(p, x, y):
    if p == "add":
        return x + y
    elif p == "subtract":
        return x - y
    elif p == "multiply":
        return x * y
    elif p == "divide":
        return x / y

print(calculate("subtract", 5, 5))