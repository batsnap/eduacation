#n=int(input())
b=[]
k=0
l=[]
v=''
stroka=''
stroka2=''
a=list(map(int,input().split()))
c=len(a)-1
for i in range (2,c):
    if c%i==0:
        b.append(i)
for i in range(len(b)): 
    for j in range(c//b[i]):
        stroka=stroka+str(a[j])+' '
    l.append(stroka)
    stroka=''
print(l)
