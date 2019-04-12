def f(x):
   if x>0:
      return x*x+4
   else:
      return x*x+5
a=-11
b=11
m=a
r=f(a)
for t in range(a,b+1):
   if f(t)<=r:
      m=t
      r=f(t)
      print(m,r)
      print(t,'   ')
      print('     ')
print(m+r)