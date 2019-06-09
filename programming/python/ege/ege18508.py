k=6
n=int(input())
a=[int(input()) for i in range(k)]
chet=nechet=0
maxsum=0
s=0
for i in range(k,n):
	x=int(input())
	if a[0]%2==0 and a[0]>chet:
		chet=a[0]
	elif a[0]%2!=0 and a[0]>nechet:
		nechet=a[0]
	s=0
	if x%2==0 and nechet>0:
		s=x+nechet
	elif x%2!=0 and chet>0:
		s=x+chet
	if s>maxsum:
		maxsum=s
	for j in range(k-1):
		a[j]=a[j+1]
	a[k-1]=x
print(maxsum)
	
