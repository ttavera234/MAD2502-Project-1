import numpy as np


def left_endpoint(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    Description:
        Approximates the area between a curve and the x-axis using rectangular heights and widths.
        The height of the rectangle is f(a) and the width is (b-a).

    Parameters:
        x_vals: a one-dimensional NumPy array containing the x-values used in approximating the integral (x[0] = a and x[-1] = b)
        func: a NumPy universal function to approximate the integral with (f(x))

    Returns:
        The sum of all the rectangular areas
    """

    rectangle_heights = func(x_vals[:-1])
    rectangles_widths = x_vals[1:] - x_vals[:-1]
    area_approx = np.sum(rectangle_heights * rectangles_widths)
    return area_approx


def trapezoid(x_vals: np.ndarray, func: np.ufunc) -> float:
    """
    Calculates area of trapezoids under curve using vertices
    Area of trapezoid = (f(a) + f(b)) * (b-a)/2), where f(a) and f(b) are y values of the x values, and b-a is the width between x-values.

    Parameters:
        x_vals: an 1-d array of the x-values used in determining the integral
        func: universal function that the integral is taken of

    Returns:
        sum_of_trapezoids: a float that is the sum of all the trapezoids used to approximate the area
    """
    y_vals = func(x_vals)
    lengths_per_x_vals = y_vals[:-1] + y_vals[1:]
    widths = x_vals[1:] - x_vals[:-1]
    sum_of_trapezoids = np.sum((lengths_per_x_vals * widths)/2)

    return sum_of_trapezoids

