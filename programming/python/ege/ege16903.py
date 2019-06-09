k=10
n=int(input())
a=[int(input()) for i in range(k)]
n10=n5=n2=0
s=0
for i in range(k,n):
	x=int(input())
	if a[0]%10==0:
		n10+=1
	elif a[0]%5==0:
		n5+=1
	elif a[0]%2==0:
		n2+=1
	if x%10==0:
		s+=i-k+1
	elif x%5==0:
		s+=n2
	elif x%2==0:
		s+=n5
	for j in range(k-1):
		a[j]=a[j+1]
	a[k-1]=x
print(s)		
