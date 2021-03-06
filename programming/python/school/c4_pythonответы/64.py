# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-64. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2016
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
64)	На спутнике «Восход» установлен прибор, предназначенный для измерения солнечной активности. В течение времени эксперимента (это время известно заранее) прибор каждую минуту передаёт в обсерваторию по каналу связи положительное целое число, не превышающее 1000, - количество энергии солнечного излучения, полученной за последнюю минуту, измеренное в условных единицах.
После окончания эксперимента передаётся контрольное значение наибольшее число R, удовлетворяющее следующим условиям:
1.	R – произведение двух различных переданных элементов последовательности («различные» означает, что не рассматриваются квадраты переданных чисел, произведения различных, но равных по величине элементов допускаются);
2.	R не делится на 26.
В результате помех при передаче как сами числа, так и контрольное значение могут быть искажены. 
Напишите эффективную по времени и используемой памяти программу, которая будет проверять правильность контрольного значения. Программа должна напечатать отчёт по следующей форме.
Вычисленное контрольное значение: ...
Контроль пройден (или Контроль не пройден) 
Если удовлетворяющее условию контрольное значение определить невозможно, то выводится только фраза «Контроль не пройден».
Перед текстом программы кратко опишите используемый Вами алгоритм решения. 
На вход программе в первой строке подаётся количество чисел N. В каждой из последующих N строк записано одно положительное целое число, не превышающее 1000. В последней строке записано контрольное значение.
Пример входных данных: 
5 
52 
12 
39 
55 
23 
2145 
Пример выходных данных для приведённого выше примера входных данных:
Вычисленное контрольное значение: 2145
Контроль пройден

"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/64.in")

N = int(input())

m0_1 = 0; m0_2 = 0
m2_1 = 0; m2_2 = 0
m13_1 = 0; m13_2 = 0

for i in range(N):
  a = int(input())
  if a% 26 != 0:
    if a % 2 == 0:
      if a > m2_1:
        m2_2 = m2_1; m2_1 = a
      elif a > m2_2: m2_2 = a
    elif a % 13 == 0:
      if a > m13_1:
        m13_2 = m13_1; m13_1 = a
      elif a > m13_2: m13_2 = a
    else:
      if a > m0_1:
        m0_2 = m0_1; m0_1 = a
      elif a > m0_2: m0_2 = a

R = int(input())
M = max( m0_1*m0_2, m0_1*m2_1, m0_1*m13_1, 
         m2_1*m2_2, m13_1*m13_2 )
if M > 0:
  print('Вычисленное контрольное значение:', M);
if R == M:
  print('Контроль пройден.')
else:  
  print('Контроль не пройден.')

sys.stdin = save_stdin