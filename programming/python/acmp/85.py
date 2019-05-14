def nod(a,b:int):
   while a != 0 and b != 0:
      if a > b:
         a = a % b
      else:
         b = b % a
   return a+b
n,m=map(int,input().split())
k=''
l=''
for i in range (n):
   k+='1'
for i in range (m):
   l+='1'
k=int(k)
l=int(l)
print(nod(k,l))
