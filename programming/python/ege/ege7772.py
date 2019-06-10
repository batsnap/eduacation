k=8
n=int(input())
a=[int(input()) for i in range(k)]
c=s=0
for i in range(n-k):
	x=int(input())
	if a[0]>c:
		c=a[0]
	if c*x>s:
		s=c*x
	for j in range(k-1):
		a[j]=a[j+1]
	a[k-1]=x
print(s)
