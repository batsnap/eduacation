n=int(input())
a=b=str()
k=[]
c=[]
for i in range(n):
    a,b=map(str,input().split())
    k.append(a)
    c.append(int(b))
    l=k.pop()
    h=