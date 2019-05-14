n=str(input())
k1=n[0]
k2=int(n[1])
a=['A','B','C','D','E','F','G','H']
if (a.index(k1)+1)%2==0 and k2%2==0:
   print('BLACK')
elif (a.index(k1)+1)%2==0 and k2%2==1:
   print('WHITE')
elif (a.index(k1)+1)%2==1 and k2%2==0:
   print('WHITE')
elif (a.index(k1)+1)%2==1 and k2%2==1:
   print('BLACK')