
class Editor():
    def execute(self):
        print ("Spell check")
        print ("Definition")
        print ("Error handling")

class pycharm():
    def execute(self):
        print("Reliable")
        print("Executeable")



class Laptop():

    def code(self,ide):
        ide.execute()

ide=Editor()

lap1=Laptop()
lap1.code(ide)

# Since ide type is coming from pycharm/editor and it has execute function in it so it is duck typing, if anything walks , quaks or looks like a duck that is duck typing