n=int(input())
a=[0 for i in range(9)]
for i in range(n):
	x=str(input())
	a[len(x)]+=1
f=max(a)
k=a.index(max(a))
s=[]
while max(a)==f:
	k=a.index(max(a))
	s.append(k)
	a[k]=-1
s.reverse()
for i in s:
	print(i)
