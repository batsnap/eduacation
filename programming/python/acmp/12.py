from math import sqrt
def vector(x1,y1,x2,y2:int):
   x3=abs(x2-x1)
   y3=abs(y2-y1)
   s=sqrt(x3**2+y3**2)
   return s
def streyg(x,y,x1,y1,x2,y2:int):
   p=(vector(x,y,x1,y1)+vector(x,y,x2,y2)+vector(x1,y1,x2,y2))/2
   s=sqrt(p*(p-vector(x,y,x1,y1))*(p-vector(x,y,x2,y2))*(p-vector(x1,y1,x2,y2)))
   return s
n=int(input())
s0=0
s1=0
k=0
for i in range (n):
   x,y,x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
   s0=vector(x1,y1,x2,y2)*vector(x2,y2,x3,y3)
   s1=streyg(x,y,x1,y1,x2,y2)+streyg(x,y,x2,y2,x3,y3)+streyg(x,y,x3,y3,x4,y4)+streyg(x,y,x1,y1,x4,y4)
   if round(s1)==round(s0):
      k+=1
print(k)
