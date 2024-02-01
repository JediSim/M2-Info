import numpy as np
from scipy.optimize import linprog

def simplex(A, b, c):
    m, n = A.shape
    tableau = np.zeros((m + 1, m + n + 1))
    
    tableau[:m, :n] = A
    tableau[:m, -1] = b
    tableau[-1, :n] = -c
    tableau[-1, -1] = 0
    
    while np.any(tableau[-1, :-1] < 0):
        pivot_col = np.argmin(tableau[-1, :-1])
        
        ratios = tableau[:-1, -1] / tableau[:-1, pivot_col]
        pivot_row = np.argmin(ratios)
        
        pivot_element = tableau[pivot_row, pivot_col]
        tableau[pivot_row, :] /= pivot_element
        
        for i in range(m + 1):
            if i != pivot_row:
                multiplier = tableau[i, pivot_col]
                tableau[i, :] -= multiplier * tableau[pivot_row, :]
    
    solution = {'x': tableau[:-1, -1], 'z': -tableau[-1, -1]}
    return solution

# exemple
c = np.array([-4, -5])
A = np.array([[1, 2], 
              [2, 1],
              [1,0],])
b = np.array([800, 700,300])

result = simplex(A, b, c)
print("Solution optimal:")
print("x =", result['x'])
print("z =", result['z'])

bnd = [(0, float("inf")),
       (0, float("inf"))]

opt = linprog(c = c, A_ub = A, b_ub = b, bounds = bnd, method="highs")
print(opt)