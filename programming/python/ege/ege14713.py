n=int(input())
a=[0 for i in range(7)]
for i in range(n):
	x=int(input())
	a[x%7]+=1
s=((a[0]-1)*a[0])//2+a[1]*a[6]+a[2]*a[5]+a[3]*a[4]
print(s)
