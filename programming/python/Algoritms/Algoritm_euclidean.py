#Алгоритм Евклида – это алгоритм нахождения наибольшего 
#общего делителя (НОД) пары целых чисел.

#Делением
def EVKdel(a,b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a+b)
#Вычитанием
def EVKvich(a,b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return(a)

print(EVKdel(10,2))
print(EVKvich(10,5))