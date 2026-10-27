import numpy as np


def gaussian_eliminate(A, b):
    """
    A: a square (n, n) NumPy array that does not require row swaps
    b: a length-n NumPy array

    Returns:
        (U, c): U is A row-reduced to upper-triangular form, c is b
        transformed by the same row operations, such that Ux = c has
        the same solution as Ax = b.
    """
    # TODO: Implement elimination on copies of A and b in lockstep,
    # from Theory.
    U = np.array(A, dtype=float)
    c = np.array(b, dtype=float).reshape(-1, 1) # Reshape to column vector
    n = A.shape[0]
    for i in range(n):
        for j in range(i+1, n):
            factor = U[j, i]/U[i, i]
            # Apply row operations to matrix U (vectorized row subtraction)
            U[j, i:] -= factor * U[i, i:]
            # Apply the exact same operation to vector c
            c[j] -= factor * c[i]
    return U, c.flatten()
            
    """M = np.hstack(A, b) #Glue A and b horizontally
    n = len(b)
    for i in range(n):
        pivot_row = np.argmax(abs(M[i:, i])) + i
        if pivot_row != -1:
            M[i, pivot_row] = M[pivot_row, i]
        for j in range(i+1, n):
            factor = M[j, i]/M[i, i]
            M[j, i:] -= factor*M[i, i:]"""
    


def back_substitute(U, c):
    """
    U: an upper-triangular (n, n) NumPy array
    c: a length-n NumPy array

    Returns:
        x, the solution to Ux = c, solved from the last row up.
    """
    U = np.array(U, dtype=float)
    c = np.array(c, dtype=float)
    n = len(c)
    x = np.zeros(n)
    for i in range(n-1, -1, -1):
        # x[i] = (c[i] - sum(coefficients * already_solved_x)) / diagonal_element
        # NumPy's np.dot quickly multiplies and sums the known components
        x[i] = (c[i] - np.dot(U[i, i+1:], x[i+1:])) / U[i, i]
    return x
