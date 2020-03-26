import sys
sys.setrecursionlimit(2000)
print(sys.getrecursionlimit())


def hel(i):   # a recursion to print hello 5 times
    i += 1
    print('xoss')
    if i == 5:
        return
    hel(i)


hel(0)


def fact(n):    # a recursion to calculate the factorial of a number
    if n == 1:
        return 1
    return n * fact(n-1)


print(fact(int(input("enter a num to be factorized:"))))