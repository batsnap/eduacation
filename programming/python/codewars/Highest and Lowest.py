def high_and_low(numbers):
    a=list(map(int,numbers.split()))
    return str(max(a))+' '+str(min(a))
print(high_and_low('4 5 29 54 4 0 -214 542 -64 1 -3 6 -6'))