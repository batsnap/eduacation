n=int(input())
a=[0 for i in range(9)]
for i in range(n):
	x=int(input())
	a[x%9]+=1
s=((a[0]-1)*a[0])//2+a[1]*a[8]+a[2]*a[7]+a[3]*a[6]+a[5]*a[4]
print(s)
