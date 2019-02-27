a,b,c=map(int,input().split())
k=''
if a>0:
   k=k+str(a)
   if b>0:
      k=k+'+'+str(b)+'x'
   elif b<0:
      k=k++str(b)+'x'
   if c>0:
      k=k+'+'+str(c)+'y'
   elif c<0:
      k=k+str(c)+'y'

elif a<0:
   k=k+str(a)
   if b>0:
      k=k+'+'+str(b)+'x'
   elif b<0:
      k=k++str(b)+'x'
   if c>0:
      k=k+'+'+str(c)+'y'
   elif c<0:
      k=k+str(c)+'y'
elif a==0:
   if b>0:
      k=k+str(b)+'x'
   elif b<0:
      k=k++str(b)+'x'
   if c>0:
      k=k+'+'+str(c)+'y'
   elif c<0:
      k=k+str(c)+'y'
print(k)

   

   
   
