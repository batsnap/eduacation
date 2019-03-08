   n,m,y,x=map(int,input().split())
   a=[]
   for i in range (n):
      for j in range(m):
         a.append([])
      for j in range(m):
         a[i].append(0)
   k=0
   for i in range (n):
      if i%2==0:
         for j in range(m):
            a[i][j]=k
            k+=1
      else:
         for j in range(0,m):
            a[i][m-j-1]=k
            k+=1
   print(a[y-1][x-1])