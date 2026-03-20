#Inheritance is the process of inheriting the features of parent class to the child class

class father:
    def fatherDetails(self):
        print("this is father class")

#Single inheritance
class mother(father):
    def motherDetails(self):
        print("this is mother details")

#multilevel inheritance
class daughter(mother):
    def daughterDetails(self):
        print("this is mother details")

#Multiple inheritance
class son(mother):
    def SonDetails(self):
        print("this is son class")

s = son()
s.fatherDetails()
s.SonDetails()
d = daughter()
d.fatherDetails()

#Multilevel inheritance
d.motherDetails()
d.fatherDetails()



