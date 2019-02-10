a,b=map(int,input().split())
c=[]
d=[]
l0=l1=0
k=1000
for i in range (4):
    c.append(a//k%10)
    k=k//10
k=1000
for i in range (4):
    d.append(b//k%10)
    k=k//10
for i in range(4):
    if c[i]==d[i]:
        l0+=1
for i in range(4):
    for j in range(4):
        if c[i]==d[j] and c[j]!=d[j]:
            l1+=1
print(l0,l1)