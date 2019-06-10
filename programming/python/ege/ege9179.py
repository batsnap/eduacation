k=9
n=int(input())
a=[float(input()) for i in range(k)]
c=s=2001.0
for i in range(n-k):
	x=float(input())
	if a[0]<c:
		c=a[0]
	if (c+x)/2<s:
		s=(c+x)/2
	for j in range(k-1):
		a[j]=a[j+1]
	a[k-1]=x
print(s)
