class A:
    def func1(self):
        print("i am func1 from class A")

    def func2(self):
        print("i am func2 from class A")


class B:
    def func3(self):
        print("i am func3 from class B")


class C(A, B):
    def func4(self):
        print("i am func4 from class C")


c1 = C()    # this object of C class can Access the entity of A and B Class but obj of A  and B cant access each other
c1.func1()
c1.func2()
c1.func3()
c1.func4()