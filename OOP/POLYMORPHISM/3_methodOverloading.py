# method overloading is same function with different parameter
#  Python does not support method overloading
# but we can create it
class Math:

    def add(self, a=None, b=None, c=None):
        if a == None:
            return 0
        if b == None:
            return a
        if c == None:
            return b+a
        else:
            return b+c+a


m = Math()
print(m.add())
print(m.add(2))
print(m.add(2, 3))
print(m.add(2, 3, 4))