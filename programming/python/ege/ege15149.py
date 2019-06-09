n=int(input())
a=[0 for i in range(10)]
for i in range(n):
	x=int(input())
	a[x%10]+=1
s=((a[0]-1)*a[0])//2+a[1]*a[9]+a[2]*a[8]+a[3]*a[7]+a[6]*a[4]+((a[5]-1)*a[5])//2
print(s)
