from multiprocessing import Process, Pool
from time import time

def proizvedenie_array(line):
    a=1;
    for i in range(len(line)):
        a*=line[i]
    return a
    

if __name__=='__main__':
    for g in range(4):

        n=[10,40,80,115]
        a=[[(i*13)**3 for i in range(1,n[g]+1)] for j in range(1,n[g]+1)]
        k=time()
        pool = Pool(processes=2)
        s=proizvedenie_array(pool.map(proizvedenie_array, a))
        print(time()-k)
        
        s=1
        k=time()
        for i in range(n[g]):
            s*=proizvedenie_array(a[i])
        print(time()-k)