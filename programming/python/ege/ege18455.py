n=int(input())
n10=n5=n2=0
for i in range(n):
	x=int(input())
	if x%10==0:
		n10+=1
	elif x%5==0:
		n5+=1
	elif x%2==0:
		n2+=1
s=n5*n2+(n-n10)*n10+((n10-1)*n10)//2
print(s)
