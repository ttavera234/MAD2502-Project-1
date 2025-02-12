import numpy as np
def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    """area of trapezoid = (f(a) + f(b)) * (b-a)/2), where f(a) and f(b) are y values of the x vales, and b-a is height"""
    y_vals = func(x_vals)
    height = np.
    sum_of_trapezoids = np.sum(

    return sum_of_trapezoids

x_values = np.linspace(0, np.pi, 10000)
function = np.sin
trapezoid_sum = trapezoid(x_values, function)
print(trapezoid_sum)
