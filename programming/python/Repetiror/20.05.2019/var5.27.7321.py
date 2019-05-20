n=int(input())
t=int(input())
y=t
y1=y2=x=0
for i in range(n):
	a,b=map(int,input().split())
	x+=a
	y1=y+b
	y2=x+t
	if y1<y2:
		y=y1
	else:
		y=y2
print(y)

    