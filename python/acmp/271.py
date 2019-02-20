n=int(input())
fib1 = 1
fib2 = 1
k=-1
i = 0
a=[1,1]
while i < n - 2:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
    a.append(fib_sum)
for i in range(len(a)):
    if a[i]==n:
        k=i
if k>0:
    print(1)
    print(k+1)
else:
    print(0)

