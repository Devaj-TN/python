import cmath
a=int(input("Enter a number: "))
b=int(input("Enter a number: "))
c=int(input("Enter a number: "))
d=b**2-4*a*c
root=-b+ cmath.sqrt(d)/2*a
print("The root is :" , root)
