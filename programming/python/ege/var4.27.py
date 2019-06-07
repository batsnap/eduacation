n=int(input())
a=[]
c103=0
s1=s=0
for i in range(4):
    a.append(int(input()))
for i in range(4,n):
    x=int(input())
    if a[0]%103==0:
        c103+=1
    s1+=i-3
    if x%103==0:
        s=s+i-3
    else:
        s+=c103
    for j in range (3):
        a[j]=a[j+1]
    a[3]=x
print(s1-s)