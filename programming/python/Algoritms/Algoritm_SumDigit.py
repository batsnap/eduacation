def SumDigit(a):
    suma=0
    while a>0:
        digit=a%10
        suma+=digit
        a//=10
    return suma
print(SumDigit(112345))