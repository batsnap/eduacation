n=int(input())
a=[[]]*n
for i in range(n):
   a[i]=[0]*(n-i)

b=list(map(int, input().split()))
for i in range (n):
   a[0][i]=b[i]
for i in range (1,n):
   for j in range(1,n-i+1):
      if i%2==1:
         if a[i-1][j]>a[i-1][j-1]:
            a[i][j-1]=a[i-1][j]
         elif a[i-1][j]<a[i-1][j-1]:
            a[i][j-1]=a[i-1][j-1]
         else:
            a[i][j-1]=a[i-1][j]
        
      elif i%2==0:
         if a[i-1][j]>a[i-1][j-1]:
            a[i][j-1]=a[i-1][j-1]
         elif a[i-1][j]<a[i-1][j-1]:
            a[i][j-1]=a[i-1][j]
         else:
            a[i][j-1]=a[i-1][j]
        
print(a[n-1][0])
         

