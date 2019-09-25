def Descending_Order(num):
    #Bust a move right here(
    a=[]
    s=str(num)
    itog=''
    for i in range(len(str(num))):
        a.append(int(s[i]))
    for i in range(len(a)):
        itog+=str(a[a.index(max(a))])
        a[a.index(max(a))]=-1
    return itog
print(Descending_Order(1234))