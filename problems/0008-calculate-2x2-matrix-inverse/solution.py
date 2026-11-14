def inverse_2x2(matrix: list[list[float]]) -> list[list[float]] | None:
    """
    Calculate the inverse of a 2x2 matrix.
    
    Args:
        matrix: A 2x2 matrix represented as [[a, b], [c, d]]
    
    Returns:
        The inverse matrix as a 2x2 list, or None if the matrix is singular
        (i.e., determinant equals zero)
    """
    # Your code here
    D=matrix[0][0]*matrix[1][1]-matrix[1][0]*matrix[0][1]
    if D==0:
        return None
    inv_mat=[x.copy() for x in matrix]
    inv_mat[0][0]=matrix[1][1]/D
    inv_mat[1][1]=matrix[0][0]/D
    inv_mat[0][1]*=-1/D
    inv_mat[1][0]*=-1/D
    return inv_mat
    pass