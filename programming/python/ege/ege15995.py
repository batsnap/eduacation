n=int(input())
k=5
n13=s=0
a=[int(input()) for i in range(k)]
for i in range(k,n):
	x=int(input())
	if a[0]%13==0:
		n13+=1
	if x%13==0:
		s+=i-k+1
	else:
		s+=n13
	for i in range(k-1):
		a[i]=a[i+1]
	a[k-1]=x
print(s)
