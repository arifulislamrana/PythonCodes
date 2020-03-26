from numpy import *
arr1 = array([1, 2, 3])
arr2 = array([4, 2, 3])

arr3 = arr1 + arr2  # will add element of array index wise
print(arr3)

print(sin(arr1))
print(log(arr2))
print(sqrt(arr3))
# copy array
arr4 = arr1  # aliasing array
print(id(arr1))
print(arr4)
print(id(arr4))
arr5 = arr1.view()  # shallow copy
print(arr5)
print(id(arr5))
arr6 = arr1.copy()  # deep copy
print(arr6)
print(id(arr6))