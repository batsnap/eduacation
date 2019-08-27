def Eratosthene_sieve(n):
    numbers=list(range(2,n+1))
    for i in range(2,int(n/2)):
        t=2*i

        while t<=n:
            numbers[t-2]=0
            t+=i
    numbers=list(set(numbers))
    numbers.remove(0)
    numbers.sort()
    
    return numbers
n=int(input())
print(Eratosthene_sieve(n))