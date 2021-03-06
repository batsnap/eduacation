# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-61. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2015
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
61) По каналу связи передаются положительные целые 
числа, не превышающие 1000 – результаты измерений, 
полученных в ходе эксперимента (количество измерений 
N известно заранее, гарантируется, что 2 < N  10000). 
После окончания эксперимента передаётся контрольное значение – наибольшее число R, удовлетворяющее следующим условиям.
1. R – сумма двух различных переданных элементов 
последовательности («различные» означает, что нельзя 
просто удваивать переданные числа, суммы различных, 
но равных по величине элементов допускаются).
2. R кратно 3.
3. Если в последовательности нет двух чисел, сумма 
которых кратна 3, контрольное значение считается равным 1.
В результате помех при передаче как сами числа, так 
и контрольное значение могут быть искажены.
Напишите эффективную, в том числе по используемой памяти, 
программу, которая будет проверять правильность контрольного 
значения. Программа должна напечатать отчёт по следующей форме:
Вычисленное контрольное значение: …
Контроль пройден (или Контроль не пройден)
Пример входных данных:
 6
 100
 8
 33
 145
 19
 84
 153
Пример выходных данных для приведенного выше примера входных данных:
  Вычисленное контрольное значение: 153
  Контроль пройден.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/61.in")

m3a = 0; m3b = 0; m1 = 0; m2 = 0;
N = int(input())
for i in range(N):
    x = int(input())
    if x % 3 == 0: 
        if x > m3a: 
            m3b = m3a            
            m3a = x
        elif x > m3b:
            m3b = x                
    if x % 3 == 1 and x > m1: m1 = x
    if x % 3 == 2 and x > m2: m2 = x
R = 1
if m1*m2 > 0:  R = m1 + m2
if m3a*m3b > 0  and  m3a+m3b > R:  R = m3a + m3b
R0 = int(input())

if R > 0: 
  print('Вычисленное контрольное значение: ', R)
if R > 0 and R == R0:
    print('Контроль пройден.')
else:
    print('Контроль не пройден.');

sys.stdin = save_stdin