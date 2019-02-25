n=str(input())
k=0
s=''
a=[]
if n[0]=='0':
   while n[k]=='0':
      k+=1
for i in range(k,len(n)):
   s=s+n[i]
s=int(s)
while s!=0:
   a.append(s%2)
   s=s//2
for i in range(k):
   a.append(0)
s=0
n=1
a.reverse()
for i in range(0,len(a)):
   s=s+n*a[i]
   n*=2
print(s)