# basic functions
def hello():
    print('Hello buddies \n This is an easy function')


hello()     # calling the function


def add(x, y):
    print('sum is:', x + y)


add(5, 6)


def add_sub(m, n):
    return m + n, m - n


r1, r2 = add_sub(5, 3)
print('sum is:', r1, '\n sub is:', r2)