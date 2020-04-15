class Animal:
    tail = 1    # this is static variable(class variable) common for all

    def __init__(self, hand, leg):
        self.hand = hand    # this is instance variable is not common for all
        self.leg = leg

    def figure(self):
        print("this type of animal has "+self.leg+" legs"+"and "+self.hand+" hands")


human = Animal('2', '2')
cow = Animal('4', '0')
print("Human:")
human.figure()
print("Cow:")
cow.figure()

Animal.tail = 3
print("human: ", human.tail)
print("Cow: ", cow.tail)
