from random import randint

def maxArray(a):
    k=a[0]
    for i in range(len(a)):
        if a[i]>k:
            k=a[i]
    return k

n=int(input())
a = [randint(0,100) for i in range(n)] 
print(a)
print(maxArray(a))