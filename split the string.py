#split the given string by , and .
import re
a=input("enter a string")
result=re.split(r',|\.',a)#splits the string using multilple seperators
print(result)
for i in result:
    print(i)

#re.split(r',',a)#split using single seprator
#re.split(r',',a,maxsplit=5)#to have maxsplit i.e maximum number of split needed in a list
    
