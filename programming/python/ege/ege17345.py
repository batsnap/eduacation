k=6
n=int(input())
a=[int(input()) for i in range(k)]
chet=nechet=0
s=0
for i in range(k,n):
	x=int(input())
	if a[0]%2==0:
		chet+=1
	else:
		nechet+=1
	if x%2==0:
		s+=nechet
	else:
		s+=chet
	for j in range(k-1):
		a[j]=a[j+1]
	a[k-1]=x
print(s)		
