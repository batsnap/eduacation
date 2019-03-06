w,h=map(int,input().split())
n=int(input())
a=[]
for i in range (100):
   for j in range(100):
      a.append([])
for i in range (100):
   for j in range(100):
      a[i].append(0)
s=0
s1=w*h
for i in range(n):
	x1,y1,x2,y2=map(int,input().split())
	for i in range(y1,y2):
		for j in range(x1,x2):
			a[j][i]=1
for i in range(100):
	s=s+sum(a[i])
print(s1-s)