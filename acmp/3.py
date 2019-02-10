f = open('INPUT.TXT', 'r')
c=str(f.read())
a=int(c)
if a==5:
    s=25
else:
    l=a//10
    s=str(l*(l+1))+'25'
l = open('OUTPUT.TXT', 'w')
l=l.write(str(s))
