k=8
n=int(input())
a=[int(input()) for i in range(k)]
amax=0
summax=0
for i in range(k,n):
	x=int(input())
	if a[0]>amax:
		amax=a[0]
	if x+amax>summax:
		summax=x+amax
	for j in range(k-1):
		a[j]=a[j+1]
	a[k-1]=x
print(summax)		
