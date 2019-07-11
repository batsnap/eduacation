from time import sleep,time
k1=time()
s='abcdefghijklmnopqrstuvwxyz'
for i in range(26):
	for j in range(26):
		for k in range(26):
			print(s[i]+s[j]+s[k])
k2=time()
print('time work',k2-k1)
print('end')
