n=int(input())
a=list(map(int,input().split()))
i=1
k=2
b1=(a[i-1]<a[i] and a[i]>a[i+1]) or not (a[i-1]>a[i] and a[i]<a[i+1])
while b1:
  i+=1
  k+=1
print(k)
