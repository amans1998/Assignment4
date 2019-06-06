print("this program is to remove consecutive duplicates")
print("please enter the string")
a=input()
b=len(a)
c=a[0]
j=0
for i in range(1,b):
    if a[i]!=c[j]:
        c=c+a[i]
        j+=1
print(c)
