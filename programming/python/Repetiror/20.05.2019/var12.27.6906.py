n=int(input())
ymax=ymin=xmax=xmin=k=0
for i in range(n):
    x,y=map(int,input().split())
    if y==0:
        if x<=xmin:
            xmin=x
            k+=1
        elif x>=xmax:
            xmax=x
            k+=1
    elif y>ymax:
        ymax=y
    elif ymin>y:
        ymin=y
if k>1 and ymax!=0 and ymin!=0:
    print(abs(xmin-xmax)*0.5*(ymax-ymin))
else: 
    print(0)
