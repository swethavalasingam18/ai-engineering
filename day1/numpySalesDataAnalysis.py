import numpy as np

sales = np.array([
    [120, 135, 150],   # Product A: Jan, Feb, Mar
    [200, 180, 220],   # Product B
    [90,  95,  100],   # Product C
    [300, 310, 295]    # Product D
])
print(sales.shape)      #(4,3)
print(sales[2])         #Indexing: Print Product C's full sales record (row 2).[90 95 100]
print(sales[0:2 ,1:3])  #Slicing: Print just Feb and Mar sales for Products A and B only (should be a 2×2 block).
print(sales.sum(axis=0))  #total sales per month
print(sales.sum(axis=1))  #total sales per product
print(sales*1.1) #10% increase

# best product
totals_per_product = sales.sum(axis=1)   # one total per product
best_product_index = totals_per_product.argmax()
print(best_product_index)   # 3 → Product D (index 3)