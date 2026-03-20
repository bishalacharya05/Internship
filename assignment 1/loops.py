#Loop are used to repeat a block of code multiple times. There are two main types of loops in Python: for loops and while loops.

#for loop is used to iterate the block of code until the condition is true.
#For loop is suitable when we know the the condition to stop 

names=["ramesh","bishal","rajesh","suresh"]

for n in names:
    print(n)

# we can also use the range in for loop
for n in range(0,len(names)):
    print(names[n])

#Uisng for loop to check wether the number is prime or not

num= int(input("Enter number "))

if num<=1:
    print("the number is not prime")
else:
    for i in range(2,num):
        if num%i==0:
            print(f"{num} is not prime")
            break
    else:
        print(f"{num} is prime")

#while loop
#While loop is mainly used when the condition to stops is unknown

#print form 1 to 10 using for loop
n=1
while n<=10:
    print(n)
    n+=1

#reversing the number using while loop

number= int(input("Enter number "))
reversed_digit=0
while number>0:
    last_digit=number%10
    reversed_digit=last_digit+reversed_digit*10
    number=number//10
    
print("the reverse is",reversed_digit)
