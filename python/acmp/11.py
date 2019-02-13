k,n=map(int,input().split())
a=[1,1]+[0]*(1+n-2)
for i in range(2,k+1):
    a[i]=a[i-1] << 1
    print(a)
for i in range(k+1,n+1):
    a[i]=(a[i-1] << 1)-a[i-1-k]
    print(a)
print(a[n])