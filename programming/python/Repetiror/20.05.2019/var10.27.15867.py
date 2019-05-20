n=int(input())
k2=k7=k14=0
ost=0
for i in range(n):
    x=int(input())
    if x%14==0:
        k14+=1
    elif x%2==0:
        k2+=1
    elif x%7==0:
        k7+=1

s=(n*(n-1))//2-(k2*k7+k14*(n-k14)+(k14*(k14-1))//2)
print(s)