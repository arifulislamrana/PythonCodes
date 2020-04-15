# to copy data from 1_fileData to 2_fileData
f1 = open('1_fileData', 'r')
f2 = open('2_fileData', 'a')  # if we use 'w' mode then after importing new data
# previous data will be erased that's why we use 'a'(append) this does not erase old data
# after importing new data
for i in f1:
    f2.write(i)

