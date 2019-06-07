n=int(input())
a=[]
c113=0
s=0
for i in range(5):
    a.append(int(input()))
for i in range(5,n):
    x=int(input())
    if a[0]%113==0:
        c113+=1
    if x%113==0:
        s=s+i-4
    else:
        s+=c113
    for j in range (4):
        a[j]=a[j+1]
    a[4]=x
print(s)