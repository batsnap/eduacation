def kmp_matcher(t,p):
    n=len(t)
    m=len(p)
    
    pi = compute_prefix_function(p)
    q=-1
    for i in range(n):
        while(q>0 and p[q]!=t[i]):
            q=pi[q]
        if(p[q]==t[i]):
            q=q+1
        if(q==m):
            print ('pattern occurs with shift '+str(i-m))
            q=pi[q]


def compute_prefix_function(p):
    m=len(p)
    pi=[0]*m
    k=0
    for q in range(2,m):
        while(k>0 and p[k]!=p[q]):
            k=pi[k]
        if(p[k]==p[q]):
            k=k+1
        pi[q]=k
    return pi

t = '1 1 1 1'
p = '1'
print(kmp_matcher(t,p))