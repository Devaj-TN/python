a=int(input("Enter a number: "))
b = int(input("Enter a number"))
try:
    c = a/b
except ZeroDivisionError as e:
    print(e)