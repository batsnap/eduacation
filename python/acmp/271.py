n=int(input())
fib1 = 1
fib2 = 1
k=-1
i = 0
a=[1,1]
fib_sum=0
while i < 1200000000 - 2 and fib_sum<n and fib_sum!=n:
    fib_sum = fib1 + fib2
    fib1 = fib2
    fib2 = fib_sum
    i = i + 1
if fib_sum==n:
    print(1)
    print(i+2)
else:
    print(0)
