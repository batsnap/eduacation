n=int(input())
k=6
a=[int(input()) for i in range(k)]
n1=n2=n0=0
s=0
for i in range(k,n):
	x=int(input())
	if a[0]%3==0:
		n0+=1
	elif a[0]%3==1:
		n1+=1
	elif a[0]%3==2:
		n2+=1
	if x%3==0:
		s+=n0
	elif x%3==1:
		s+=n2
	elif x%3==2:
		s+=n1
	for j in range(k-1):
		a[j]=a[j+1]
	a[k-1]=x
print(s)
