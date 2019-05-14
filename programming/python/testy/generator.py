from random import randint,uniform
x=int(input())
y=int(input())
c=str()
b= [randint(0, 10) for i in range(x)] for j in range(y)]
for i in range(y):
    for j in range (x):
        c=str(b[i][j])
        print(c, end=' ')
    print()
