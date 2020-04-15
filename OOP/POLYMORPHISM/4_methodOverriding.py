# MethodOverriding is same function with different workings
class A:
    def show(self):
        print("I'm A class")


class B(A):
    def show(self):
        print("I'm B class")


b = B()
b.show()