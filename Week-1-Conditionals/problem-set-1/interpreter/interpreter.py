# Prompt user for input
userInput = input("Expression: ")

# Using split functon to split enitre input by space seperaated values
expression = userInput.split(" ")

# Assigning each variable their value as homework suggested
x = round(float(expression[0]), 2)
y = expression[1]
z = round(float(expression[2]), 2)

# Find which operation does we hande to and print result
match y:
    case "+":
        print((x + z))
    case "-":
        print((x - z))
    case "*":
        print((x * z))
    case "/":
        if z == 0:
            print("You can not divide number on zero!")
        else:
            print((x / z))
