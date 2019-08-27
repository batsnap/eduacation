def changeFromTo(x,sis1,sis2):
    num=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
    k=len(x)-1
    s=0
    itog=''
    for i in range(len(x)):
        s+=num.index(x[i])*(sis1**k)
        k-=1
    while s>0:
        if s%sis2<10:
            itog+=num[num.index(str(s%sis2))]
            s//=sis2
        else:
            itog+=num[s%sis2]
            s//=sis2
    print('Итоговое число:',itog[::-1])
x=str(input('Введите число:'))
sis1=int(input('Введите систему счисление числа:'))
sis2=int(input('Введите систему счисление числа конечного:'))
changeFromTo(x,sis1,sis2)