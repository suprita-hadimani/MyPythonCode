import re
string="suriprita-sup-hadimani"
a=re.search("(ri.*)",string) #search will search through out the string 
if a:
    print("search:",a.group(0))
b=re.match("(ri.*)",string) #match will match at the begining of the string
if b:
    print("match:",b.group(1))
