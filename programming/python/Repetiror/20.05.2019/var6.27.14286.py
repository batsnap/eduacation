n=int(input())
b=[i for i in range(19)]
a=[0]*19
for i in range(n):
	x=int(input())
	a[x%10+(x%100)//10]+=1
print(b)
x=n+1
for i in range(19):
	if a[i]<x and a[i]!=0:
		x=a[i]
print(a.index(x))