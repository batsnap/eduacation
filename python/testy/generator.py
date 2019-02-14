from random import randint,uniform
x=int(input())
y=int(input())
b= [[randint(0, 10) for i in range(x)] for j in range(y)]
for i in range(y):
    for j in range (x):
        print(b[i][j],end=' ')
    print()
