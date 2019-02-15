from random import randint,uniform
x=int(input())
y=int(input())
c=str()
l=open('output.txt','w')
l=l.write('test')
l.write(str(5))
b= [[randint(0, 10) for i in range(x)] for j in range(y)]
for i in range(y):
    for j in range (x):
        c=str(b[i][j])
        print(c)
        l.write(c)
        l.write(' ')
    l.write('\n')
