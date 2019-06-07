def chet(x,y):
	if y>0 and x>0:
		return 0
	elif y>0 and x<0:
		return 1
	elif y<0 and x<0:
		return 2
	else:
		return 3

n=int(input())
xymin=[[0,0,0,0],[0,0,0,0]]
chetvert=[0,0,0,0]
for i in range(n):
	x,y=map(int,input().split())
	if x!=0 and y!=0:
		chetvert[chet(x,y)]+=1
		if abs(x)<abs(xymin[0][chet(x,y)]) or abs(y)<abs(xymin[1][chet(x,y)]) or (xymin[0][chet(x,y)]==0 and xymin[1][chet(x,y)]==0):
			xymin[0][chet(x,y)]=x
			xymin[1][chet(x,y)]=y

k=chetvert.index(max(chetvert))
m=max(chetvert)
a='('+str(xymin[0][k])+','+str(xymin[1][k])+')'
r=min(abs(xymin[0][k]),abs(xymin[1][k]))
print('K=',k+1)
print('M=',m)
print('A=',a)
print('R=',r)