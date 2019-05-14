n=int(input())
for i in range (n):
    a=list(map(int,input().split()))
    for j in range(a[1]):
        if len(str(a[0]))==1:
            s1='0'+str(a[0])
            s2='0'+str(a[0]+1)
        else:
            s1=str(a[0])
            s2=str(a[0]+1)
        if j%2==0:
            print('..'+s1+'..')
        else:
            print(s1+'..'+s2)
        if j%2==0:
            a[0]+=1
        else:
            a[0]+=2
