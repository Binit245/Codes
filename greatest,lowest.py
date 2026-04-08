a=int(input("enter first number:"))
b=int(input("enter second number:"))
c=int(input("enter third number:"))
if(a>b):
    if(a>c):
        print("a is  greatest")
if(b>c):
    if(b>a):
        print("b is greatest")
else:
    print("c is greatest")