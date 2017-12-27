#1. unpacking the args
def fun(a,b,c,d,e):
    print(a,b,c,d)
my_list=[1,2,3,4,5]
#unpacking list of aruguments * is used to unpack the args
fun(*my_list)

#2. packing the elements
def sum(*args):
    sum=0
    for i in range(0,len(args)):
        sum=sum+args[i]
    return sum
print(sum(1,2,3))
print(sum(1,2))
