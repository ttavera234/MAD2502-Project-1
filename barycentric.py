import numpy as np


def get_barycentric_coordinates(triangle_coordinates: np.ndarray, point_coordinates: np.ndarray) -> np.ndarray:
    """
    Description:
        Calculates the barycentric coordinates when given the triangle and point coordinates

    Parameters:
        triangle_coordinates: a 2x3 matrix in the form
                ([x1, x2, x3],
                 [y1, y2, y3])
        point_coordinates: a 1x2 matrix in the form
                ([x, y])

    Returns:
        The barycentric coordinates in the form of a 1-D array representing (lambda1, lambda2, lambda3)
    """

    """
        The barycentric coordinates are calculated by solving Ax=B; however, A and B must be converted into the following matrices:
        A:  (                                                 
                [x1, x2, x3],
                [y1, y2, y3],
                [ 1,   1,  1]
            )
            
        B:  (
                [x],
                [y],
                [1]
            )
            
        in order to solve for the lambda matrix:
            (
                [lambda1],
                [lambda2],
                [lambda3]
            )       
    """

    coefficient_matrix: np.array = np.insert(triangle_coordinates, 2, [1, 1, 1], axis=0)
    resultant_matrix: np.array = np.insert(point_coordinates, 2, [1], axis=0).reshape(3, 1)
    bary_coord = np.linalg.solve(coefficient_matrix, resultant_matrix).reshape(1, 3)
    return bary_coord


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
    """
    Parameters:
        triangle_coordinates: A 2x3 matrix containing coordinate:
                ([x1, x2, x3],
                 [y1, y2, y3])
        point_coordinates: A 1x2 matrix in the form of coordinates
                ([x, y])

    Returns:
        A boolean confirming whether a point is within a triangle based on the signs of the barycentric coordinates.
    """
    bary_coord = get_barycentric_coordinates(triangle_coordinates, point_coordinates)
    return np.all(bary_coord >= 0)

