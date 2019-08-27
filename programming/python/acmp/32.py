def znak(x):
    if int(x)>0:
        return True
    else:
        return False
def Brazvp(x):
    a=[]
    k=''
    for i in range(len(x)):
        a.append(int(x[i]))
    for i in range(len(a)):
        k+=str(max(a))
        a[a.index(max(a))]=-1
    return int(k)
def Mrazvp(x):
    a=[]
    k=''
    for i in range(len(x)):
        a.append(int(x[i]))
    for i in range(len(a)):
        k+=str(min(a))
        a[a.index(min(a))]=100000000000
    return int(k)
def Mrazvm(k):
    x=str(int(k)*(-1))
    a=[]
    k=''
    for i in range(len(x)):
        a.append(int(x[i]))
    for i in range(len(a)):
        k+=str(min(a))
        a[a.index(min(a))]=100000000000
    return int(k)*(-1)
def Brazvm(k):
    x=str(int(k)*(-1))
    a=[]
    k=''
    for i in range(len(x)):
        a.append(int(x[i]))
    for i in range(len(a)):
        k+=str(max(a))
        a[a.index(max(a))]=-1
    return int(k)*(-1)
def main(a,b):
    if znak(a) and znak(b):
        if Brazvp(a)>Brazvp(b):
            print(Brazvp(a)-Mrazvp(b))
        elif Brazvp(b)>Brazvp(a):
            print(Brazvp(b)-Mrazvp(a))
    elif not znak(a) and znak(b):
        print(Brazvp(b)-Brazvm(a))
    elif not znak(b) and znak(a):
        print(Brazvp(a)-Brazvm(b))
    else:
        if Brazvm(a)>Brazvm(b):
            print(Mrazvm(b)-Brazvm(a))
        elif Brazvm(b)>Brazvm(a):
            print(Mrazvm(a)-Brazvm(b))
l=str(input())
m=str(input())
main(l,m)