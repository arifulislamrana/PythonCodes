from numpy import *
arr = array([1, 2, 3])
print(arr)
print(arr.dtype)

arr = linspace(0, 15, 10)
print('linspace array is', arr)

arr = arange(0, 15, 3)
print('arange array is', arr)

arr = logspace(0, 15, 5)
print('logspace array is', arr)

arr = zeros(5)
print('zeros array is', arr)

arr = ones(5)
print('ones array is', arr)
