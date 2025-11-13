a = [10,20,30,40,50]
try:
    index = int(input("Enter the index: "))
    value = a[index]
    div = int(input("Enter the divisor "))
    result = value/div
    print("Result:" , result)
except (ImportError,ValueError,ZeroDivisionError)as e:
    print(a)