#factorial of number
def fact(n):
    if n==1:
        return n
    else:
        return n * fact(n-1)
b=int(input("enter number to compute factorial"))
print(fact(b))
