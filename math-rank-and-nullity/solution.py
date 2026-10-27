import numpy as np


def rank(A):
    """
    A: an (m, n) NumPy array

    Returns:
        The rank of A: the number of linearly independent rows,
        computed via row-reduction (skip a column with no usable pivot
        rather than treating it as an error).
    """
    # TODO: Implement row-reduction with a separate pivot-row/pivot-
    # column pointer, counting pivots found, from Theory.
    m, n = A.shape
    # Use a small tolerance for floating point comparisons
    tol = 1e-8
    rank = 0
    pivot_row = 0
    pivot_col = 0
    # Create a copy to avoid modifying the original array
    a_copy = A.copy()

    while pivot_row < m and pivot_col < n:
        # Find the pivot in the current column, starting from pivot_row
        max_row = pivot_row
        for i in range(pivot_row + 1, m):
            if abs(a_copy[i, pivot_col]) > abs(a_copy[max_row, pivot_col]):
                max_row = i

        # If the pivot element is close to zero, move to the next column
        if abs(a_copy[max_row, pivot_col]) < tol:
            pivot_col += 1
            continue

        # Swap the current row with the row containing the pivot
        a_copy[[pivot_row, max_row]] = a_copy[[max_row, pivot_row]]

        # Normalize the pivot row
        pivot_element = a_copy[pivot_row, pivot_col]
        a_copy[pivot_row, :] /= pivot_element

        # Eliminate other rows
        for i in range(m):
            if i != pivot_row:
                factor = a_copy[i, pivot_col]
                a_copy[i, :] -= factor * a_copy[pivot_row, :]

        # Increment rank and move to the next pivot position
        rank += 1
        pivot_row += 1
        pivot_col += 1

    return rank


def nullity(A):
    """
    A: an (m, n) NumPy array

    Returns:
        The nullity of A: A.shape[1] - rank(A), per the Rank-Nullity
        Theorem.
    """
    # TODO: Implement using rank(A) from Theory's formula.
    return A.shape[1] - rank(A)
