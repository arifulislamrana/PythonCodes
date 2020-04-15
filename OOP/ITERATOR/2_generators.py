# generator gives iterator where declaration of next and iter is not needed
# yield is a special keyword to define a function that it is an generator


def count():
    n = 1
    while n <= 10:
        sq = n * n
        yield sq
        n += 1


x = count()
for i in x:
    print(i)
