a=[]
k=0
n=5
for i in range(0,n):
	a.append(int(input()))
for i in range(n-1):
		if a[i]%13==0 or a[i+1]%13==0:
			k+=1
print(k)
