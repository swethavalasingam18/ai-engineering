import numpy as np

# Create an array from a list
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))


print(arr.shape)     # shape tells you the dimensions

# 2D array (like a table/matrix)
matrix = np.array([[1, 2, 3], [4, 5, 6]])
print(matrix)
print(matrix.shape)  # (rows, columns)

# Common quick-create functions
zeros = np.zeros((2, 3))       # 2x3 array of zeros
ones = np.ones((3, 3))         # 3x3 array of ones
rng = np.arange(0, 10, 2)      # [0 2 4 6 8] - like Python's range()
lin = np.linspace(0, 1, 5)     # 5 evenly spaced values from 0 to 1

a = np.array([10, 20, 30])
print(a, a.dtype , type(a))


