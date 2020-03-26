def person(name, age):
    print(name)
    print(age)


person('Arif', 24)   # Positional arguments
person(age=24, name='arif')  # keyword arguments


# for default arguments
def person1(name, age=18):
    print(name)
    print(age)


person1('arif', 24)


# for variable length arguments
def add(*b):
    c = 0
    for i in b:
        c = c + i
    print(c)


add(23, 34, 3, 20)  # multiple value passing for one variable(parameter)
