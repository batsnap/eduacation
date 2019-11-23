from random import randint
def minor(matrix,k):
    i1=j1=0
    s=[[0 for i in range(len(matrix[0])-1)] for j in range(len(matrix[0])-1)]
    for i in range(1,len(matrix[0])):
        for j in range(len(matrix[0])):
            if j!=k :
                s[i1][j1]=matrix[i][j]
                j1+=1
        j1=0
        i1+=1
    return s
def opredelitel(matrix):
    s=0
    if len(matrix[0])!=2:
        for i in range(len(matrix[0])):
            if i%2==0:
                s=s+matrix[0][i]*opredelitel(minor(matrix,i))
            else:
                s=s-(matrix[0][i]*opredelitel(minor(matrix,i)))
        return s
    else:
        return matrix[0][0]*matrix[1][1]-matrix[0][1]*matrix[1][0]
a=[[7,-2,-5],[-10,7,-2],[-8,-10,-3]]

print('det',opredelitel(a))
