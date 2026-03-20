#import is a built-in function in Python that allows you to import modules and their functions, classes, or variables into your current script.
#It is used to access code from other files or libraries.
'''syntax 
   import module_name
'''
import math

#Importing square root function
a= 20
b= math.sqrt(a)
print(b)

#Importing specific function instead of importing whole module
from math import factorial

x=5
y=factorial(x)
print(y)



