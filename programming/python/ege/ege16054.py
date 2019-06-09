n=int(input())
k=4
n29=s=0
a=[int(input()) for i in range(k)]
for i in range(k,n):
	x=int(input())
	if a[0]%29==0:
		n29+=1
	if x%29==0:
		s+=i-k+1
	else:
		s+=n29
	for i in range(k-1):
		a[i]=a[i+1]
	a[k-1]=x
print(s)
