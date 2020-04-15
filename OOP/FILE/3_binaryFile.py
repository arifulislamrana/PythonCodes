# to copy an image
f1 = open('vaibon.JPG', 'rb')
f2 = open('vaibonCopy.JPG', 'wb')
for i in f1:
    f2.write(i)

