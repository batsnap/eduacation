a=[2,4,6,1,7,2,3,6,7,2]
s=0
for i in range(9):
  if a[i]<a[i+1]:
    a[i+1]-=a[i]
  else:
    a[i]-=a[i+1]
  s+=a[i]
print(s)
