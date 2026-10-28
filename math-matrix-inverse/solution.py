import numpy as np
#import torch


def determinant(a: np.ndarray) -> float:
    """
    Mirrors np.linalg.det(a) / torch.linalg.det(a): a single scalar
    that is zero exactly when a is singular (not invertible).
    """
    #return float(np.linalg.det(a))
    r, c = a.shape
    if r == 1 and c == 1:
        return a
    if r == 2 and c == 2:
        return a[0,0]*a[1,1] - a[0,1]*a[1,0]
    determinent = 0
    for col in range(c):
        sub_matrix = np.delete(np.delete(a, 0, axis=0), col, axis=1)
        sign = (-1) ** col
        determinent += sign*a[0, col] * determinant(sub_matrix)
    return determinent
        


def is_invertible(a: np.ndarray) -> bool:
    """
    A square matrix is invertible iff its determinant is nonzero.
    Compare against 0 with a tolerance (np.isclose), not exact equality:
    floating-point determinant computations essentially never land on
    a bit-exact 0.0 even for a truly singular matrix.
    """
    #det = np.linalg.det(a)
    det = determinant(a)
    return not np.isclose(det, 0.0)

def get_determinant(matrix: np.ndarray) -> float:
    """Calculates the determinant of an n x n matrix recursively."""
    r, c = matrix.shape
    if r == 1:
        return float(matrix[0, 0])  # Explicitly extract the scalar element
        
    if r == 2:
        # FIX: Access scalar elements using commas instead of element-wise array operations
        return float(matrix[0, 0] * matrix[1, 1] - matrix[0, 1] * matrix[1, 0])
    
    det = 0.0
    for col in range(c):
        sub_matrix = np.delete(np.delete(matrix, 0, axis=0), col, axis=1)
        sign = (-1) ** col
        det += sign * matrix[0, col] * get_determinant(sub_matrix)
    return det
    
def matrix_inverse(a: np.ndarray) -> np.ndarray:
    """
    Mirrors np.linalg.inv(a): the matrix A^-1 such that A @ A^-1 == I.

    Raise np.linalg.LinAlgError if `a` is not invertible (check with
    is_invertible first), rather than letting a near-singular matrix
    silently produce huge, meaningless numbers.
    """
    if not is_invertible(a):
        raise np.linalg.LinAlgError("No inverse exists for singular matrix")
    return np.linalg.pinv(a)
    """r, c = a.shape
    if r != c:
        raise np.linalg.LinAlgError("Inverse of non square matrix do not exist")
    det = get_determinant(a)
    if not np.isclose(det, 0.0):
        raise np.linalg.LinAlgError("Inverse do not exist for singular matrix")
    if r == 1:
        return np.array([[1.0 / det]])
    cofactor_matrix = np.zeros(r,c)
    for row in range(r):
        for col in range(c):
            # Extract the sub-matrix by dropping the current row and column
            sub = np.delete(np.delete(matrix, row, axis=0), col, axis=1)
            # Cofactor = (-1)**(i+j) * det(sub-matrix)
            sign = (-1) ** (row + col)
            cofactor_matrix[row, col] = sign * get_determinant(sub)
    # Adjugate matrix is the Transpose of the Cofactor matrix
    adjugate_matrix = cofactor_matrix.T
    # Inverse = (1 / determinant) * adjugate
    return adjugate_matrix / det"""
