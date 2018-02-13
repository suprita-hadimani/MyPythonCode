import random
m=random.randint(1,10)
print("random number is generated")
print(m)
count=0
while True:
    count+=1
    n=int(input("guess the random number"))
    print(n)
    if m==n:
        print("correct guess")
        print("number of chances to guess=",count)
        break
    elif m<n:
      print("guess lesser number")
    else:
      print("guess bigger number")
