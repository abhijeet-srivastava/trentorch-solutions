import numpy as np


def qr_decompose(A):
    """
    A: an (m, n) NumPy array with linearly independent columns

    Returns:
        (Q, R): Q is (m, n) with orthonormal columns, R is (n, n)
        upper-triangular, such that Q @ R reconstructs A exactly.
    """
    # TODO: Implement Gram-Schmidt column by column, recording each
    # projection coefficient into R and each leftover norm into R's
    # diagonal, from Theory.
    m, n = A.shape
    Q = np.zeros((m, n), dtype=float)
    R = np.zeros((n, n), dtype=float)
    V = A.astype(float).copy()

    for k in range(n):
         # 1. Record the leftover norm of the current column
        R[k,k] = np.linalg.norm(V[:, k])
        # 2. Generate the unit vector for Q
        Q[:, k]  = V[:, k]/R[k,k]
        # 3. Project and subtract this new vector out of all REMAINING columns
        for j in range(k+1, n):
            # Record the projection coefficient
            #R[k,j] = np.dot(V[:, k], Q[:, j])
            R[k,j] = np.dot(Q[:, k], V[:, j])
            # Subtract the projection to make column j orthogonal to Q[:, k]
            V[:, j] -= R[k, j]*Q[:,k]
    return Q, R
