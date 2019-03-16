a=[]
n=5
for i in range(0,n):
	a.append(int(input())
for i in range(n):
	for j in range(1,n):
		if a[i]%13==0 or a[j]%13==0:
			k+=1
print(k)
