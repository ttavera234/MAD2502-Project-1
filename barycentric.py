import numpy as np
def get_cartesian_coordinates(triangle_coordinates: np.ndarray[[2, 3]], barycentric_coordinates: np.ndarray[[1,3]]) -> np.ndarray:
    x_y = np.matmul(barycentric_coordinates, triangle_coordinates)
    return x_y

