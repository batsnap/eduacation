n=int(input())
c=[0,2,4]+[0]*(n-2)
i=3
while i<n+1:
    c[i]=c[i-1]+i
    i+=1
print(c[n])