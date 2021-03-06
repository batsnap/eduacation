﻿# -*- coding: utf-8 -*-
"""
-------------------------------------------------
Задача C4-17. 
Решение на языке Python 3.
 Автор: Константин Поляков, 2013
E-mail: kpolyakov@mail.ru
   Web: kpolyakov.spb.ru
-------------------------------------------------
На вход программе подается текст заклинания, состоящего не более, чем
из 200 символов, заканчивающийся точкой (другие точки во входных 
данных отсутствуют). Гарри Поттеру нужно зашифровать его следующим
образом. Сначала Гарри определяет количество букв в самом коротком
слове, обозначив полученное число через K (словом называется
непрерывная последовательность английских букв, слова друга от друга
отделяются любыми другими символами, длина слова не превышает 20
символов). Затем он заменяет каждую английскую букву в заклинании на
букву, стоящую в английском алфавите на K букв ранее (алфавит
считается циклическим, то есть, перед буквой A стоит буква Z), оставив
другие символы неизменными. Строчные буквы при этом остаются
строчными, а прописные – прописными. 
Требуется написать программу для Гарри Поттера, которая будет выводить
на экран текст зашифрованного заклинания. Например, если исходный
текст был таким:
    Zb Ra Ca Dab Ra. 
то результат шифровки должен быть следующий:
    Xz Py Ay Byz Py.
"""
import sys
save_stdin = sys.stdin
sys.stdin = open("in/17.in")

import string
msg = sys.stdin.read().split('.')[0]
s = "".join(msg.split("\n"))
words = s.split()

K = min([len(w) for w in words])
L = len(string.ascii_uppercase)
msgNew = ""
for letter in msg:
    n = string.ascii_uppercase.find(letter)
    if n >= 0:
        letter = string.ascii_uppercase[(n + L - K) % L]
    n = string.ascii_lowercase.find(letter)
    if n >= 0:
        letter = string.ascii_lowercase[(n + L - K) % L]
    msgNew = msgNew + letter
print(msgNew + ".")

sys.stdin = save_stdin