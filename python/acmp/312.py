a1,a2,n=map(int,input().split())
k=a2-a1
for i in range(n-1):
   a1+=k
print(a1)