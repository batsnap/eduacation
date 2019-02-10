def lcm(a,b):
    m = a*b
    while a != 0 and b != 0:
        if a > b:
            a %= b
        else:
            b %= a
    return m // (a+b)
 
while 1:
    try:
        x,y=map(int,input().split())
        print(lcm(x,y))
    except:
        break