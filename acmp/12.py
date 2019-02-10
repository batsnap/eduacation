n=int(input())
s=0
for i in range(n):
    x,y,x1,y1,x2,y2,x3,y3,x4,y4=map(int,input().split())
    if((x>=x1)and(x<=x3)and(y>=y1)and(y<=y3)):
        s+=1
    elif ((x>=x2)and(x<=x4)and(y>=y2)and(y<=y4)):
        s+=1
print(s)