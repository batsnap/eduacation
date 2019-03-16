n=int(input())
k=n
a=[]
while n!=0:
   a.append(n%2)
   n//=2
print(sum(a)+k)