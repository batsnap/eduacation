a=int(input())
b=a
k=-1
if a>=0:
    while a!=0:
        a//=2
        k+=1
    if b==2**k:
        print('YES')
    else:
        print('NO')
else:
    print('NO')