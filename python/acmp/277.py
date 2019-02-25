a,b,c=map(int,input().split())
if a>0 and b>0 and c>0:
   print(str(a)+'+'+str(b)+'x'+'+'+str(c)+'y')
elif a>0 and b<0 and c>0:
   print(str(a)+'-'+str(b)+'x'+'+'+str(c)+'y')
elif a>0 and b<0 and c<0:
   print(str(a)+'-'+str(b)+'x'+'-'+str(c)+'y')
elif a>0 and b>0 and c<0:
   print(str(a)+'+'+str(b)+'x'+'-'+str(c)+'y')
elif a==0 and b>0 and c>0:
   print(str(b)+'x'+'+'+str(c)+'y')
elif a==0 and b<0 and c>0:
   print('-'+str(b)+'x'+'+'+str(c)+'y')
elif a==0 and b<0 and c<0:
   print('-'+str(b)+'x'+'-'+str(c)+'y')
elif a==0 and b>0 and c<0:
   print(str(b)+'x'+'-'+str(c)+'y')
elif a!=0 and b==0 and c>0:
   print(str(a)+'+'+str(c)+'y')
elif a!=0 and b==0 and c<0:
   print(str(a)+'-'+str(c)+'y')
elif a!=0 and b==0 and c==0:
   print(str(a))
elif a!=0 and b>0 and c==0:
   print(str(a)+'-'+str(b)+'x')
elif a!=0 and <>0 and c==0:
   print(str(a)+'-'+str(b)+'x')

