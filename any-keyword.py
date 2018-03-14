#python any() as argument
l=[1,2,3,4,0]
print(any(l)) #all values are true returns true
l=[0,False]
print(any(l)) #all values are false returns false
l=[0,False,5]
print(any(l))#one value is true others are false then returns true
l=[1,2,3,False]
print(any(l))#one value is false others are true then returns true
l=[]
print(any(l))#empty iterable returns false
