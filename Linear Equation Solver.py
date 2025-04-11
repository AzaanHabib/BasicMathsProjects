import numpy as np 

def gaussian_elimination(A_in, b_in):
    n = A_in.shape[0]
    x = np.zeros(n)
    A = np.copy(A_in)
    b = np.copy(b_in)

    for k in range(n - 1):

        for i in range(k + 1, n):

            mult = A[i, k] / A[k, k]

            for j in range(k, n):
                A[i, j] -= mult * A[k, j]
            

            b[i] -= mult * b[k]
        
        # end of i loop 

    # back substitution 
    x[-1] = b[-1]/A[-1,-1]
    for i in range(n - 1, -1, -1):
        s = b[i]
        for j in range(i + 1, n):
            s -= A[i, j] * x[j]
        x[i] = s / A[i, j]
    
    return A, x

A = np.array([[1., 2., 3.], [2., 3., 4.], [5., 6., 1.]])
b = np.array([3., 4., 7.])

A, x = gaussian_elimination(A, b)

print(f'Solution {x}')
print(f'Upper triangular A: {A}')

