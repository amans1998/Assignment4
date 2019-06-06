print("this is the program to count the number of uppercase, lowercase, special character and numeric")
print("plese enter the string")
a=input()
d=len(a)
up=0
lo=0
nu=0
sc=0
for i in range(d):
    if a[i].isupper()==True:
        up+=1
    elif a[i].islower()==True:
        lo+=1
    elif a[i].isdigit()==True:
        nu+=1
    else:
        sc+=1
print("the uppercase are %s" %(up))
print("the lowercase are %s" %(lo))
print("the numeric are %s" %(nu))
print("the special character are %s" %(sc))
