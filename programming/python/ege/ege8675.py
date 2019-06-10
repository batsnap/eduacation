k=10
n=int(input())
a=[int(input()) for i in range(k)]
c=s=0
for i in range(n-k):
	x=int(input())
	if a[0]**2>c:
		c=a[0]
	if c**2*x**2>s:
		s=c**2*x**2
	for j in range(k-1):
		a[j]=a[j+1]
	a[k-1]=x
print(s)
