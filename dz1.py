from math import sqrt
a=int(input())
b=int(input())
c=int(input())
d=(b**2)-(4*a*c)
x1=0
x2=0
if d<0:
    print("None")
elif d==0:
    x1=(-b)/(2*a)
    print(x1)
else:
    x1=(-b-sqrt(d))/(2*a)
    x2=(-b+sqrt(d))/(2*a)
    print(x1,x2)