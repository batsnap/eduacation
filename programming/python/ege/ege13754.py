n=int(input())
n26=n13=n2=0
for i in range(n):
	x=int(input())
	if x%26==0:
		n26+=1
	elif x%13==0:
		n13+=1
	elif x%2==0:
		n2+=1
s=n2*n13+n26*(n-n26)+((n26-1)*n26)//2
print(s)

