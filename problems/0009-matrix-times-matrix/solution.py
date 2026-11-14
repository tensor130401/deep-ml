def matrixmul(a:list[list[int|float]],b:list[list[int|float]])-> list[list[int|float]]:
    if len(a[0])!=len(b):
        return -1
    x=len(a)
    y=len(a[0])
    z=len(b[0])
    c=[[0]*z for i in range(x)]
    for i in range(x):
        for j in range(z):
            for k in range(y):
                c[i][j]+=a[i][k]*b[k][j]
        
    return c