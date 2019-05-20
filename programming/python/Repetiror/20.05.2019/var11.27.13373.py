n=int(input())
k26=k2=k13=kmax=-1
for i in range(n):
    x=int(input())
    if x%26==0 and k26<x:
        k26=x
    elif x%13==0 and k13<x:
        k13=x
    elif x%2==0 and k2<x:
        k2=x
    elif x>kmax:
        kmax=x
a=[k26*k13,k26*k2,k26*kmax,k2*k13,]
print(max(a))