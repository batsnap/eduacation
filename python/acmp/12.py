def cormax(x1,y1,x2,y2:int):
   if x1>x2 and y1>y2:
      return true
   elif x2>x1 and y2>y1:
      rerutn false
n=int(input())
a=[]
xmax=[]
for i in range(n):
    x,y,x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
    
