#variable type hint
x:str = 1
print(x)

#function type hint
def sum(a:int, b:int, c:int) ->int :
    return a+b+c

x=sum(1,2,3)
print(x)