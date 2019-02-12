n=int(input())
a=list(map(int, input().split()))
c=0
c2=0
k=a[0]
k2=1000
for i in range(len(a)):
    if k<a[i]:
        k=a[i]
        c=i

for i in range(len(a)):
    if k2>=a[i]:
        k2=a[i]
        c2=i
