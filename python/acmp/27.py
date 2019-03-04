w,h=map(int,input().split())
n=int(input())
a=[[0]*w]*h
s=0
s1=w*h
for i in range(n):
	x1,y1,x2,y2=map(int,input().split())
	for i in range(y1+1,y2):
		for j in range(x1,x2):
			a[i][j]=1
for i in range(h):
	print(a[i])
	s=s+sum(a[i])
print(s1-s)
