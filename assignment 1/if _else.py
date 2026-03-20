#if else statement is used to make decision in the code

a=12
b=13

if a>b:
    print("a is greater than b")
else:
    print("b is greater")

num = int(input("enter the number:"))

if num%2==0:
    print("the number is even")
else:
    print("the number is odd")

#Nested if-else

number = int(input("enter the number:"))

if number>0:
    if number%2==0:
     print("the number is even")
    else:
     print("the number is odd")
else:
   print("the number is negative")

#elif

x=int(input("enter the value of x"))
y=int(input("enter the value of y"))
z=int(input("enter the value of z"))

if x>y and x>z:
  print("x is greatest")
elif y>x and y>z:
  print("y is greatest")
else:
  print("z is greatest")
  