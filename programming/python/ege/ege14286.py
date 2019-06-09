n=int(input())
a=[0 for i in range(18)]
for i in range(n):
	x=int(input())
	a[x%10+x%100//10]+=1
print(a.index(1))

