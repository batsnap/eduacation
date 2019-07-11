k=6
m=1001
s=10001
n=int(input())
a=[float(input()) for i in range(k)]
for i in range(n-k):
	x=float(input())
	if a[0]<m:
		m=a[0]
	if m*x<s:
		s=m*x
print('контрольное значние:',s)
	
