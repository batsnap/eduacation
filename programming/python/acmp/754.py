def chek(a):
    if a>94 and a<727:
        return True

a,b,c=map(int,input().split())
s=[a,b,c]
if chek(a) and chek(b) and chek(c):
    print(max(s))
else:
    print('Error')