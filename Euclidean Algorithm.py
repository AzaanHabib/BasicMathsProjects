

def highest_divisor(N, D):
    # Program checks that user inputs are in the correct format
    if type(N) is not int:
        print('Please enter an integer value for N')
        exit()
    if type(D) is not list:
        print('Please enter a list value for D')
        exit()

    # The highest divisor is found from a collection of all divisors of N, that are in list D
    highest_divisor = []
    for k in D:
        if N%k == 0:
            highest_divisor.append(k)
    
    
    if len(highest_divisor) == 0:
        print('There are no divisors')
        return

    else:
        return max(highest_divisor)
    
# print(highest_divisor(5, [6, 2, 7]))


