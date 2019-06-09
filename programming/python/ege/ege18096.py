n=int(input())
n62=n31=n2=0
for i in range(n):
	x=int(input())
	if x%62==0:
		n62+=1
	elif x%31==0:
		n31+=1
	elif x%2==0:
		n2+=1
s=n31*n2+(n-n62)*n62+((n62-1)*n62)//2
print(s)
