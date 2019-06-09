n=int(input())
a=[0 for i in range(18)]
for i in range(n):
	x=int(input())
	a[x%10+x%100//10]+=1
f=max(a)
k=a.index(max(a))
while max(a)==f:
	k=a.index(max(a))
	a[k]=-1
print(k)

