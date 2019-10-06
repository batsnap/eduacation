def tribonacci(signature, n):
    k=0
    plus=0
    if n>3:
        for i in range(n-3):
            for j in range(3):
                plus+=signature[k+j]
            signature.append(plus)
            k+=1
            plus=0
        return signature
    elif n==0:
        return []
    elif n==1:
        return [signature[0]]
    elif n==2:
        return [signature[0],signature[1]]
    elif n==3:
        return [signature[0],signature[1],signature[2]]