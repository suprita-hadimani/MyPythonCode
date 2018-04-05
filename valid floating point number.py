import re
a=int(input("number of re expressions"))
pattern="^[-+]?[0-9]*\.[0-9]+$"
for i in range a:
    if re.match(pattern,a):
        print("yes")
    else:
        print("no")
