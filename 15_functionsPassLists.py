n = int(input("enter no of values to enter: "))
lst = [int(input("enter nums:")) for i in range(n)]
print(lst)


def odd_even(l):
    odd = 0
    even = 0
    for i in l:
        if i % 2 == 0:
            even += 1
        else:
            odd += 1
    return even, odd


even, odd = odd_even(lst)
print('Total even: {}\n Total odd: {}\n'.format(even, odd))




