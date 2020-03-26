x = lambda a: a + 10
print(x(5))
x1 = lambda a, b: a * b
print(x1(5, 6))

# uses of filter, map, reduce  using lambda function
nums = [2, 4, 5, 3, 8]
evens = list(filter(lambda a: a % 2 == 0, nums))  # returns even numbers from nums list
print(evens)
doubles = list(map(lambda a: a * 2, evens))     # double the values of evens
print(doubles)

from functools import reduce    # to use reduce function

sum = reduce(lambda a, b: a + b, doubles)
print(sum)
