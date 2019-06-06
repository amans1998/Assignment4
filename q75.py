print("this is the program to find the smallest window so please enter the string")
a=input()
x=len(a)
b=a[0]
y=len(b)
d=0
for i in range(1,x):
    for j in range(y):
        if b[j]==a[i]:
            d=1
            break
    if d==0:
        b=b+a[i]
        y+=1
    else:
        d=0
print("the smallest window of given string is %s" %(b))
            
