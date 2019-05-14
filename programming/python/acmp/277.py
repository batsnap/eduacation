a,b,c=map(int,input().split())
k=''
if a>0:
   k=k+str(a)
   if b==1:
      k=k+'+x'
   elif b==-1:
      k=k+'-x'
   elif b>0:
      k=k+'+'+str(b)+'x'
   elif b<0:
      k=k+str(b)+'x'
   if c==1:
      k=k+'+y'
   elif c==-1:
      k=k+'-y'
   elif c>0:
      k=k+'+'+str(c)+'y'
   elif c<0:
      k=k+str(c)+'y'

elif a<0:
   k=k+str(a)
   if b==1:
      k=k+'+x'
   elif b==-1:
      k=k+'-x'
   elif b>0:
      k=k+'+'+str(b)+'x'
   elif b<0:
      k=k++str(b)+'x'
   if c==1:
      k=k+'+y'
   elif c==-1:
      k=k+'-y'
   elif c>0:
      k=k+'+'+str(c)+'y'
   elif c<0:
      k=k+str(c)+'y'
elif a==0:
   if b==1:
      k=k+'x'
   elif b==-1:
      k=k+'-x'
   elif b>0:
      k=k+str(b)+'x'
   elif b<0:
      k=k+str(b)+'x'
   if c==1:
      k=k+'+y'
   elif c==-1:
      k=k+'-y'
   elif c>0:
      k=k+'+'+str(c)+'y'
   elif c<0:
      k=k+str(c)+'y'
if k=='':
   print(0)
else:
   print(k)