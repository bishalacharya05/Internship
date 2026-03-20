'''Function is a block of code which performs specific task 
   Function helps to reuse block of code
   function is initialize using def keyword


'''
#Simple function 
def greeting():
    print("hello good morning")

greeting()

#function with parameter
def hello(name):
    print(f"hello {name}")

hello('bishal')

#fuction with return value
def add (a,b):
    return a+b

result=add(2,3)
print(result)

#function to check whether the number is prime or not
def prime_check(num):
    if num<=1:
        print("the number is not prime")
    else:
        for i in range(2,num):
            if num%i==0:
                print("the number is not prime")
                break
        else:
            print("number is prime")

prime_check(123)


