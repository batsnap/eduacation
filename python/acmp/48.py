n=str(input())
j=len(n)-1
while n[j]=='0':
   j-=1
j=len(n)-j-1
k='1'
while j>0:
   k=k+'0'
   j-=1
print(k)
