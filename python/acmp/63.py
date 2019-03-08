
s,p=map(int,input().split())
k1=0
k2=0
for i in range (s):
   for j in range(i,s):
      if i+j==s and i*j==p:
         k1=i
         k2=j
         break
if k1>k2:
   print(k2,k1)
else:
   print(k1,k2)