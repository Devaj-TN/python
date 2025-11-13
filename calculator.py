def add(a,b):
    return a + b
def sub(a,b):
    return a - b
def multiply(a,b):
    return a * b
def divide(a,b):
    return a / b

num1 = int(input("First Number: "))
num2 = int(input("Second Number: "))

a = add(num1,num2)
s = sub(num1,num2)
m = multiply(num1,num2)
d = divide(num1,num2)

print("Sum: ", a)
print("Difference: ", s)
print("Product: ", m)
print("Division: ", d)