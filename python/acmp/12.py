from math import sqrt,pi,acos
def vector(x1,y1,x2,y2:int):
   x3=abs(x1-x2)
   y3=abs(y1-y2)
   return sqrt(x3**2+y3**2)
s=0
n=int(input())
for i in range(n):
   x,y,x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
   s1=acos((vector(x,y,x1,y1)**2+vector(x,y,x2,y2)**2-vector(x1,y1,x2,y2)**2)/(2*vector(x,y,x1,y1)*vector(x,y,x2,y2)))
   s2=acos((vector(x,y,x3,y3)**2+vector(x,y,x2,y2)**2-vector(x3,y3,x2,y2)**2)/(2*vector(x,y,x3,y3)*vector(x,y,x2,y2)))
   s3=acos((vector(x,y,x3,y3)**2+vector(x,y,x4,y4)**2-vector(x3,y3,x4,y4)**2)/(2*vector(x,y,x3,y3)*vector(x,y,x4,y4)))
   s4=acos((vector(x,y,x1,y1)**2+vector(x,y,x4,y4)**2-vector(x1,y1,x4,y4)**2)/(2*vector(x,y,x1,y1)*vector(x,y,x4,y4)))
   if (s1+s2+s3+s4)<=2*pi:
      s+=1
print(s)