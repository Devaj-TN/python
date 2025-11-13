import numpy as np 
a = np.array([[1,2,3],[4,5,6]])
b = np.array([[4,5,6],[1,2,3]])
add = a + b
sub = a - b
mult = a * b
transpose = a.transpose()

print(f"Addition:\n {add} \n")
print(f"Subtraction:\n {sub} \n")
print(f"Multiplication:\n {mult} \n ")
print(f"Transpose:\n {transpose} \n")