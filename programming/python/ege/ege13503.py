n=int(input())
a=[0 for i in range(10)]
for i in range(n):
	x=int(input())
	while x>0:
		a[x%10]+=1
		x//=10
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

