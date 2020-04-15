class Student:
    def __init__(self, name, rollno):
        self.name = name
        self.roll = rollno
        self.lap = self.Laptop()

    def show(self):
        print(self.name, self.roll)

    class Laptop:
        def __init__(self):
            self.brand = 'MSI'
            self.cpu = 'i3'
            self.ram = 4

        def show(self):
            print(self.brand, self.cpu, self.ram)


s1 = Student('Arif', 170632)
s1.show()
s1.lap.show()