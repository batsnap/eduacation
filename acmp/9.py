a=[]
b=[]
n=int(input())
for i in range (n):
    a.append('')
j=0
l = open('INPUT.TXT', 'r')
f=open('OUTPUT.TXT','w')
c=str(l.read())
for i in range (2,len(c)):
    if c[i]!=' ':
        a[j]=a[j]+c[i]
    else: 
        j+=1
for i in range (len(a)):
    b.append(int(a[i]))
print(b)
a=0
c1=0
c2=0
max=-9999
min=9999
for i in range(len(b)):
    if b[i]>max:
        max=b[i]
        c1=i
    if b[i]<min:
        min=b[i]
        c2=i
print(c2,' ',c1)
sum=0
proz=1
if c2>c1:
    for i in range (c1+1,c2):
        proz=proz*b[i]
else:
    for i in range (c2+1,c1):
        proz=proz*b[i]
for i in range(len(b)):
    if b[i]>0:
        sum=sum+b[i]
s=''
s=str(sum)+' '+str(proz)
f=f.write(s)

