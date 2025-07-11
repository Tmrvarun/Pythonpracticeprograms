from threading import *
from time import sleep
class Hello(Thread): #Here we are importing thread and making our class a thread class
    def run(self):
        for i in range(5):
            print("Hello")
            sleep(1) # To avoid collision of two threads hello and hi we apply sleep

class Hi(Thread): #Here we are importing thread and making our class a thread class
    def run(self):
        for i in range (5):
            print("Hi")
            sleep(1) # To avoid collision of two threads hello and hi we apply sleep


h1=Hello()
h2=Hi()

h1.start() # This is how threading is started in threading
h2.start()

h1.join() #This line is used to set a condition that if two threads join together then only bye will be printed at the end
h2.join()

print("Bye")