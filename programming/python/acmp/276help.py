n,m=map(int,input().split())
a=[n//m]*m
i=0
s=''
if (m)**2>n :
   while sum(a)!=n:
      a[i]+=1
      i+=1
      if i==m:
         i=0
   a.sort()
else:
   while sum(a)!=n:
      a[i]-=1
      i+=1
      if i==m:
         i=0
   a.sort()
   a.reverse()
for i in range (m):
   s=s+str(a[i])+' '
print(s)