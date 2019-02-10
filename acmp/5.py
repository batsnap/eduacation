l=open('INPUT.TXT', 'r')
f=open('OUTPUT.TXT','w')
c=str(l.read())
a=[]
b=[]
n=''
for i in range (0,c.find('\n')):
    n=n+c[i]
n=int(n)
for i in range (n):
    a.append('')
j=0

for i in range (c.find('\n')+1,len(c)):
    if c[i]!=' ':
        a[j]=a[j]+c[i]
        print(a)
    else: 
        j+=1
for i in range (len(a)):
    b.append(int(a[i]))
chet=''
nechet=''
k1=0
k2=0
for i in range (len(b)):
    if b[i]%2==0:
        chet=chet+str(b[i])+' '
        k1+=1
    else:
        nechet=nechet+str(b[i])+' '
        k2+=1
if n==1 and k2>0:
    if len(nechet)==3:
        nechet=nechet[0]+nechet[1]
    f=f.write(nechet+'\n\n'+'NO')
    
elif n==1 and k1>0:
    if len(chet)==3:
        chet=chet[0]+chet[1]
    f=f.write(chet+'\n\n'+'YES')
elif n==0:
    f=f.write('NO')
elif k1<k2:
    f=f.write(nechet+'\n'+chet+'\n'+'NO')
elif k1>k2:
    f=f.write(nechet+'\n'+chet+'\n'+'YES')
else:
    f=f.write(nechet+'\n'+chet+'\n'+'YES')

