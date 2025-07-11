
class Computer:

    def __init__(self,cpu,ram): #This in-build special method is used to pass values of variables from object to the class
        self.cpu=cpu
        self.ram=ram



    def config(self):
        print("Configuration: ",self.cpu,self.ram)



com1=Computer("i5",256) #passing variables of object to class computer
com2=Computer("AMD",128)


com1.config() #calling config
com2.config()