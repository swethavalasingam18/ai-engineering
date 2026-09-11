import pandas as pd
import numpy as np
 #A. From a standard Python List (with default numeric index)

list_data = [10, 20, 30, 40]
series_from_list = pd.Series(list_data)

# B. From a List with custom Index Labels
labels = ['a', 'b', 'c', 'd']
series_with_labels = pd.Series(list_data, index=labels)

# C. From a Python Dictionary (Keys automatically become the index)
dict_data = {'Day 1': 420, 'Day 2': 380, 'Day 3': 390}
series_from_dict = pd.Series(dict_data)

print("--- Series with Custom Labels ---")
print(series_with_labels)
print("\n--- Series from Dictionary ---")
print(series_from_dict)

