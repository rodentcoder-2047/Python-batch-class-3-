print("Simple calculator")
x = float(input(">"))
y = float(input(">"))

print("sum", x + y)
print("diffrence", x - y)
print ("product", x * y)

if y == 0:
    print("division: cannot divide by zero")
else:
    print ("division", x / y)