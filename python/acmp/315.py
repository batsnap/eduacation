a=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36]
b=['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
m=[]
s=str(input())
k=0
l=0
for i in range(len(s)):
   for j in range(36):
      if s[i]==b[j]:
         if k<a[j]:
            k=a[j]
      else:
         l+=1
   if l==36:
      break
   l=0
if s=='':
   print(-1)
elif l==36:
   print(-1)
elif k==1:
   print(2)
else:
   print(k)