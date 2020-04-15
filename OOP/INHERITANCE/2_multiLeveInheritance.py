class A:
    def func1(self):
        print("i am func1 from class A")

    def func2(self):
        print("i am func2 from class A")


class B(A):
    def func3(self):
        print("i am func3 from class B")


class C(B):
    def func4(self):
        print("i am func4 from class C")


c1 = C()    # this object of C class can Access the entity of A through B Class
c1.func1()
c1.func2()
c1.func3()
c1.func4()