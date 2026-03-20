'''
Tuple are the data structure which is used to store multiple data
  #features of tuples
  1.Tuple are immutable(cannot change original tuple value)
  2.tuple are created using parenthesis ()
  3.We can store multiple data type in a single variable
'''
names =('ramesh','suresh','rajesh')

#Showing all the elements of tuple
print(names)

#showing one specific element of the tuple
print(names[0])
print(names[2])

#Changing the value of the element
# names[0]='srijesh'#This will show error because tuple are im-mutable
print(names)

#we can store multiple data type in single tuple
multiple=('ram',101,245.56,True)
print(multiple)

#length of the tuple
print(len(names))
print(len(multiple))


#looping through tuple
for m in multiple:
    print(m)
