import numpy as np

def dot_product(v, w):

    n = len(v)
    m = len(w)

    # Program returns an error message if both vectors are not the same length
    if m != n:
        raise ValueError('Calculation cannot be completed')  
    
    # Program returns the dot product, s, defined as the sum of each element of v and w multiplied together
    else:
        s = 0  # s is initialised
        for i in range(n):  # for loop iterates over entire length of both vectors
            s += (v[i] * w[i])  # dot product is defined, and each new term is added to s
    return s  # final value of s is returned




