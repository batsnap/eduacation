k1=0
k2=0
for i in range(4):
   a,b=map(int,input().split())
   k1+=a
   k2+=b
if k1>k2:
   print(1)
elif k2>k1:
   print(2)
else:
   print('DRAW')