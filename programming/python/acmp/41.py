n=int(input())
a=list(map(int,input().split()))
a.sort()
s=''
for i in range(n):
    s+=str(a[i])+' '
print(s)
