def stroka(n,a,j:int):

    if j>0:
        s1=''
        s2=''
        if len(str(a))==1 and a<9:
            s1='0'+str(a)
            s2='0'+str(a+1)
        elif len(str(a))==1 and a==9:
            s1='0'+str(a)
            s2=str(a+1)
        else:
            s1=str(a)
            s2=str(a+1)
        if n%2==0:
            return ('..'+s1+'..')
        else:
            return (s1+'..'+s2)
    else:
        return ('......')
n = int(input()) 
a = []
for i in range(n):
    a.append([int(j) for j in input().split()])
max=a[0][1]
for i in range (1,len(a)):
    if a[i][1]>max:
        max=a[i][1]
s=''
for i in range (max):
    for j in range (len(a)):
        if j!=(len(a)-1):
            s=s+stroka(i,a[j][0],a[j][1])+'..'
        else:
            s=s+stroka(i,a[j][0],a[j][1])
    print(s)
    for j in range (len(a)):
        if i%2==0:
            a[j][0]+=1
        else:
            a[j][0]+=2
        a[j][1]=a[j][1]-1
    s=''


