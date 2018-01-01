print("enter the number range of number")
m=int(input("enter the first number"))
n=int(input("enter the second number"))
for num in range(m,n):
    if num > 1:
        for i in range(2,num):
            if(num%i)==0:
                break
        else:
            print(num)
