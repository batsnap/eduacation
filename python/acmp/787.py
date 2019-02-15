def max(a,b:int):
   if a>b:
      return a
   elif b>a:
      return b
   else:
      return a
def min(a,b:int):
   if a>b:
      return b
   elif b>a:
      return a
   else:
      return a
n=int(input())
a=[[]]*n
for i in range(n):
   a[i]=[0]*(n-i)
b=list(map(int, input().split()))
for i in range (n):
   a[0][i]=b[i]
if n%2==0:
   for i in range (1,n):
      for j in range(1,n-i+1):
         if i%2==1:
            a[i][j-1]=max(a[i-1][j-1],a[i-1][j])
         else:
            a[i][j-1]=min(a[i-1][j-1],a[i-1][j])
else:
   for i in range (1,n):
      for j in range(1,n-i+1):
         if i%2==1:
            a[i][j-1]=min(a[i-1][j-1],a[i-1][j])
         else:
            a[i][j-1]=max(a[i-1][j-1],a[i-1][j])
print(a[n-1][0])