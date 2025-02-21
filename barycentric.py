import numpy as np
def get_cartesian_coordinates(triangle_coordinates: np.ndarray, barycentric_coordinates: np.ndarray) -> np.ndarray:
    """
    Parameters:
        triangle_coordinates: a 2x3 matrix representing triangle coordinates in the shape
                ([x1, x2, x3],
                [y1, y2, y3])
        barycentric_coordinates: a 1x3 matrix representing lambdas in the shape
                ([lambda1,lambda2, lambda3])

    Return:
        a 1-D array representing (x,y)
    """
    x_y = np.matmul(triangle_coordinates, barycentric_coordinates)
    return x_y

