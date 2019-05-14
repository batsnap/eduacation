from math import exp
e=float(input())
print(exp(1))
x=1
c=1.0000000000000000000000000000000000
while exp(1)-c>=e:
    c=(1.00000000000000000000000000000000000+1.000000000000000000000000000000000/x)**x
    x+=1
    print(c)
    print(x)
print(x)