import numpy as np

def make_diagonal(x):
    # Your code here
    l=len(x)
    diag=np.zeros((l,l))
    for i in range(l):
        diag[i][i]=x[i]
    return diag
    pass