import numpy as np

def transform_matrix(A: list[list[int|float]], T: list[list[int|float]], S: list[list[int|float]]) -> list[list[int|float]]:
    D1=np.linalg.det(T)
    D2=np.linalg.det(S)
    if D1==0 or D2==0:
        return -1
    if len(T[0])!=len(A) or len(A[0])!=len(S):
        return -1
    T_inv=np.linalg.inv(T)
    transformed_matrix=T_inv@A@S
    return transformed_matrix