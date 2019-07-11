from time import sleep
s='abcdefghijklmnopqrstuvwxyz'
k=1
c=0
x=True
while x==True:
	if k%26!=0:
		print(s[c]+s[k])
		k+=1
	elif c!=25:
		c+=1
		k=1
	else:
		x=False
print('end')
