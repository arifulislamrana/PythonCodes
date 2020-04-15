class Math:
    def __init__(self, m1, m2):
        self.m1 = m1
        self.m2 = m2

    def __add__(self, other):   # defining functionality for '+' of objects
        s1 = self.m1 + other.m1
        s2 = self.m2 + other.m2
        return Math(s1, s2)

    def __gt__(self, other):    # defining functionality for '<' of objects
        x = self.m1 + self.m2
        y = other.m1 + other.m2
        if x > y:
            return True
        else:
            return False


x1 = Math(65, 45)
x2 = Math(75, 35)
x3 = x1 + x2
print(x3.m1, x3.m2)

if x1 > x2:
    print("X1 has highest score")
else:
    print("x2 has highest score")

