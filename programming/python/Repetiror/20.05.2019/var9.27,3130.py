from random import randint
s=''
s1=''
k=0
for i in range(30):
    x=randint(-1000,1000)
    if x>=0:
        s+=str(x)+' '
        k+=1
    else:
        s1+=str(x)+' '
print(s1+s)