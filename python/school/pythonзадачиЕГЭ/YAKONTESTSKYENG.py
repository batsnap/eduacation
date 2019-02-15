def maxid(a):
   k=0
   s=a[0]
   for i in range (1,len(a)):
      if a[i]>s:
         k=i
         s=a[i]
   return k
n=int(input())
a=b=str()
k=[]
c=[]
slova=['']*3
count=[0]*3
for i in range(n*3):
    a,b=map(str,input().split())
    k.append(a)
    c.append(int(b))
for i in range(3):
   slova[i]=(k.pop(maxid(c)))
   count[i]=(c.pop(maxid(c)))
print(slova,count)
