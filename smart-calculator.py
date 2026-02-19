import math
print("Smart Calculator")
print("Type 'exit' to exit the program")

def square(x):
    return x*x

def cube(x):
    return x*x*x

def sqrt(x):
    return math.sqrt(x)

def sin(x):
    return math.sin(x)

def cos(x):
    return math.cos(x)

def tan(x):
    return math.tan(x)


while True:
    expr = input("\n enter calculation: ")
    if expr == "exit":
        break
    try:
        result = eval(expr)
        print("Result: ", result)
    except:
        print("Invalid expression")
