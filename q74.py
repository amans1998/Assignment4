print("this is the program to find the minimum window")
print("enter first string")
a=input()
print("enter second string")
b=input()
d=""
x=len(a)
y=len(b)
if y>x:
    c=a
    a=b
    b=c
x=len(a)
y=len(b)
m=0
n=x-1
for i in range(y):
    for j in range(x):
        if b[i]==a[j]:
            if i==0:
                n=j
            if m<j:
                m=j
            break
for i in range(n,m+1):
    d=d+a[i]
print("the minimum window is %s"%(d))
