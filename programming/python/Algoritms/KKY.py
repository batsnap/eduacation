"""from math import sqrt
print('Введите коэфициенты')
a,b,c=map(int,input().split())
d=b*b-4*a*c
x1=(-b+sqrt(d))/(2*a)
x2=(-b-sqrt(d))/(2*a)
print('x1=',x1,'x2=',x2)"""
from sympy import *
init_printing(use_latex='png')
x=symbols('x')
