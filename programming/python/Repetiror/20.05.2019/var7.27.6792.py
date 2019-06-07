n=int(input())
a=[[],[]]
for i in range(n):
	d,k=map(int,input().split())
	if k%d!=0:
		if k%d not in a[0]:
			a[0].append(k%d)
			a[1].append(1)
		else:
			a[1][a[0].index(k%d)]+=1
k=max(a[1])
n=a[0][a[1].index(max(a[1]))]
for i in range(len(a[1])):
	if a[1][i]==k and n<a[0][i]:
		n=a[0][i]
print(n)