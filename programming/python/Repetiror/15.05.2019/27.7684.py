# -*- coding: utf-8 -*-
n=int(input())
chet=0
nechet=0

for i in range(n):
    x=int(input())
    if x%2==1 and x>nechet:
        nechet=x
    elif x%2==0 and x>chet:
        chet=x
if chet==0 or nechet==0:
    R=-1
    
else:
    R=nechet+chet
print('Вычисленное контрольное значение:',R)
if R==-1:
    print('Контроль не пройден')
else:
    print('Контроль пройден')