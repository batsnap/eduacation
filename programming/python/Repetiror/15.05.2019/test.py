from random import randint
import time
n=int(input())
t1=time.time()
b=[0 for i in range(0,16)]

for i in range(n):
    x=randint(1,16)
    b[x-1]+=1
print('')
while sum(b)!=0:
    print(b.index(max(b))+1,max(b))
    b[b.index(max(b))]=0
t2=time.time()
print('')
print("--- %s seconds ---"%(t2-t1))