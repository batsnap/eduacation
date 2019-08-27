def TENtoTWO(n):
    b = ''
    while n > 0:
        b = str(n % 2) + b
        n = n // 2
    return b
n = int(input())
print(TENtoTWO(n))