print("this program is to concatinate uncommon string")
print("enter first string")
a=input()
print("enter second string")
b=input()
c=a[0]
x=len(a)
y=len(b)
z=len(c)
d=0
for i in range(1,x):
    for j in range(z):
        if c[j]==a[i]:
            d=1
            break
    if d==0:
        c=c+a[i]
        z+=1
    else:
        d=0
print(c)
z=len(c)
for i in range(y):
    for j in range(z):
        if c[j]==b[i]:
            d=1
            break
    if d==0:
        c=c+b[i]
        y+=1
    else:
        d=0
print("the string after cocatenation uncommon string is %s"%(c))
