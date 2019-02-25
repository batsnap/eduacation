n=int(input())
ost=[0]*12
for i in range(n):
    a=int(input())
    ost[a%12]+=1
for i in range(6,1):
    for j in range(1,6):
        i