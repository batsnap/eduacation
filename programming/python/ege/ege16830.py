k=6
n=int(input())
a=[int(input()) for i in range(k)]
n6=n3=n2=0
s=0
for i in range(k,n):
	x=int(input())
	if a[0]%6==0:
		n6+=1
	elif a[0]%3==0:
		n3+=1
	elif a[0]%2==0:
		n2+=1
	if x%6==0:
		s+=i-k+1
	elif x%3==0:
		s+=n2
	elif x%2==0:
		s+=n3
	for j in range(k-1):
		a[j]=a[j+1]
	a[k-1]=x
print(s)		
