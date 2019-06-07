n=int(input())
a=[]
c79=0
s=0
for i in range(4):
    a.append(int(input()))
for i in range(4,n):
    x=int(input())
    if a[0]%79==0:
        c79+=1
    if x%79==0:
        s=s+i-3
    else:
        s+=c79
    for j in range (3):
        a[j]=a[j+1]
    a[3]=x
print(s)