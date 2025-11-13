print("Menu:")
print(" Sum")
print(" Subtraction")
print(" Product")
print("Division")

n = int(input("Enter your choice :"))

a = int(input("Enter first number:"))
b = int(input("Enter second number:"))

if n == 1:
    print("sum =", a + b)
elif n == 2:
    print("subtraction =", a - b)
elif n == 3:
    print("product =", a * b)
elif n==4:
    print("Division=", a/b)

