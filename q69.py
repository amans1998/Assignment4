print("this program is to find the longest common sub string from two string")
print("please enter first string")
a=input()
print("please enter first string")
b=input()
x=len(a)
y=len(b)
z=x
c=""
d=""
z=len(d)
for i in range(x):
    for j in range(y):
        if a[i]==b[j]:
            c=c+a[i]
            l=True
            while l==True:
                i+=1
                j+=1
                if a[i]==b[j]:
                    c=c+a[i]
                else:
                    i-=1
                    j-=1
                    break
                if i==z-1:
                    l=False
                elif j==y-1:
                    l=False
            break
    if z<len(c):
        d=c
        c=""
        l=0
        z=len(d)
print("the longest common sub string from two string is %s" %(d))
    
