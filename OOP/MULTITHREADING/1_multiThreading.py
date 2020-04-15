from threading import *
from time import sleep


class Hello(Thread):
    def run(self):      # run is the built in method of thread class
        for i in range(5):
            print("hello")
            sleep(1)    # wait 1 sec for next print


class Hi(Thread):
    def run(self):
        for i in range(5):
            print("hi")
            sleep(1)    # wait 1 sec for next print


obj1 = Hello()
obj2 = Hi()
obj1.start()   # start will create different execution in parallel and it will call run which is built in method in threading class
sleep(0.2)  # this sleep will make the gap b2in hello and hi and prevent over lapping
obj2.start()

obj1.join()  # asking main thread to wait till obj1.start execute
obj2.join()  # asking main thread to wait till obj2.start execute

print("bye")    # main thread will execute this
