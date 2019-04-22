n=int(input())
razmin1=1000
razmin2=1000
razmin3=1000
summin=0
itog=0
for i in range (n):
   a=list(map(int,input(str(i+1)+':').split()))
   summin+=min(a)
   if razmin1>abs(a[0]-a[1]) and abs(a[0]-a[1])%4==1:
      razmin1=abs(a[0]-a[1])
   if razmin2>abs(a[0]-a[1]) and abs(a[0]-a[1])%4==2:
      razmin2=abs(a[0]-a[1])
   if razmin3>abs(a[0]-a[1]) and abs(a[0]-a[1])%4==3:
      razmin3=abs(a[0]-a[1])
if razmin1>razmin2+razmin3:
   razmin1=razmin2+razmin3
if razmin3>razmin2+razmin1:
   razmin3=razmin2+razmin1
if summin%4==3 and razmin1!=1000:
   itog=summin+razmin1
elif summin%4==2 and razmin2!=1000:
   itog=summin+razmin2
elif summin%4==1 and razmin3!=1000:
   itog=summin+razmin3
elif summin%4==0:
   itog=summin
print('raz1:',razmin1)
print('raz2:',razmin2)
print('raz3:',razmin3)
print('sum:',summin)
print('irog:',itog)