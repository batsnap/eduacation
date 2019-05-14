w,h=map(int,input().split())
n=int(input())
a=[]
for i in range (w):
   for j in range(h):
      a.append([])
for i in range (w):
   for j in range(h):
      a[i].append(0)
s=0
s1=w*h
for i in range(n):
	x1,y1,x2,y2=map(int,input().split())
	for i in range(y1,y2):
		for j in range(x1,x2):
			a[i][j]=1
for i in range(w):
	for j in range(h):
		s=s+a[i][j]
print(s1-s)