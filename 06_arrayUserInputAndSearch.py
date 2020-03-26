from array import *

arr = array('i', [])

l = int(input('enter the length of array:'))

for i in range(l):
    n = int(input('enter element:'))
    arr.append(n)

print(arr)

# index searching
num = int(input('Enter Searching value index'))
k=0
for e in arr:
    if e == num:
        print('number is in index:', k)
        break
    k += 1

print(arr.index(num))   # built in functions for searching index
