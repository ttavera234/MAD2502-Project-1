import numpy as np
def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    Calculates area of trapezoids under curve using vertices (a,0), (a, f(a)), (b,0), and (b, f(b))
    Area of trapezoid = (f(a) + f(b)) * (b-a)/2), where f(a) and f(b) are y values of the x vales, and b-a is height.

    Parameters:
        x_vals: an 1-d array of the x-values used in determining the integral
        func: universal function that the integral is taken of

    Returns:
        sum_of_trapezoids: a float that is the sum of all the trapezoids used to approximate the area
    """
    y_vals = func(x_vals)
    height = np.
    sum_of_trapezoids = np.sum

    return sum_of_trapezoids


