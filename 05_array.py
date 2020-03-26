from array import *
x = array('i', [1, 2, 3])#int array
print(x)
print(x.buffer_info())

for e in x:
    print(e)


for i in range(len(x)):
    print(x[i])

m = array(x.typecode, (a for a in x))# copy the array x
print(m)
m = array(x.typecode, (a*a for a in x))# copy the square of array x


y = array('u', ['b', 'j', 'k'])#char array
for e in y:
    print(e)


