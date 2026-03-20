'''Dictionary is the data structure which stores the value in key value pair
  features of dictionary
  1. Dictionary stores the data in the form of key and value.
  2. Dictionaries are unordered and mutable.
  3.Dictionary are created by using parenthesis like sets.
  4.Dictionary does not have numeric index like list, key is acted as the index in dictionary
  

'''
students ={
    'name':'John',
    'class':'second year',
    'roll_no':101,
    'course':'Computer science',
    'age':21
}

#Showing all the key and values of the dictionary
print(students)

#Accessing dictionary elements
print(students['name'])
print(students['age'])

#Adding new key 
students['section']='C'
print(students)

#Updating value
students['name']='John Doe'
print(students['name'])

#Poping values 
students.pop('course')
print(students)

#looping through dictionary
#looping through key
for key in students:
    print(key)

#looping through value
for i in students.values():
    print(i)

#Looping through key-value Pair
for key,value in students.items():
    print(f"{key}:{value}")


#list inside dictionary
person={
    'age':[23,24,56,78,90] 
}
for key,value in person.items():
    if key=='age':
        print("age:")
        for a in value:
            print(a)
    
marks ={
    'ramesh':78,
    'suresh':45,   
    'rajesh':90,
    'bishal':23,
    'srijesh':85
}

#Accessing key and value in dictionary
for key,value in marks.items():
    if value>50:
        print(f"{key} is passed")
    else:
        print(f"{key} is Failed")

