n=int(input())
n14=n7=n2=maxn=0
for i in range(n):
	x=int(input())
	if x%14==0 and x>n14:
		n14=x
	elif x%7==0 and x>n7:
		n7=x
	elif x%2==0 and x>n2:
		n2=x
	elif x>maxn:
			maxn=x
if n2*n7>n14*maxn and n2*n7>n14*n2 and n2*n7>n14*n7:
	print(n2*n7)
elif n2*n7<n14*maxn and n14*maxn>n14*n2 and n14*maxn>n14*n7:
	print(n14*maxn)
elif n2*n7<n14*n2 and n14*maxn<n14*n2 and n14*n2>n14*n7:
	print(n14*n2)
	
