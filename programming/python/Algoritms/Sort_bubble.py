from random import randint

def Sort_bubble(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]

n=int(input())
a = [randint(0,100) for i in range(n)]
Sort_bubble(a)
print(a)

#время O(n^2)