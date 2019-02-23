import math
def IsPrime(n):
   if (math.factorial(n - 1) + 1) % n != 0:  # Теорема Вильсона
      return False
   else:
      return True
n=int(input())
k=10**(len(str(n))-1)
IsPrime(n)
if n%k==0:
   print(k)
elif IsPrime(n):
   print(1)
else:
   print(n)

