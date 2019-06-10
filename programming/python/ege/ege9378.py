k=6
n=int(input())
a=[int(input()) for i in range(k)]
chet=nechet=1001
s=10001
for i in range(n-k):
	x=int(input())
	if a[0]%2==0 and a[0]<chet:
		chet=a[0]
	elif a[0]%2!=0 and a[0]<nechet:
		nechet=a[0]
	if x%2==0:
		if x*chet<s and chet<nechet:
			s=x*chet
		elif x*nechet<s and nechet<chet:
			s=x*nechet
	else:
		if x*chet<s:
			s=x*chet
	for j in range(k-1):
		a[j]=a[j+1]
	a[k-1]=x
if s%2==0:
	print(s)
else:
	print(-1)
