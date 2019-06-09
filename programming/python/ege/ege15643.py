n=int(input())
n34=n17=n2=0
for i in range(n):
	x=int(input())
	if x%34==0:
		n34+=1
	elif x%17==0:
		n17+=1
	elif x%2==0:
		n2+=1
print(((n-1)*n)//2-(n2*n17+n34*(n-n34)+((n34-1)*n34)//2))
