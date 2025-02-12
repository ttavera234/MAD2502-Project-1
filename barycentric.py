import numpy as np
def get_cartesian_coordinates(triangle_coordinates: np.ndarray, barycentric_coordinates: np.ndarray) -> np.ndarray:
    """
    Parameters:
        triangle_coordinates: a 2x3 matrix representing triangle coordinates
        barycentric_coordinates: a 1x3 matrix representing lambdas

    Return:
        a 1-d array representing (x,y)
    """
    x_y = np.matmul(barycentric_coordinates, triangle_coordinates)
    return x_y

