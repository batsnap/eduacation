a=[]
b=[]
a=['','','','']
l = open('INPUT.TXT', 'r')
f=open('OUTPUT.TXT','w')
c=str(l.read())
j=0
for i in range (0,len(c)):
    if c[i]!=' ':
        a[j]=a[j]+c[i]
    else: 
        j+=1

for i in range (len(a)):
    b.append(int(a[i]))
s=''
for i in range(-100,101):
    if i**3*b[0]+i**2*b[1]+i*b[2]+b[3]==0:
        s=s+str(i)+' '
f.write(s)
