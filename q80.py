print("enter the string in which you want to check")
a=input()
ss=a.split()
n=len(ss)
b=0
for i in range(n):
    c=ss[i]
    d=len(c)
    if c[0]==c[d-1]:
        b+=1
print("the number of substring in the given string whose first and last character is same are %s" %(b))