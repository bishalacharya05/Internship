'''OOP is a programming style where we organize code in the form of class and object
   class: Class is the blue print of creating object
   object: object is instance of the object
'''

class car:
    #It is a constructor which is used is called when object is created
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model
    
    def start(self):
        print(f"the car of brand {self.brand} and  model {self.model} is started")
        
c = car('toyata','supra')
c.start()