from abc import ABC, abstractmethod

#This is abstract class and abstract class must have atleast one abstract method.
class Animal(ABC):

    @abstractmethod
    #this is abstract method and child must have to implement this to inherit and access any method from the abstract method
    def sound(self):
        pass
    def show(self):
        print("this is show method")

#This is the child class and we must have to implement the abstract method i.e sound() to inherite dog class
#Otherwise it will throw error
class dog(Animal):
    def sound(slef):
        print("dog barks")
    def display(self):
        print("display")
    

d= dog()
d.show()