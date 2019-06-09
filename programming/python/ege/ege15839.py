n=int(input())
n10=n5nechet=chet=nechet=0
for i in range(n):
	x=int(input())
	if x%10==0:
		n10+=1
	elif x%5==0 and x%2!=0:
		n5nechet+=1
	elif x%5!=0 and x%2==0:
		chet+=1
	elif x%5!=0 and x%2!=0:
		nechet+=1
s=n10*nechet+n5nechet*chet+n10*n5nechet
print(s)

