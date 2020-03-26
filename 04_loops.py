#while loop
i = 0
while i <= 5 :
    print('vai',end='')
    j = 0
    while j <= 3 :
        print('salam',end='')
        j = j + 1
    i = i + 1
    print()

#for loop
x = ['arif', 21, 2.1]
for i in  x:
    print(i)

y = 'arif'
for i in y:
    print(i)


for i in ['arif', 21, 2.1]:
    print(i)


for i in range(10):
    print(i)


for i in range(10,21,2):
    print(i)

for i in range(20,9,-2):
    print(i)


for i in range(0, 21):
    if i % 3 == 0 or i % 5 == 0:
        print('hello')
        continue
    print(i)


for i in range(0, 21):
    if i % 3 == 0 or i % 5 == 0:
        pass
    else:
        print(i)




for number in range(2, 10):
    if number % 2 == 0:
        print("Found an even number", number)
        continue
    print("Found a number", number)