from math import factorial
def zeros(n):
    c=0
    for i in str(factorial(n)):
        if i=='0':
            c+=1
    return str(factorial(n))
print(zeros(100000))