import numpy as np
import scipy


def lu_decompose(A):
    """
    A: a square (n, n) NumPy array that does not require row swaps
       (every pivot encountered during elimination is non-zero)

    Returns:
        (L, U): L is lower-triangular with 1s on the diagonal, U is
        upper-triangular, such that L @ U reconstructs A exactly.
    """
    n = A.shape[0]
    U = A.astype(float).copy()
    # Initialize L as the identity matrix (ones on the diagonal, zeros elsewhere)
    L = np.eye(n, dtype =float)
    for col in range(n):
        for row in range(col+1, n):
            factor = U[row, col]/U[col, col]
            L[row, col] = factor
            U[row] = U[row] - factor * U[col]
    return L, U
