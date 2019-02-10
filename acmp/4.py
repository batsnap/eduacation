l=open('INPUT.txt','r')
f=open('OUTPUT.txt','w')
c=str(l.read())
b=c[0]
s=b+'9'+str(9-int(b))
f=f.write(str(s))
