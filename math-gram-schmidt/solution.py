import numpy as np


def gram_schmidt(vectors):
    """
    vectors: a list of 1D NumPy arrays, all the same length, guaranteed
             linearly independent

    Returns:
        A list of the same length: an orthonormal basis (unit length,
        mutually perpendicular) spanning the same space, built by
        processing vectors in the given order.
    """
    # TODO: Implement Gram-Schmidt from Theory: for each vector, subtract
    # its projection onto every already-built basis vector, then
    # normalize what's left.
    basis = []
    for v in vectors:
        w = v.copy()
        for u in basis:
            projection = np.dot(v, u) * u
            w -= projection
        norm_w = np.linalg.norm(w)
        if norm_w > 1e-10:  # Avoid division by zero for near-zero vectors
            basis.append(w / norm_w)
    return basis
