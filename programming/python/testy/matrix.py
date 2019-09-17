from random import randint
a=[]
for i in range (5):
   for j in range(5):
      a.append([])

for i in range (5):
   for j in range(5):
      a[i].append(0)
for i in range(5):
   print(a[i])


n=int(input())
b=[[randint(-100,100) for i in range(n)] for j in range(n)]