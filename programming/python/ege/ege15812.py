n=int(input())
n6=n3nechet=nechet=chet=0
for i in range(n):
	x=int(input())
	if x%6==0:
		n6+=1
	elif x%3==0 and x%2!=0:
		n3nechet+=1
	elif x%3!=0 and x%2==0:
		chet+=1
	elif x%3!=0 and x%2!=0:
		nechet+=1
s=n6*nechet+chet*n3nechet+n6*n3nechet
print(s)

