from random import randint%
n=int(input())
s=0.0
x=0
a=[randint(0,30000) for i in range(n)]
print(a)
for i in range (n):
    if a[i]%2==1:
        s+=a[i]
        x+=1
print(s)
print(x)
print(s/x)
