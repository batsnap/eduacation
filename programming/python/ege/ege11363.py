n=int(input())
maxsum=0
raznmin=0
for i in range(n):
	a,b=map(int,input().split())
	if a>b:
		maxsum+=a
	else:
		maxsum+=b
	if abs(a-b)%3>0 and abs(a-b)<10001:
		raznmin=abs(a-b)
if maxsum%3==0:
	if raznmin>10001:
		maxsum=0
	else:
		maxsum-=raznmin
print(maxsum)