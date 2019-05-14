n=int(input())
b=[]
for i in range(n):
    a=list(map(int,input().split()))
    while a[0] != 0 and a[1] != 0:
        if a[0] > a[1]:
            a[0] %= a[1]
        else:
            a[1] %= a[0]
    b.append(a[0]+a[1])
b_d = {}.fromkeys(b, 0)
for c in b:
    b_d[c] += 1
max_value = max(b_d.values())
final_dict = {k: v for k, v in b_d.items() if v == max_value}
for i in final_dict:
    print(i)