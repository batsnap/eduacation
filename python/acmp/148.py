def nod(a,b:int):
   while a != 0 and b != 0:
      if a > b:
         a = a % b
      else:
         b = b % a
   return a+b
n,m=map(int,input().split())
print(nod(n,m))
