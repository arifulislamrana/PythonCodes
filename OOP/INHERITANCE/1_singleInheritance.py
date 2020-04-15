class A:
    def func1(self):
        print("i am func1 from class A")

    def func2(self):
        print("i am func2 from class A")


class B(A):
    def func3(self):
        print("i am func3 from class B")


b1 = B()    # this object of B class can Access the entity of A Class
b1.func1()
b1.func2()
b1.func3()