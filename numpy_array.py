import numpy as np

a = np.random.randint(0,101,10)

mean = np.mean(a)
std_dev = np.std(a)

print(a)
print(f"Mean: {mean}")
print(f"Standard Deviation: {std_dev}")