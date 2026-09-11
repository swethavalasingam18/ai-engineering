import numpy as np
a = np.array([10, 20, 30, 40, 50])

print(a[0])      # 10  → first element
print(a[-1])     # 50  → last element
print(a[1:3])    # [20 30]  → slice from index 1 to 2 (3 excluded)
print(a[:3])     # [10 20 30]  → first 3
print(a[::2])    # [10 30 50]  → every 2nd element


b = np.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])

print(b[0, 0])     # 1   → row 0, col 0
print(b[1, 2])     # 6   → row 1, col 2
print(b[2])        # [7 8 9]  → entire row 2
print(b[:, 0])     # [1 4 7]  → entire column 0
print(b[0:2, 0:2]) # [[1 2] [4 5]]  → top-left 2x2 block


c = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(c[1, :])      # row 1
print(c[:, 2])      # column 2
print(c[0:2, 1:3])  # top-right 2x2 block