n,s=map(int,input().split())
a=list(map(int,input().split()))
a.sort()
k=1
m=a[0]
while m<s and k!=n:
    m+=a[k]
    k+=1
print(k-1)
