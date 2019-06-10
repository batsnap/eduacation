n=int(input())
chet=nechet=-1
R=0
for i in range(n):
	x=int(input())
	if x%2==0 and x>chet:
		chet=x
	elif x%2!=0 and x>nechet:
		nechet=x
if nechet==-1 or chet==-1:
	print(-1)
else:
	print(chet+nechet)
	
