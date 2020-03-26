def update(x):
    print('id of x before update:', id(x))
    x = 8
    print('id of x after update:', id(x))
    return x


m = 6
print('id of m:', id(m))
n = update(m)
print('id of n:', id(n))

lst = [1, 2, 3, 4]


def list_handle(x):
    print('before update id of lst[1]:', id(x[1]), 'list:', x)
    x[1] = 30
    print('after update id of lst[1]:', id(x[1]), 'list:', x)


list_handle(lst)
