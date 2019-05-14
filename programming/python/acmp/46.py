n=int(input())
s='71828182845904523536028751'

k='2.'
if n==0:
   print(3)
else:
   for i in range(n-1):
      k=k+s[i]
   if int(s[n])>=5:
      l=str(int(s[n-1])+1)
      k=k+l
   else:
      k=k+s[n-1]
   print(k)