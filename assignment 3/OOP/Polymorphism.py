#polymorphism means same methods or operator behaves differently for different object

class int_operation:
    def sum(self,a,b):
        print(a+b)

class float_operation:
    def sum(self,a,b):
        return a+b

class string_operation:
    def sum(self,a,b):
        print(a+b)
    
a1= int_operation()
a1.sum(3,5)

a2= string_operation()
a2.sum('hello','world')