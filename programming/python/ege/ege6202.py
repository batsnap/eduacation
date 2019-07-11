k=max7=max1=0
x=1
while x!=0:
	x=int(input())
	if x==0:
		break
	else:
		k+=1
		if x%7!=0 and x>max1:
			max1=x
		elif x%7==0 and x%49!=0 and x>max7:
			max7=x
ctr=int(input())
print('количество чисел',k)
print('контрольное значение',ctr)
if max7*max1==0:
	s=0
else:
	s=max7*max1
print('вычисленное значение',s)
if ctr==s:
	print('значения совпали')
else:
	print('значения не совпали')

