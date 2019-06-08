def summa(x):
	return x%10+x%100//10+x//100
n=int(input())
a=[0 for i in range(27)]
for i in range(n):
	k=int(input())
	a[summa(k)]+=1
print('ответ:',a.index(max(a)))
