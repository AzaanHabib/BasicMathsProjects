import itertools as it


def linear_convergence_analyser(a, b, x, t, N):
    # Program checks that user inputs are in the correct format
    if type(N) is not int:
        print('Please enter an integer value for N')
        exit()
    if 0 > N or N > 101:
        print('Please ensure the value of N is in between of 0 and 100')
        exit()

    # We define an iterative function f(x) = ax + b, and create a list, D, containing all its values
    f = lambda x: a*x + b 
    D = []
    for i in range(N):
        x = f(x)
        D.append(x)

    # To test for convergence, we check if the difference between any two elements of D is smaller or greater than the convergence tolerance
    for d1, d2 in it.pairwise(D):
        if d2 - d1 < t: 
            convergence = True

        elif d2 - d1 >= t:
            convergence = False

    # If we have convergence, we return the last value in D. If there is no convergence, we print a statement and return none
    if convergence == True:
        print('The function converges, and the last x value was ')
        return x

    elif convergence == False:
        print('The function does not converge')
        return 

# print(linear_convergence_analyser(a, b, x, t, N))
