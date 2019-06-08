n=int(input())
n2=n29=n58=0
for i in range(n):
	x=int(input())
	if x%58==0:
		n58+=1
	elif x%29==0:
		n29+=1
	elif x%2==0:
		n2+=1
s=n2*n29+n58*(n-n58)+((n58-1)*n58)//2
print(s)