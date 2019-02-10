n=int(input())
a=['']*n
b=[]
j=0
z=0
for i in range (n):
    c=str(input())
    for k in range (len(c)):
        if c[k]!=' ':
            a[j]=a[j]+c[k]
        else: 
            j+=1
    for i in range (len(a)):
        b.append(int(a[i]))
    z=z+sum(b)
    a=['']*n
    b=[]
    j=0
print(z//2)
