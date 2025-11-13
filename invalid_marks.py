try:
    mark =int(input("Enter the mark: "))
    if(mark <0 or mark >100 ):
        raise ValueError("Invalid marks")
    print("valid")
except ValueError as e:
    print(e)