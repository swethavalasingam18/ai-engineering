import numpy as np
a = np.array([10, 20, 30])
print(a.shape)   # (3,)   → 1D array with 3 elements

b = np.array([[1, 2, 3], [4, 5, 6]])
print(b.shape)   # (2, 3)  → 2 rows, 3 columns

print(b.ndim)    # 2  → number of dimensions
print(b.size)    # 6  → total number of elements

c= np.arange(1,13)  # [1 2 3 4 5 6 7 8 9 10 11 12]  shape (12,)
print(c)
print(c.shape)
d= c.reshape(3,4)     # 3 rows, 4 columns
print(d) 
print(d.shape)

e= d.reshape(4,3)    # 4 rows, 3 columns
print(e)
print(e.shape)
