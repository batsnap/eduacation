def ProizvDigit(a):
    proizv=1
    while a>0:
        digit=a%10
        proizv*=digit
        a//=10
    return proizv
print(ProizvDigit(112345))