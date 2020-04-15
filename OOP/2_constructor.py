class Computer:
    def __init__(self, cpu, ram):
        self.cpu = cpu
        self.ram = ram

    def config(self):
        print("config is: \n Processor: ", self.cpu, " and ram is: ", self.ram)


c1 = Computer('i7', 16)
c2 = Computer('i9', 12)

c1.config()
c2.config()
