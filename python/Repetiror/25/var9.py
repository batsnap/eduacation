a=[]
k=0
n=5
for i in range(0,n):
	a.append(int(input()))
<<<<<<< HEAD
for i in range(n)
	for j in range(1,n):
		if a[i]%13==0 or a[j]%13==0:
=======
for i in range(n-1):
		if a[i]%13==0 or a[i+1]%13==0:
>>>>>>> 41325caabd2857ff129b70aa45ee0f163c5407e5
			k+=1
print(k)
