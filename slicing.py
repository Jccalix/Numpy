import numpy as np

array = np.array([[1, 2, 3, 4], 
                  [5, 6, 7, 8], 
                  [9, 10, 11, 12], 
                  [13, 14, 15, 16]])

# Slicing to get the first two rows and the last two columns
sliced_array = array[:2, 2:]

print(sliced_array)
print('--------------------------------')

# array [start:end:step, start:end:step]

print(array[1:3, 1:4])  
