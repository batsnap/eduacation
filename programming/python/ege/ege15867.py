n=int(input())
n14=n7=n2=0
for i in range(n):
	x=int(input())
	if x%14==0:
		n14+=1
	elif n%7==0:
		n7+=1
	elif x%2==0:
		n2+=1
s=n2*n7+(n-n14)*n14+((n14-1)*n14)//2
print(s)
