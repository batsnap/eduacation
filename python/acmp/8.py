a=[]
b=[]
a=['','','']
l = open('INPUT.TXT', 'r')
f=open('OUTPUT.TXT','w')
c=str(l.read())
j=0
for i in range (0,len(c)-1):
    if c[i]!=' ':
        a[j]=a[j]+c[i]
    else: 
        j+=1
for i in range (len(a)):
    b.append(int(a[i]))
print(b)
if b[0]*b[1]==b[2]:
    f.write('YES')
else:
    f.write('NO')
