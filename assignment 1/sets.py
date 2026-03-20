'''Sets are the data structure which is used to store data in a single variable
   #features of sets
   1. Sets are mutable
   2. Sets doesn't allows duplicate values
   3. Sets are created using curly brackets



'''

marks = {78,98,90,98,95}

#Showing all elements and shows non repatitive elements 
print(marks)

#showing one elements
# print(marks[1]) this will show error because sets objects are not callable

for m in marks:
    print(m)

#Adding elements to set
marks.add(85)
print(marks)

#Removing elemnts from set
marks.remove(78)
print(marks)

#Set operations

#Uinon: It is the process of combining two or more sets in single set
fruits ={'apple','pineapple','banana'}
veggies ={'brocauli','potato','tomato'}
fruit_veggies= fruits | veggies
print(fruit_veggies)

#Intersection: It is the process of finding the common elements form sets
fruitsI ={'apple','pineapple','banana','tomato'}
veggiesI ={'brocauli','potato','tomato'}
comman= fruitsI & veggiesI
print(comman)