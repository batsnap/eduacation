a=list(map(int,input().split()))
k1=a[0]
k2=a[1]
for i in range(len(a)):
   if i%2==0:
      if a[i]<k1:
         k1=a[i]
   else:
      if a[i]>k2:
         k2=a[i]
print(k1+k2)
