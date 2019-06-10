n=int(input())
n6=n3nechet=chet=nechet=m6max=n3nechetmax=chetmax=nechetmax=0
s1=s2=s3=0
for i in range(n):
	x=int(input())
	if x%6==0 and x>n6max:
		n6max=x
		n6+=1
	elif x%3==0 and x%2!=0 and x>n3nechetmax:
		n3nechet+=1
		n3nechetmax=x
	elif x%3!=0 and x%2!=0 and x>nechetmax:
		nechet+=1
		nechetmax=x
	elif x%3!=0 and x%2==0 and x>chetmax:
		chetmax=x
		chet+=1
if n6>0 and nechet>0:
	s1=n6max+nechetmax
if n3nechet>0 and chet>0:
	s2=n3nechetmax+chetmax
if n6>0 and n3nechet>0:
	s3=n6max+n3nechetmax
c=[s1,s2,s3]
k=c.index(max(c))
if max(c)!=0:
	if k==0:
		print(n6max,nechetmax)
	elif k==1:
		print(n3nechetmax,chetmax)
	elif k==2:
		print(n6max,n3nechetmax)
else:
	print(0)