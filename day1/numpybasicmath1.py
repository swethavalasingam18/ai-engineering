import numpy as np

a = np.array([1, 2, 3, 4])
b = np.array([10, 20, 30, 40])

print(a + b)    # [11 22 33 44]
print(a - b)    # [-9 -18 -27 -36]
print(a * b)    # [10 40 90 160]
print(a / b)    # [0.1 0.1 0.1 0.1]
print(a ** 2)   # [1 4 9 16]


# array with single number 
c = np.array([1, 2, 3, 4])

print(c + 10)   # [11 12 13 14]  → adds 10 to every element
print(c * 2)    # [2 4 6 8]
print(c / 2)    # [0.5 1.  1.5 2. ]



# usefull agregative functions

d = np.array([4, 8, 15, 16, 23, 42])

print(d.sum())     # 108
print(d.mean())    # 18.0
print(d.max())     # 42
print(d.min())     # 4
print(d.std())     # standard deviation
print(np.sqrt(d))  # square root of every element