class Person:
    def __init__(self):
        self.name = "Arif"
        self.age = 24

    def update(self):
        self.age = 25   # Bcz of "self" which object uses update its age will be changed

    def compare(self, other):
        if self.age == other.age:
            print("two object are same")
        else:
            print("two objects are different")


p1 = Person()
p2 = Person()

print(p1.age)
print(p2.age)
p1.compare(p2)

p1.update()     # update will change the value of age only for p1 not for others

print(p1.age)
print(p2.age)
p1.compare(p2)
