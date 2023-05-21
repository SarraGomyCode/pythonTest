class Init :

    def __init__(self,name):
        self.name = name
    def say_hey (self):
        print ("Hey", self.name)
    def change_name (self, newname) :
        self.name = newname
        print("Hey", self.name)

class A:

    def __init__(self, something):
        print("A is called")
        self.something = something
        print("A is called", self.something)
    def definition_plan (self,newthing):
        self.something = newthing
        print("A is called", self.newthing)

class B(A):

    def __init__(self,something):
        A.__init__(self,something)
        print ("B is called", self.something)
        self.something = something



sarra_name = Init ("sarra")
mohsen_name = Init ("mohsen")
sarra_name.say_hey()
mohsen_name.say_hey()
sarra_name.change_name("salah")
exemple_A = A ("test_A")
exemple_B = A ("test_A_Bis")
exemple_A.definition_plan ("add")
obj = B("omething")
