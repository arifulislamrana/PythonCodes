from numpy import *
from math import *

arr = array([
    [1, 2, 3, 4],
    [1, 2, 3, 4],
    [9, 8, 7, 2]
])
print('Data Type:', arr.dtype)
print('Dimension:', arr.ndim)
print('row, column:', arr.shape)
print('total elements', arr.size)

arr1 = arr.flatten()    # making one dimensional
print(arr1)
arr2 = arr.reshape(4, 3)    # making 4 row and 3 col
print(arr2)
arr3 = arr.reshape(2, 3, 2)  # making 3 dimensional array
print(arr3)

m = matrix(arr)
print('matrix:\n', m)

m1 = matrix('1 2 3; 3 4 5; 7 8 6')
print(m1)
print(diagonal(m))  # will print diagonal value of the matrix
# print(m + m1) # will print addition value of the matrix m and m1
# print(m * m1) # will print multiplication value of the matrix m and m1

