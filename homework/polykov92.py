chet=l2=l1=nechet=1001
a=[]
s=1001*1001
n=int(input())
for i in range (6):
    a.append(int(input()))
for i in range (0,n-6):
    k=int(input())
    if a[0]%2==0 and a[0]<chet:
        chet=a[0]
    elif a[0]%2!=0 and a[0]<nechet:
        nechet=a[0]
    if k%2==0 and k<l1:
        l1=k
    elif k%2!=0 and k<l2:
        l2=k
    for j in range (5):
        a[j]=a[j+1]
    a[5]=k
a=min(chet*l1,nechet*l1,l2*chet)
if a%1001!=0:
    print(a)
else:
    print(1)
