# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-33. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
Дан список результатов сдачи экзамена учащимися школ некоторого района,
с указанием фамилии и имени учащегося, номера школы и итогового балла.
Напишите эффективную по времени работы и по используемой памяти
программу (укажите используемую версию языка программирования,
например, Borland Pascal 7.0), которая определяет номера школ, в которых
больше всего учащихся получило за экзамен максимальный балл среди всех
учащихся района. 
На вход программе в первой строке подается количество учащихся во всех
школах района N. В  каждой  из  последующих  N  строк  находится
информация  в следующем формате: 
    <Фамилия> <Имя> <Номер школы> <Балл>
где < Фамилия > - строка, состоящая не более, чем из 20 символов без
пробелов, <Имя>  -  строка,  состоящая не более, чем из  20  символов 
без пробелов, <Номер школы> - число от 1 до 99, <Балл> – число от 0 до 
100. Порядок следования строк - произвольный.
Пример входных данных:
    б
    Иванов Сергей 7 74
    Сергеев Петр 3 82
    Петров Кирилл 7 85
    Кириллов Егор 3 82
    Егоров Николай 7 85
    Николаев Иван 19 85
Программа должна вывести номера школ, из которых наибольшее количество 
учащихся получило на экзамене максимальный балл среди всех учащихся
района. Пример вывода для приведенного выше примера ввода:
    7
Примечание. В данном примере максимальный балл по району равен 85, его 
набрало 2 учащихся из школы 7 и 1 учащийся из школы 19, поэтому
выводится только номер школы 7.
При выполнении задания следует учитывать, что значение N может быть
велико (до 10.000).
"""
import sys, codecs
save_stdin = sys.stdin
sys.stdin = codecs.open("in/33.in", "r", "utf-8")

N = int(input())
cntMax = {}
maxBall = 0
for i in range(N):
    fam, name, school, ball = input().split()
    school, ball = int(school), int(ball)
    if ball > maxBall:
        maxBall = ball
        for sch in cntMax:
            cntMax[sch] = 0
    if ball == maxBall:
        cntMax[school] = cntMax.get(school,0) + 1

maxCount = max([x[1] for x in cntMax.items()])
for x in cntMax.items():
    if x[1] == maxCount:
        print(x[0])

sys.stdin = save_stdin