from threading import Thread
from time import sleep
from math import exp
def test(k):
    x=1
    c=1.0
    while exp(1)-c>=float(k):
        c=(1.0+1.0/x)**x
        x+=1
    print(c)
a=[0.00000001,0.00000001,0.00000001,0.00000001,0.00000001]
for i in range(0,5):
    k=str(a[i])
    thread1 = Thread(target=test, args=(k,))
    thread1.start()