import numpy as np

def area_approximator(a, b, N, f):
    # Program checks that user inputs are in the correct format
    if N < 1: 
        print('Please ensure the value of N is greater than 1')
        exit()
    if a > b: 
        print('Please ensure the value of b is greater than the value of a')
        exit()
        
    # The width of each trapezium, w
    w = abs((b - a) / N)

    # A list containing the heights, or y values, of each trapezium's left and right sides, is created
    heights = np.linspace(a, b, N+1)
    realheights = [f(h) for h in heights]

    # The total area is found by summing the area of of all trapeziums
    area = 0
    for i in range(N):
        area += 0.5 * (realheights[i] + realheights[i+1]) * w

    return area

function = input('Define the function for x: ')
f = lambda x: eval(function)

# print(area_approximator(a, b, N, f))