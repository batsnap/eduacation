a=[]
for i in range (10):
    a.append(0)
print(a)
n=int(input())
for i in range (n):
    k=int(input())
    c=int(k%10+(k%100)/10)
    a[c]+=1
    print(a)
max=a[0]
pos=0
for i in range (10):
    if a[i]>max:
        max=a[i]
        pos=i
    elif a[i]==max:
        if pos<i:
            pos=i
print(pos)
