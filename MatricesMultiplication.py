import numpy as np

def multiply_matrices(matrix1, matrix2):
    # First to check the inputs are whether empty or not
    if not (isinstance(matrix1, list) and isinstance(matrix2, list) and matrix1 and matrix2):
        raise ValueError("Inputs must be non-empty matrices.")

    # Second to check inputs are whether matrices or not
    if not (all(isinstance(row, list) for row in matrix1) and all(isinstance(row, list) for row in matrix2)):
        raise ValueError("Inputs must be matrices (lists of lists).")
        
    # Helper function to check if all elements in a matrix are integers
    def are_elements_integers(matrix):
        return all(isinstance(element, int) for row in matrix for element in row)
    if not (are_elements_integers(matrix1) and are_elements_integers(matrix2)):
        raise ValueError("All elements in the matrices must be integers.")

    # Convert lists to numpy arrays
    matrix1 = np.array(matrix1)
    matrix2 = np.array(matrix2)

    # Check if the matrices can be multiplied
    if matrix1.shape[1] != matrix2.shape[0]:
        raise ValueError("Matrices cannot be multiplied: "
                         "Number of columns in the first matrix must be equal to the number of rows in the second matrix.")

    # Matrix multiplication
    return np.dot(matrix1, matrix2)
