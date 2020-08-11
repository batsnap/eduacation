n=int(input())
a=[]
a1=[]
for i in range(n):
    k=str(input())
    if k not in a:
        a.append(k)
        a1.append(1)
    else:
        a1[a.index(k)]+=1
for i in range(len(a1)-1):
        for j in range(len(a1)-i-1):
            if a1[j] > a1[j+1]:
                a1[j], a1[j+1] = a1[j+1], a1[j]
                a[j], a[j+1] = a[j+1], a[j]
for i in range(3):
    print(a[i],a1[i])