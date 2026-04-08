f=1
n=int(input("enter a number"))
for i in range(1,n+1,1):
     r=n%10
     f*=i
     n=n//10
print(f)

