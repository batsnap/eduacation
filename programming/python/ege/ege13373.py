n13=n26=n2=nmax=0
m=0
n=int(input())
for i in range(n):
	x=int(input())
	if x%26==0 and x>n26:
		n26=x
	elif x%7==0 and x>n7:
		n7=x
	elif x%2==0 and x>n2:
		n2=x
	elif x>nmax:
		nmax=x
	if x*n26>m:
		m=x*n26
	if x*n2>m:
		m=x*n2
	if x*n13>m:
		m=x*n2
	if x*nmax>m:
		m=x*n2
	if x*n2>m:
		m=x*n2
	if x*n13>m:
		m=x*n13
print('контрольное значние ',m)
if m==0:
	print('контроль не пройден')
else:
	print('контроль пройден')

