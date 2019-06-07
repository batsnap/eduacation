n=int(input())
a=[]
c101=0
s1=s=0
for i in range(5):
    a.append(int(input()))
for i in range(5,n):
    x=int(input())
    if a[0]%101==0:
        c101+=1
    s1+=i-4
    if x%101==0:
        s=s+i-4
    else:
        s+=c101
    for j in range (4):
        a[j]=a[j+1]
    a[4]=x
print(s1-s)