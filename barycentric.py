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

def is_inside_triangle(triangle_coordinates: np.ndarray, point_coordinates) -> bool:
    x1, y1 = triangle_coordinates[:,0]
    x2, y2 = triangle_coordinates[:,1]
    x3, y3 = triangle_coordinates[:,2]
    px, py = point_coordinates

    def dire(x1, y1, x2, y2, x3, y3):
        return (x1 - x3) * (y2 - y3) - (x2 - x3) * (y1 - y3)

    d1 = dire(px, py, x1, y1, x2, y2)
    d2 = dire(px, py, x2, y2, x3, y3)
    d3 = dire(px, py, x3, y3, x1, y1)
    if (d1 <= 0) and (d2 <= 0) and (d3 <= 0):
        return True
    elif (d1 >= 0) and (d2 >= 0) and (d3 >= 0):
        return True
    else:
        return False
