def arthemetic():
    print("please enter the first value")
    a=int(input())
    print("please enter the second value")
    b=int(input())
    print("what operation you want to execute")
    print("for addition type add")
    print("for subtraction type sub")
    print("for multiplication type multi")
    print("for division type div")
    print("for modulus type mod")
    print("for float division type fdiv")
    print("for exponent type exp")
    s=input()
    if s=="add":
        c=a+b
        print("%s + %s = %s" %(a,b,c))
    elif s=="sub":
        c=a-b
        print("%s - %s = %s" %(a,b,c))
    elif s=="multi":
        c=a*b
        print("%s * %s = %s" %(a,b,c))
    elif s=="div":
        c=a/b
        print("%s / %s = %s" %(a,b,c))
    elif s=="mod":
        c=a%b
        print("%s modulus %s = %s" %(a,b,c))
    elif s=="fdiv":
        c=a//b
        print("%s // %s = %s" %(a,b,c))
    elif s=="exp":
        c=a**b
        print("%s ** %s = %s" %(a,b,c))
def logical():
    print("please enter the first value")
    a=int(input())
    print("please enter the second value")
    b=int(input())
    print("please enter the third value")
    c=int(input())
    print("what operation you want to execute")
    print("and")
    print("or")
    s=input()
    if s=="and":
        if a<b and b<c:
            print("the result of a<b and b<c is True")
        else:
            print("the result of a<b and b<c is False")
    elif s=="or":
        if a<b or b<c:
            print("the result of a<b or b<c is True")
        else:
            print("the result of a<b or b<c is False")
def comparison():
    print("please enter the first value")
    a=int(input())
    print("please enter the second value")
    b=int(input())
    print("what operation you want to execute")
    print("for < type l")
    print("for > type g")
    print("for <= type le")
    print("for >= type ge")
    print("for == type ee")
    print("for != type ne")
    s=input()
    if s=="l":
        if a<b:
            print("the result of a<b is True")
        else:
            print("the result of a<b is False")
    elif s=="g":
        if a>b:
            print("the result of a>b is True")
        else:
            print("the result of a>b is False")
    elif s=="le":
        if a<=b:
            print("the result of a<=b is True")
        else:
            print("the result of a<=b is False")
    elif s=="ge":
        if a>=b:
            print("the result of a>=b is True")
        else:
            print("the result of a>=b is False")
    elif s=="ee":
        if a==b:
            print("the result of a==b is True")
        else:
            print("the result of a==b is False")
    elif s=="ne":
        if a!=b:
            print("the result of a!=b is True")
        else:
            print("the result of a!=b is False")
def membership():
    print("please enter the first string")
    a=input()
    print("please enter the second string")
    b=input()
    print("what operation you want to execute")
    print("in")
    print("not in")
    s=input()
    if s=="in":
        c=b in a
        print("the result of b in a is %s"%(c))
    elif s=="not in":
        c=b not in a
        print("the result of b not in a is %s"%(c))
print("please enter which operator you want to do")
print("arthemetic")
print("logical")
print("comparison")
print("membership")
print("RND")
op=input()
if op=="arthemetic":
    arthemetic()
if op=="logical":
    logical()
if op=="comparison":
    comparison()
if op=="membership":
    membership()
if op=="RND":
    rnd()
