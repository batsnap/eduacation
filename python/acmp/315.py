a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16]
b=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
m=[]
s=str(input())
k=0
l=0
for i in range(len(s)):
   for j in range(16):
      if s[i]==b[j]:
         if k<a[j]:
            k=a[j]
      else:
         l+=1
   if l==16:
      break
   l=0
if l==16:
   print(-1)
elif k==1:
   print(-1)
else:
   print(k)