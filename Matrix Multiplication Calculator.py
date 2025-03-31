import numpy as np 

def matrix_prod(A, B):
    n = len(A[:,0])  # define n as the row entries of A, or column entries of B
    C = np.copy(A)
    C = []  # C is initialised

    # Program calculates c, elements of the matrix C, to create each row of C
    for i in range(n):
        row = []  # new row is initialised
        for j in range(n):
            c = 0  # c is initialised
            for k in range(len(A[i])):
                c += A[i][k] * B[k][j]  # each element c is calculated
            row.append(c)  # each c is appended to the row
        
        C.append(row)  # each row is appended to the matrix C
        
    return C
