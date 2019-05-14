f = open('INPUT.TXT', 'r')
c=str(f.read())
a=int(c)
s=0
if a>0:
  s=int(((1+a)*a)/2)
elif a<0:
  for i in range(a,2):
  	s+=i
else:
  s=1
l = open('OUTPUT.TXT', 'w')
l=l.write(str(s))
