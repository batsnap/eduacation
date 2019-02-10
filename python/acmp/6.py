l=open('INPUT.TXT', 'r')
f=open('OUTPUT.TXT','w')
c=str(l.read())
a=[]
my_dict={
    'A':1,
    'B':2,
    'C':3,
    'D':4,
    'E':5,
    'F':6,
    'G':7,
    'H':8,
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '-':0
}
for i in range(len(c)):
    if c[i] in my_dict.keys():
        a.append(my_dict.get(c[i]))
if len(a)==5 and a[2]==0:
    if (abs(a[0]-a[3]))==1 and (abs(a[1]-a[4]))==2:
        f.write('YES')
    elif (abs(int(a[0])-int(a[3])))==2 and (abs(int(a[1])-int(a[4])))==1:
        f.write('YES')
    else:
        f.write('NO')
else:
    f.write('ERROR')
