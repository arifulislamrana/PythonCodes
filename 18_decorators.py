# example-1
def inc(x):
    return x + 1


def dec(x):
    return x - 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 3))
print(operate(dec, 3))

# example-2


def is_called():
    def is_returned():
        print("Hello")
    return is_returned


new = is_called()
new()

# example-3


def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner


def ordinary():
    print("I am ordinary")


ordinary()
pretty = make_pretty(ordinary)
pretty()

# example-4


def div(x, y):
    print(int(x / y))


def smart_div(func):

    def inner(x, y):
        if x < y:
            x, y = y, x
        return func(x, y)
    return inner


div = smart_div(div)
div(2, 4)

# example-5


def works_for_all(func):
    def inner(*args, **kwargs):
        print("I can decorate any function")
        return func(*args, **kwargs)
    return inner


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star   # @is also indicate decorators
@percent
def printer(msg):
    print(msg)


printer("Hello-1: decoration using @ sign")
# understandable decoration. this is equivalent to previous decoration


def printer(msg):
    print(msg)


printer = star(percent(printer))
printer('hello-2: decoration without using @ sign')