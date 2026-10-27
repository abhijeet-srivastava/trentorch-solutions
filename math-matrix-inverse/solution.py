import numpy as np
#import torch


def determinant(a: np.ndarray) -> float:
    """
    Mirrors np.linalg.det(a) / torch.linalg.det(a): a single scalar
    that is zero exactly when a is singular (not invertible).
    """
    return float(np.linalg.det(a))


def is_invertible(a: np.ndarray) -> bool:
    """
    A square matrix is invertible iff its determinant is nonzero.
    Compare against 0 with a tolerance (np.isclose), not exact equality:
    floating-point determinant computations essentially never land on
    a bit-exact 0.0 even for a truly singular matrix.
    """
    det = np.linalg.det(a)
    return not np.isclose(det, 0.0)


def matrix_inverse(a: np.ndarray) -> np.ndarray:
    """
    Mirrors np.linalg.inv(a): the matrix A^-1 such that A @ A^-1 == I.

    Raise np.linalg.LinAlgError if `a` is not invertible (check with
    is_invertible first), rather than letting a near-singular matrix
    silently produce huge, meaningless numbers.
    """
    if not is_invertible(a):
        raise np.linalg.LinAlgError("Inverse do not exist for singular matrix")
    return np.linalg.pinv(a)
