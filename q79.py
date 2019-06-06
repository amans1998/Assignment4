print("enter the string in which you want to check the largest word and the smallest word")
a=input()
ss=a.split()
n=len(ss)
b=0
for i in range(n):
    b=b*10+len(ss[i])
print(b)
m=b%10
n=b%10
b=b//10
l=0
k=0
for i in range(1,n):
    r=b%10
    b=b//10
    if m<r:
        m=r
        l=i
    elif n>r:
        n=r
        k=i
print("the largest word is %s" %(ss[l]))
print("the smallest word is %s" %(ss[k]))