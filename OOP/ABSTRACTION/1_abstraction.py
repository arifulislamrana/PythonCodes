from abc import *

# abstract class should have at least one abstract method
# abstract method does not have any body
# we cant create object of a abstract class


class Phone(ABC):  # inheriting ABC class
    @abstractmethod
    def processor(self):
        pass

    @abstractmethod
    def camera(self):
        pass

    @abstractmethod
    def battery(self):
        pass


class Sony(Phone): # this class must implement all methods of phone
    def processor(self):
        print("good processor")

    def camera(self):
        print("Average camera quality")

    def battery(self):
        print("good battery performance")


class Samsung(Phone):  # this class must implement all methods of phone
    def processor(self):
        print("average processor")

    def camera(self):
        print("better camera quality")

    def battery(self):
        print("poor battery performance")


obj1 = Sony()
obj1.processor()
obj1.camera()
obj1.battery()

obj2 = Samsung()
obj2.processor()
obj2.camera()
obj2.battery()