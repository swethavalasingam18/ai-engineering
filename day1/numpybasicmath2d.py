import numpy as np

m = np.array([[1, 2], [3, 4]])
n = np.array([[10, 20], [30, 40]])

print(m + n)
# [[11 22]
#  [33 44]]

print(m.sum())        # 10  → sum of ALL elements
print(m.sum(axis=0))  # [4 6]  → sum down each column
print(m.sum(axis=1))  # [3 7]  → sum across each row

print(n.sum(axis=0))  # [40 60]  → sum down each column
print(n.sum(axis=1))  # [30 70]  → sum across each row


scores = np.array([[85, 90, 78], [92, 88, 95]])
# row 0 = student A's 3 test scores, row 1 = student B's 3 test scores

print(scores.mean())          # overall average
print(scores.mean(axis=1))    # average per student (per row)
print(scores.mean(axis=0))    # average per test (per column)