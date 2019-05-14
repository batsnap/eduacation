n=int(input())
a=[]
c1=c7=c9=s=c3=0
for i in range(4):
    a.append(int(input()))
for i in range(n-4):
    k=int(input())
    if a[0]%10==1:
        c1+=1
    elif a[0]%10==7:
        c7+=1
    elif a[0]%10==3:
        c3+=1
    elif a[0]%10==9:
        c9+=1
    if k%10==1:
        s=s+c1
    elif k%10==7:
        s=s+c3
    elif k%10==3:
        s=s+c7
    elif k%10==9:
        s=s+c9
    for j in range (3):
        a[j]=a[j+1]
    a[3]=k
print(s)