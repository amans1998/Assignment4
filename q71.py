print("this program is to move all spaces in front")
print("enter the string")
a=input()
ss=a.split()
b=len(ss)
for i in range(b-1):
    print(" ",end="")
for i in range(b):
    print(ss[i],end="")
