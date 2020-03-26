# different address of global and local variable
a = 10  # global variable


def test():
    a = 23  # local variable
    print('a inside func test:', a)


test()
print('a outside func test:', a)


# default access of global variable from local scope
a = 10  # global variable


def test1():
    print('a inside func test1:', a)


test1()
print('a outside func test1:', a)


# accessing global variable by local variable
a = 10  # global variable


def test2():
    global a
    a = 23  # local variable
    print('a inside func test2:', a)


test2()
print('a outside func test2:', a)


# different address of global and local variable
a = 10  # global variable
print('id of a:', id(a))


def test3():
    a = 23  # local variable
    x = globals()['a']  # accessing the the global variable a
    print('id of local x:', id(x))
    print('a inside func test3:', a)
    globals()['a'] = 20


test3()
print('a outside func test3:', a)