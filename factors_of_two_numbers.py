a=int(input("enter the first number"))
b=int(input("enter the second number"))
def compute(x,y):
    n=[]
    if x>y:
        smaller=y
    else:
        smaller=x
    for i in range(1,smaller+1):
        if((x%i==0) and (y%i==0)):
            n.append(i)
    return n
m=compute(a,b)
print(m)
