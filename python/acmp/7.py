def check(a,b):
    k=2
    i=0
    
    while i<(len(a)):
        if (int(a[i]))>(int(b[i])):
            k=0
            return 0
        elif (int(a[i]))<(int(b[i])):
            k=1
            return 1
        elif (int(a[i]))==(int(b[i])):
            k=2
        i+=1
        
    return 2

a=['','','']
j=0
f = open('INPUT.TXT', 'r')
l = open('OUTPUT.TXT', 'w')

c=str(input())
#'''вытаскиваем из файла числы'''
for i in range (0,len(c)): 
    if c[i]!=' ':
        a[j]=a[j]+c[i]
    else: 
        j+=1

#'''если a=b=c'''

if len(a[0])==len(a[1])==len(a[2]):
    if check(a[0],a[1])==0 and check(a[0],a[2])==0:#если первое самое большое
        l=l.write(a[0])
    elif check(a[0],a[1])==1 and check(a[1],a[2])==0:#если второе самое большое
        l=l.write(a[1])
    elif check(a[0],a[1])==2 and check(a[0],a[2])==0:#если 1 равно 2 но 1 больше 3 
        l=l.write(a[0])
    elif check(a[0],a[1])==2 and check(a[0],a[2])==1:#если 1 равно 2 но 3 больше 1
        l=l.write(a[2])
    elif check(a[1],a[2])==2 and check(a[1],a[0])==0:#если 2 равно 3 но 2 больше 1 
        l=l.write(a[1])
    elif check(a[1],a[2])==2 and check(a[1],a[0])==1:#если 2 равно 3 но 1 больше 2 
        l=l.write(a[0])
    elif check(a[0],a[2])==2 and check(a[0],a[1])==0:#если 1 равно 3 но 1 больше 2 
        l=l.write(a[0])
    elif check(a[0],a[2])==2 and check(a[0],a[1])==1:#если 1 равно 3 но 2 больше 1 
        l=l.write(a[1])
    else:#если 3 самоебольшеое
        l=l.write(a[2])
#если a=b но a>c'''
elif (len(a[0])==len(a[1])) and (len(a[0])>len(a[2])):
    if check(a[0],a[1])==0:
        l=l.write(a[0])
    else:
        l=l.write(a[1])
#если a=b но a<c
elif (len(a[0])==len(a[1])) and (len(a[2])>len(a[0])):
    l=l.write(a[2])
#'''если a=c но a>b'''
elif (len(a[0])==len(a[2])) and (len(a[0])>len(a[1])):
    if check(a[0],a[2])==0:
        l=l.write(a[0])
    else:
        l=l.write(a[2])
#'''если a=c но a<b'''
elif (len(a[0])==len(a[2])) and (len(a[1])>len(a[0])):
    l=l.write(a[1])
#'''если b=c но b>a'''
elif (len(a[1])==len(a[2])) and (len(a[1])>len(a[0])):
    if check(a[1],a[2])==0:
        l=l.write(a[1])
    else:
        l=l.write(a[2])
#'''если b=c но b<a'''
elif (len(a[1])==len(a[2])) and (len(a[0])>len(a[1])):
    l=l.write(a[0])
#'''если они все разной длинны'''
elif len(a[0])>len(a[1]) and len(a[0])>len(a[2]):
    l=l.write(a[0])
elif len(a[1])>len(a[0]) and len(a[1])>len(a[2]):
    l=l.write(a[1])
else:
    l=l.write(a[2])
l = open('OUTPUT.TXT', 'r')
c=str(l.read())
print(c)
