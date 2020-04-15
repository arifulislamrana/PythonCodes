f = open('1_fileData', 'r')
# print(f.read())  # it reads entire data from text file
print(f.readline(), end="")     # reads first line of data
print(f.readline(), end="")     # now it reads second line of data and so on....
print(f.readline(5))  # now it reads first 5 char of 3rd line of data
