a=[[5 for i in range(10)] for j in range(10)]
diag1=diag=k=0
for i in range(10):
	diag1+=a[i][9-i]
	diag+=a[i][i]
stolb=stroka=0
if diag1==diag:
	for i in range(10):
		for j in range(10):
			stolb+=a[j][i]
		stroka=sum(a[i])
		if stolb!=stroka:
			print('no')
			k+=1
			break
		else:
			stolb=stroka=0
if k==0:
	print('yes')
