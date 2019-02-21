def kaprikar(x:int):
   m=[]
   l=0
   r=''
   a=x//1000
   b=(x%1000)//100
   c=(x%100)//10
   d=x%10
   m.append(a)
   m.append(b)
   m.append(c)
   m.append(d)
   m.sort()
   x=int(str(m[0])+str(m[1])+str(m[2])+str(m[3]))
   m.reverse()
   a=int(str(m[0])+str(m[1])+str(m[2])+str(m[3]))
   return a-x
n=int(input())
i=0
while kaprikar(n)!=6174:
   n=kaprikar(n)
   i+=1
print(6174)
if i==0:
   print(0)
elif i==7:
   print(7)
else:
   print(i+1)