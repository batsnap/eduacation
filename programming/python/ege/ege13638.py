n=int(input())
a=[0 for i in range(9)]
for i in range(n):
	x=str(input())
	a[len(x)]+=1
print(a.index(min(a)),min(a))

