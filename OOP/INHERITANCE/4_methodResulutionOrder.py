class A:
    def __init__(self):
        print("constructor from A")

    def func1(self):
        print("i am func1 from class A")


class B:
    def __init__(self):
        print("constructor from B")

    def func1(self):
        print("i am func1 from class B")


class C(A, B):
    def __init__(self):
        super().__init__()  # this will call constructor of A cz in (A, B) A is in left side
        print("constructor of C")

    def func2(self):
        super().func1()  # this will call func1() of A cz in (A, B) A is in left side
        print("i am func2 from class C")


c1 = C()    # this object of C class can Access the entity of A and B Class but obj of A  and B cant access each other

c1.func2()
