import numpy as np

# Create two matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6]])

matrix2 = np.array([[7, 8, 9],
                     [10, 11, 12]])

# Add the matrices
result = matrix1 + matrix2
print("Sum of matrices:")
print(result)

# Find the transpose of the result
transpose = result.transpose()
print("\nTranspose of the sum:")
print(transpose)