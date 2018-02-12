import subprocess
m=subprocess.check_output("ipconfig")
m=m.decode("utf-8")
f=open("new.txt","w")
f.write(str(m))
f.close()
f=open("new.txt","r")
for line in f:
    if "IPv4" in line:
        print(line.split(":")[1])

