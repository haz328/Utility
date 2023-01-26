import numpy as np

def solve_y_from_ployfit(poly_coeffs, y):
    # get firstpositive root
    pc = poly_coeffs.copy()
    roots = (poly_coeffs - y).roots()
    for i in range(len(roots)):
        if np.isreal(roots[i]) and roots[i]>0:
                return np.real(roots[i])
    return -99999

    
def solve_maxmin_from_ployfit(poly_coeffs):
    
    deriv = poly_coeffs.deriv(m=1)
    x_max = solve_y_from_ployfit(deriv, 0)
    y_max = poly_coeffs(x_max)

    return x_max,y_max
