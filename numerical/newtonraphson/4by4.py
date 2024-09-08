import numpy as np

def cramer(mat, constant):
    D = np.linalg.det(mat)
    mat1 = np.array([constant, mat[:, 1], mat[:, 2]])
    mat2 = np.array([mat[:, 0], constant, mat[:, 2]])
    mat3 = np.array([mat[:, 0], mat[:, 1], constant])
    Dx = np.linalg.det([mat1, mat2, mat3])
    X = Dx/D
    print(X)

cramer([[2,5],[5,-4]],[26,-1])