a1=list(map(int,input().split()))
a2=list(map(int,input().split()))
a1.sort()
a2.sort()
a1.reverse()
a2.reverse()
if a1[0]*a1[1]==a2[0]*a2[1] and a1[2]==a2[2]:
   print('Boxes are equal')
elif a1[0]*a1[1]==a2[0]*a2[1] and a1[2]>=a2[2]:
   print('The first box is larger than the second one')
elif a1[0]*a1[1]==a2[0]*a2[1] and a1[2]<=a2[2]:
   print('The first box is smaller than the second one')





elif a1[0]*a1[1]>a2[0]*a2[1] and a1[2]==a2[2]:
   print('The first box is larger than the second one')
elif a1[0]*a1[1]>a2[0]*a2[1] and a1[2]>=a2[2]:
   print('The first box is larger than the second one')
elif a1[0]*a1[1]>a2[0]*a2[1] and a1[2]<=a2[2]:
   print('Boxes are incomparable')
   




elif a1[0]*a1[1]<a2[0]*a2[1] and a1[2]==a2[2]:
   print('The first box is smaller than the second one')
elif a1[0]*a1[1]<a2[0]*a2[1] and a1[2]<a2[2]:
   print('The first box is smaller than the second one')
elif a1[0]*a1[1]<a2[0]*a2[1] and a1[2]>a2[2]:
   print('Boxes are incomparable')