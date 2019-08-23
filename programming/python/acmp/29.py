a=[[0 for i in range(8)] for j in range(8)]
#шахматная доска сверху
fer,lad,kon=map(str,input().split())
print(fer,lad,kon)
buk='ABCDEFGH'
print(buk.index(fer[0]))
a[buk.index(fer[0])][int(fer[1])-1]=1
if